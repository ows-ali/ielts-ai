"""End-to-end test for badges, public profiles and the community endpoints.

Run against a running backend (uvicorn app.main:app --port 8000):

    python -m scripts.test_community
    python -m scripts.test_community --api http://localhost:8000

Creates fresh teacher/student accounts, produces a speaking evaluation (real
Gemini call) plus a writing submission with feedback, then verifies
/api/me/badges, /api/users/{id}/profile and /api/community. Cleans up after
itself. Requires SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY in .env.
"""

import argparse
import io
import os
import struct
import sys
import uuid
import wave

import httpx
from dotenv import load_dotenv

load_dotenv()

PASSWORD = "E2EPass!2026"
PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {name}")
    else:
        FAIL += 1
        print(f"[FAIL] {name} {('- ' + detail) if detail else ''}")


def _admin_headers(key: str) -> dict:
    return {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }


def _bearer(token: str) -> dict:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def make_wav_bytes() -> bytes:
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(8000)
        w.writeframes(b"\x00\x00" * 4000)
    return buf.getvalue()


class Flow:
    def __init__(self, api_base: str, supabase_url: str, key: str, http: httpx.Client):
        self.api = api_base
        self.url = supabase_url.rstrip("/")
        self.key = key
        self.http = http
        self.suffix = uuid.uuid4().hex[:8]
        self.teacher_id = None
        self.student_id = None
        self.teacher_token = None
        self.student_token = None
        self.room = None
        self.audio_path = None

    def sign_in(self, email: str) -> str:
        resp = self.http.post(
            f"{self.url}/auth/v1/token?grant_type=password",
            headers=_admin_headers(self.key),
            json={"email": email, "password": PASSWORD},
        )
        resp.raise_for_status()
        return resp.json()["access_token"]

    def create_user(self, email: str, role: str) -> str:
        resp = self.http.post(
            f"{self.url}/auth/v1/admin/users",
            headers=_admin_headers(self.key),
            json={
                "email": email,
                "password": PASSWORD,
                "email_confirm": True,
                "user_metadata": {"role": role, "name": f"E2E {role.title()}"},
            },
        )
        resp.raise_for_status()
        return resp.json()["id"]

    def ensure_audio_bucket(self) -> None:
        existing = self.http.get(
            f"{self.url}/storage/v1/bucket/audio", headers=_admin_headers(self.key)
        )
        if existing.status_code != 200:
            resp = self.http.post(
                f"{self.url}/storage/v1/bucket",
                headers=_admin_headers(self.key),
                json={"name": "audio", "public": True},
            )
            if resp.status_code != 201:
                raise RuntimeError(f"could not create audio bucket: {resp.text[:200]}")
        else:
            self.http.put(
                f"{self.url}/storage/v1/bucket/audio",
                headers=_admin_headers(self.key),
                json={"public": True},
            )

    def upload_audio(self) -> str:
        self.ensure_audio_bucket()
        path = f"e2e/{self.suffix}.wav"
        self.audio_path = path
        resp = self.http.post(
            f"{self.url}/storage/v1/object/audio/{path}",
            headers={
                "apikey": self.key,
                "Authorization": f"Bearer {self.key}",
                "Content-Type": "audio/wav",
                "x-upsert": "true",
            },
            content=make_wav_bytes(),
        )
        if resp.status_code not in (200, 201):
            raise RuntimeError(f"audio upload failed: {resp.status_code} {resp.text[:200]}")
        return f"{self.url}/storage/v1/object/public/audio/{path}"

    def delete_user(self, user_id: str) -> None:
        try:
            self.http.delete(
                f"{self.url}/auth/v1/admin/users/{user_id}",
                headers=_admin_headers(self.key),
            )
        except Exception as exc:
            print(f"  (cleanup warning) delete user {user_id}: {exc}")

    def delete_room(self, room_id: str) -> None:
        try:
            self.http.delete(
                f"{self.url}/rest/v1/rooms?id=eq.{room_id}",
                headers={**_admin_headers(self.key), "Prefer": "return=minimal"},
            )
        except Exception as exc:
            print(f"  (cleanup warning) delete room {room_id}: {exc}")

    def delete_audio(self) -> None:
        if not self.audio_path:
            return
        try:
            self.http.request(
                "DELETE",
                f"{self.url}/storage/v1/object/audio",
                headers=_admin_headers(self.key),
                json={"prefixes": [self.audio_path]},
            )
        except Exception as exc:
            print(f"  (cleanup warning) delete audio {self.audio_path}: {exc}")

    def delete_writing_submission(self, submission_id: str) -> None:
        try:
            self.http.delete(
                f"{self.url}/rest/v1/writing_submissions?id=eq.{submission_id}",
                headers={**_admin_headers(self.key), "Prefer": "return=minimal"},
            )
        except Exception as exc:
            print(f"  (cleanup warning) delete writing submission {submission_id}: {exc}")

    def run(self) -> None:
        t_email = f"e2e_{self.suffix}_teacher@example.com"
        s_email = f"e2e_{self.suffix}_student@example.com"
        print(f"teacher: {t_email}")
        print(f"student: {s_email}")

        self.teacher_id = self.create_user(t_email, "teacher")
        self.student_id = self.create_user(s_email, "student")
        self.teacher_token = self.sign_in(t_email)
        self.student_token = self.sign_in(s_email)

        # ---- Speaking evaluation so badges have real data ----
        created = self.http.post(
            f"{self.api}/api/rooms",
            headers=_bearer(self.teacher_token),
            json={"title": "Badge Test Room", "part": 1},
        )
        check("create room (teacher)", created.status_code == 201, created.text)
        if created.status_code == 201:
            self.room = created.json()
            joined = self.http.post(
                f"{self.api}/api/rooms/join",
                headers=_bearer(self.student_token),
                json={"room_code": self.room["room_code"]},
            )
            check("join room (student)", joined.status_code == 200, joined.text)
            started = self.http.post(
                f"{self.api}/api/rooms/{self.room['id']}/start",
                headers=_bearer(self.teacher_token),
            )
            question_id = started.json().get("question_id") if started.status_code == 200 else None
            audio_url = self.upload_audio()
            transcript = (
                "I work as a software engineer. In my free time I enjoy reading and "
                "travelling. I like meeting new people and learning about different cultures."
            )
            answer = self.http.post(
                f"{self.api}/api/rooms/{self.room['id']}/answers",
                headers=_bearer(self.student_token),
                json={
                    "room_id": self.room["id"],
                    "question_id": question_id,
                    "audio_url": audio_url,
                    "transcript": transcript,
                },
            )
            ok = answer.status_code == 200 and answer.json().get("overall_band") is not None
            check("submit speaking answer -> evaluation (Gemini)", ok, answer.text)

        # ---- Writing submission + feedback ----
        question = self.http.get(
            f"{self.api}/api/writing/questions?part=1",
            headers=_bearer(self.student_token),
        )
        qid = question.json()[0]["id"] if question.status_code == 200 and question.json() else None
        submission_id = None
        if qid:
            sub = self.http.post(
                f"{self.api}/api/writing/submissions",
                headers=_bearer(self.student_token),
                json={
                    "question_id": qid,
                    "answer_text": (
                        "This is a test writing answer for the badge end-to-end flow. "
                        "It describes the main trends in the chart over the period shown. "
                        "Overall the figures increased steadily throughout the decade."
                    ),
                    "part": 1,
                },
            )
            check("submit writing answer (student)", sub.status_code == 201, sub.text)
            if sub.status_code == 201:
                submission_id = sub.json()["id"]
                fb = self.http.post(
                    f"{self.api}/api/writing/feedback",
                    headers=_bearer(self.teacher_token),
                    json={
                        "submission_id": submission_id,
                        "task_achievement": 7,
                        "coherence_cohesion": 7,
                        "lexical_resource": 7,
                        "grammatical_range": 7,
                        "overall_comment": "Well structured answer.",
                    },
                )
                check("teacher gives writing feedback", fb.status_code == 200, fb.text)

        # ---- Badges / profile / community ----
        badges = self.http.get(
            f"{self.api}/api/me/badges", headers=_bearer(self.student_token)
        )
        check("GET /api/me/badges", badges.status_code == 200, badges.text)
        if badges.status_code == 200:
            earned = {b["id"] for b in badges.json().get("badges", []) if b.get("earned")}
            check("first_step earned", "first_step" in earned, str(earned))
            check("first_draft earned", "first_draft" in earned, str(earned))
            check("feedback_seeker earned", "feedback_seeker" in earned, str(earned))
            check(
                "earned_count matches badges",
                badges.json().get("earned_count") == len(earned),
                str(badges.json()),
            )

        profile = self.http.get(
            f"{self.api}/api/users/{self.student_id}/profile",
            headers=_bearer(self.student_token),
        )
        check("GET /api/users/{id}/profile", profile.status_code == 200, profile.text)
        if profile.status_code == 200:
            body = profile.json()
            check("profile name matches", body.get("name") == "E2E Student", body.get("name"))
            check(
                "profile exposes badges",
                isinstance(body.get("badges"), list) and len(body["badges"]) > 0,
                str(body),
            )
            check(
                "profile shows only earned badges",
                isinstance(body.get("badges"), list)
                and all(b.get("earned") for b in body["badges"])
                and len(body["badges"]) == body.get("earned_count"),
                str(body),
            )
            check(
                "profile has aggregate stats",
                isinstance(body.get("stats"), dict),
                str(body),
            )

        # The profile endpoint is public: must work without any token.
        anon_profile = self.http.get(
            f"{self.api}/api/users/{self.student_id}/profile",
            headers={"Content-Type": "application/json"},
        )
        check(
            "public profile works without auth",
            anon_profile.status_code == 200,
            anon_profile.text,
        )

        profile404 = self.http.get(
            f"{self.api}/api/users/{uuid.uuid4()}/profile",
            headers=_bearer(self.student_token),
        )
        check("profile 404 for unknown user", profile404.status_code == 404, profile404.text)

        community = self.http.get(
            f"{self.api}/api/community", headers=_bearer(self.student_token)
        )
        check("GET /api/community", community.status_code == 200, community.text)

        anon_community = self.http.get(
            f"{self.api}/api/community",
            headers={"Content-Type": "application/json"},
        )
        check(
            "public community works without auth",
            anon_community.status_code == 200,
            anon_community.text,
        )
        if community.status_code == 200:
            body = community.json()
            week_ids = [e["user_id"] for e in body.get("week", [])]
            all_ids = [e["user_id"] for e in body.get("all", [])]
            activity_actors = [a["actor_id"] for a in body.get("activity", [])]
            check("student on weekly board", self.student_id in week_ids, str(week_ids))
            check("student on all-time board", self.student_id in all_ids, str(all_ids))
            check(
                "student appears in activity feed",
                self.student_id in activity_actors,
                str(activity_actors),
            )
            check(
                "activity entry has detail",
                any(
                    isinstance(a.get("detail"), str) and a["detail"]
                    for a in body.get("activity", [])
                ),
                str(body),
            )

        # Clean up writing submission (cascades feedback)
        if submission_id:
            self.delete_writing_submission(submission_id)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Run the badges/community integration test.")
    parser.add_argument("--api", default="http://localhost:8000")
    args = parser.parse_args()

    supabase_url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
    if not supabase_url or not key:
        raise SystemExit("SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set in .env")

    flow = Flow(args.api, supabase_url, key, httpx.Client(timeout=120))
    try:
        flow.run()
    except Exception as exc:
        check("unexpected exception", False, f"{type(exc).__name__}: {exc}")
    finally:
        if flow.teacher_id:
            flow.delete_user(flow.teacher_id)
        if flow.student_id:
            flow.delete_user(flow.student_id)
        if flow.room:
            flow.delete_room(flow.room["id"])
        flow.delete_audio()

    print(f"\n{PASS} passed, {FAIL} failed")
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
