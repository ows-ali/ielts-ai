"""Multi-user verification script (1 Teacher, 2 Students) testing room creation,
both students joining, turn progression, audio submission, class reports with audio URLs,
and student privacy filtering.
"""

import io
import os
import uuid
import wave

import httpx
from dotenv import load_dotenv

load_dotenv()

API = "http://localhost:8000"
SUPABASE_URL = os.getenv("SUPABASE_URL", "").rstrip("/")
ANON_KEY = os.getenv("SUPABASE_ANON_KEY", "")
PASSWORD = "DummyPass123!"
TEACHER_PASSWORD = "TeacherSecure#2026"

TEACHER_EMAIL = "teacher1@example.com"
STUDENT1_EMAIL = "student1@example.com"
STUDENT2_EMAIL = "student2@example.com"


def login(http: httpx.Client, email: str, password: str = PASSWORD) -> str:
    headers = {"apikey": ANON_KEY, "Content-Type": "application/json"}
    resp = http.post(
        f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
        headers=headers,
        json={"email": email, "password": password},
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def bearer(token: str) -> dict:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def make_wav_bytes() -> bytes:
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(8000)
        w.writeframes(b"\x00\x00" * 4000)
    return buf.getvalue()


def run():
    print("=== Multi-User E2E Verification (1 Teacher, 2 Students) ===")
    with httpx.Client(timeout=120.0) as http:
        print("[1] Logging in test accounts...")
        teacher_token = login(http, TEACHER_EMAIL, TEACHER_PASSWORD)
        student1_token = login(http, STUDENT1_EMAIL)
        student2_token = login(http, STUDENT2_EMAIL)

        # Get user info
        t_user = http.get(f"{API}/api/auth/me", headers=bearer(teacher_token)).json()
        s1_user = http.get(f"{API}/api/auth/me", headers=bearer(student1_token)).json()
        s2_user = http.get(f"{API}/api/auth/me", headers=bearer(student2_token)).json()

        print(f"    Teacher: {t_user['name']} ({t_user['id']})")
        print(f"    Student 1: {s1_user['name']} ({s1_user['id']})")
        print(f"    Student 2: {s2_user['name']} ({s2_user['id']})")

        # 2. Teacher creates room
        print("[2] Teacher creating room...")
        r_resp = http.post(
            f"{API}/api/rooms",
            headers=bearer(teacher_token),
            json={"title": "E2E Multi-User Room", "part": 1},
        )
        r_resp.raise_for_status()
        room = r_resp.json()
        room_id = room["id"]
        code = room["room_code"]
        print(f"    Room Created: Code={code}, ID={room_id}")

        # 3. Student 1 and Student 2 join
        print("[3] Students joining room...")
        http.post(f"{API}/api/rooms/join", headers=bearer(student1_token), json={"room_code": code}).raise_for_status()
        http.post(f"{API}/api/rooms/join", headers=bearer(student2_token), json={"room_code": code}).raise_for_status()

        # 4. Check participants list
        pts = http.get(f"{API}/api/rooms/{room_id}/participants", headers=bearer(teacher_token)).json()
        print(f"    Participants count: {len(pts)}")
        assert len(pts) >= 2, "Expected at least 2 participants"

        # 5. Teacher starts session
        print("[4] Teacher starting session...")
        turn1 = http.post(f"{API}/api/rooms/{room_id}/start", headers=bearer(teacher_token)).json()
        print(f"    Turn 1 Active Student: {turn1['current_student_name']}")

        # 6. Active student 1 submits answer
        active1_token = student1_token if turn1["current_student_id"] == s1_user["id"] else student2_token
        active1_id = turn1["current_student_id"]
        
        # Audio upload to storage bucket
        wav = make_wav_bytes()
        up_url = f"{SUPABASE_URL}/storage/v1/object/audio/{room_id}/{active1_id}/{uuid.uuid4().hex}.wav"
        http.post(
            up_url,
            headers={"Authorization": f"Bearer {active1_token}", "Content-Type": "audio/wav"},
            content=wav,
        )
        
        print("[5] Submitting answer for turn 1...")
        eval1 = http.post(
            f"{API}/api/rooms/{room_id}/answers",
            headers=bearer(active1_token),
            json={
                "room_id": room_id,
                "question_id": turn1["question_id"],
                "audio_url": up_url,
                "transcript": "I am working as a software developer and I love solving problems.",
            },
        ).json()
        band1 = eval1.get("overall_band", eval1.get("overall"))
        print(f"    Student 1 Band Score: {band1}")

        # 7. Turn 2 for Student 2
        turn2 = http.get(f"{API}/api/rooms/{room_id}/turn", headers=bearer(teacher_token)).json()
        print(f"    Turn 2 Active Student: {turn2['current_student_name']}")
        
        if turn2["current_student_id"]:
            active2_token = student1_token if turn2["current_student_id"] == s1_user["id"] else student2_token
            up_url2 = f"{SUPABASE_URL}/storage/v1/object/audio/{room_id}/{turn2['current_student_id']}/{uuid.uuid4().hex}.wav"
            http.post(
                up_url2,
                headers={"Authorization": f"Bearer {active2_token}", "Content-Type": "audio/wav"},
                content=wav,
            )
            eval2 = http.post(
                f"{API}/api/rooms/{room_id}/answers",
                headers=bearer(active2_token),
                json={
                    "room_id": room_id,
                    "question_id": turn2["question_id"],
                    "audio_url": up_url2,
                    "transcript": "My favourite hobby is playing music and traveling around the world.",
                },
            ).json()
            band2 = eval2.get("overall_band", eval2.get("overall"))
            print(f"    Student 2 Band Score: {band2}")

        # 8. Teacher Report Verification (Audio URLs + Transcripts)
        print("[6] Verifying Teacher Class Report (Audio Playback & Details)...")
        teacher_report = http.get(f"{API}/api/rooms/{room_id}/report", headers=bearer(teacher_token)).json()
        print(f"    Class Average Band: {teacher_report['average_band']}")
        for p in teacher_report["participants"]:
            print(f"    -> Participant {p['student_name']}: Band {p['band']}, Audio URL: {p['audio_url']}")
            assert p["audio_url"] is not None, f"Expected audio_url for {p['student_name']} in teacher report"
            assert p["transcript"] is not None, f"Expected transcript for {p['student_name']} in teacher report"

        # 9. Student Report Privacy Verification
        print("[7] Verifying Student 1 Class Report Privacy...")
        s1_report = http.get(f"{API}/api/rooms/{room_id}/report", headers=bearer(student1_token)).json()
        for p in s1_report["participants"]:
            if p["student_id"] == s1_user["id"]:
                print(f"    -> Student 1 own entry: Audio URL present = {p['audio_url'] is not None}")
                assert p["audio_url"] is not None, "Student 1 should see their own audio URL"
            else:
                print(f"    -> Classmate entry ({p['student_name']}): Band={p['band']}, Audio URL sanitized = {p['audio_url'] is None}")
                assert p["audio_url"] is None, "Student 1 MUST NOT see classmate audio URL"
                assert p["transcript"] is None, "Student 1 MUST NOT see classmate transcript"

        print("\n🎉 MULTI-USER E2E VERIFICATION PASSED SUCCESSFULLY!")


if __name__ == "__main__":
    run()
