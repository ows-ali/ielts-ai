"""End-to-end integration test for the IELTS AI Speaking Classroom API.

Run this against a running backend (uvicorn app.main:app --port 8000):

    python -m scripts.test_flow
    python -m scripts.test_flow --api http://localhost:8000

The test creates fresh teacher/student accounts, runs the full classroom flow
(sign in -> create room -> join -> start -> submit answer -> reports), then
cleans up both users and the room. Requires SUPABASE_URL and
SUPABASE_SERVICE_ROLE_KEY in .env. The answer step makes real Gemini calls.
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

    def run(self) -> None:
        t_email = f"e2e_{self.suffix}_teacher@example.com"
        s_email = f"e2e_{self.suffix}_student@example.com"
        print(f"teacher: {t_email}")
        print(f"student: {s_email}")

        self.teacher_id = self.create_user(t_email, "teacher")
        self.student_id = self.create_user(s_email, "student")
        self.teacher_token = self.sign_in(t_email)
        self.student_token = self.sign_in(s_email)

        me = self.http.get(f"{self.api}/api/auth/me", headers=_bearer(self.teacher_token))
        check("sign in + /api/auth/me (teacher)", me.status_code == 200, me.text)
        if me.status_code == 200:
            check("role is teacher", me.json().get("role") == "teacher", me.text)

        created = self.http.post(
            f"{self.api}/api/rooms",
            headers=_bearer(self.teacher_token),
            json={"title": "E2E Test Room", "part": 1},
        )
        check("create room (teacher)", created.status_code == 201, created.text)
        if created.status_code != 201:
            return
        self.room = created.json()
        room_code = self.room["room_code"]
        room_id = self.room["id"]
        check("room starts waiting", self.room.get("status") == "waiting", created.text)

        joined = self.http.post(
            f"{self.api}/api/rooms/join",
            headers=_bearer(self.student_token),
            json={"room_code": room_code},
        )
        check("join room (student)", joined.status_code == 200, joined.text)

        participants = self.http.get(
            f"{self.api}/api/rooms/{room_id}/participants",
            headers=_bearer(self.teacher_token),
        )
        ok = participants.status_code == 200 and any(
            p.get("student_id") == self.student_id for p in participants.json()
        )
        check("participants list contains student", ok, participants.text)

        started = self.http.post(
            f"{self.api}/api/rooms/{room_id}/start",
            headers=_bearer(self.teacher_token),
        )
        ok = (
            started.status_code == 200
            and started.json().get("status") == "live"
            and started.json().get("current_student_id") == self.student_id
            and started.json().get("question_id")
        )
        check("start session assigns turn + question", ok, started.text)

        turn = self.http.get(
            f"{self.api}/api/rooms/{room_id}/turn", headers=_bearer(self.student_token)
        )
        check("student sees current question", turn.status_code == 200 and turn.json().get("question") is not None, turn.text)

        question_id = started.json().get("question_id")
        audio_url = self.upload_audio()
        transcript = (
            "I work as a software engineer. In my free time I enjoy reading and "
            "travelling. I like meeting new people and learning about different cultures."
        )
        answer = self.http.post(
            f"{self.api}/api/rooms/{room_id}/answers",
            headers=_bearer(self.student_token),
            json={
                "room_id": room_id,
                "question_id": question_id,
                "audio_url": audio_url,
                "transcript": transcript,
            },
        )
        ok = answer.status_code == 200 and answer.json().get("overall_band") is not None
        check("submit answer -> evaluation (Gemini)", ok, answer.text)

        report = self.http.get(
            f"{self.api}/api/students/me/report", headers=_bearer(self.student_token)
        )
        check("student progress report", report.status_code == 200, report.text)

        class_report = self.http.get(
            f"{self.api}/api/rooms/{room_id}/report", headers=_bearer(self.teacher_token)
        )
        check("teacher class report", class_report.status_code == 200, class_report.text)

        final_turn = self.http.get(
            f"{self.api}/api/rooms/{room_id}/turn", headers=_bearer(self.teacher_token)
        )
        check("room auto-ends after student completes", final_turn.status_code == 200 and final_turn.json().get("status") == "ended", final_turn.text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the end-to-end classroom flow test.")
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
