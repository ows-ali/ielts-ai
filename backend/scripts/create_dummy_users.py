"""Create dummy teacher/student accounts for local testing.

Usage:
    python -m scripts.create_dummy_users

Creates 2 teachers and 2 students (counts configurable via --teachers / --students).
Users are created as email-confirmed, so no verification email is required.

Requires SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY in .env.
"""

import argparse
import os

import httpx
from dotenv import load_dotenv

load_dotenv()

DEFAULT_PASSWORD = "DummyPass123!"


def create_users(role: str, count: int, password: str, supabase_url: str, service_key: str) -> None:
    for i in range(1, count + 1):
        email = f"{role}{i}@example.com"
        name = f"Dummy {role.title()} {i}"
        payload = {
            "email": email,
            "password": password,
            "email_confirm": True,
            "user_metadata": {"role": role, "name": name},
        }
        resp = httpx.post(
            f"{supabase_url}/auth/v1/admin/users",
            headers={
                "apikey": service_key,
                "Authorization": f"Bearer {service_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=30,
        )
        if resp.status_code in (409, 422) and "email_exists" in resp.text.lower():
            print(f"[skip]  {email} already exists")
            continue
        if resp.status_code not in (200, 201):
            print(f"[error] {email}: {resp.status_code} {resp.text[:200]}")
            continue
        user_id = resp.json().get("id")
        print(f"[ok]    {email}  id={user_id}  verified=yes")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create dummy teacher/student accounts.")
    parser.add_argument("--teachers", type=int, default=2)
    parser.add_argument("--students", type=int, default=2)
    parser.add_argument("--password", default=DEFAULT_PASSWORD)
    args = parser.parse_args()

    supabase_url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    service_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
    if not supabase_url or not service_key:
        raise SystemExit("SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set in .env")

    create_users("teacher", args.teachers, args.password, supabase_url, service_key)
    create_users("student", args.students, args.password, supabase_url, service_key)
    print(f"\nPassword for all accounts: {args.password}")


if __name__ == "__main__":
    main()
