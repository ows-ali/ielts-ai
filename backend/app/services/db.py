from typing import Any

from app.core.security import CurrentUser
from app.services.check import ensure_backend_ready
from app.services.supabase_client import get_supabase_client


async def _client():
    client = await get_supabase_client()
    ensure_backend_ready(client, "Supabase")
    return client


async def upsert_user(user: CurrentUser) -> dict:
    payload = {
        "id": user.id,
        "email": user.email,
        "name": user.name or user.email,
        "role": user.role,
    }
    client = await _client()
    data = (
        await client.table("users")
        .upsert(payload, on_conflict="id")
        .execute()
    )
    return data.data[0]


async def get_user(user_id: str) -> dict | None:
    client = await _client()
    data = (
        await client.table("users").select("*").eq("id", user_id).maybe_single().execute()
    )
    return data.data if data else None


async def create_room(room: dict) -> dict:
    client = await _client()
    data = await client.table("rooms").insert(room).execute()
    return data.data[0]


async def get_room_by_code(room_code: str) -> dict | None:
    client = await _client()
    data = (
        await client.table("rooms")
        .select("*")
        .eq("room_code", room_code)
        .maybe_single()
        .execute()
    )
    return data.data if data else None


async def get_room(room_id: str) -> dict | None:
    client = await _client()
    data = (
        await client.table("rooms").select("*").eq("id", room_id).maybe_single().execute()
    )
    return data.data if data else None


async def update_room(room_id: str, payload: dict) -> dict:
    client = await _client()
    data = (
        await client.table("rooms")
        .update(payload)
        .eq("id", room_id)
        .execute()
    )
    return data.data[0]


async def list_rooms_for_teacher(teacher_id: str) -> list[dict]:
    client = await _client()
    data = (
        await client.table("rooms")
        .select("*")
        .eq("teacher_id", teacher_id)
        .order("created_at", desc=True)
        .execute()
    )
    return data.data


async def add_participant(payload: dict) -> dict:
    client = await _client()
    data = await client.table("participants").insert(payload).execute()
    return data.data[0]


async def get_participant(room_id: str, student_id: str) -> dict | None:
    client = await _client()
    data = (
        await client.table("participants")
        .select("*")
        .eq("room_id", room_id)
        .eq("student_id", student_id)
        .maybe_single()
        .execute()
    )
    return data.data if data else None


async def list_participants(room_id: str) -> list[dict]:
    client = await _client()
    data = (
        await client.table("participants")
        .select("*, users(id, name)")
        .eq("room_id", room_id)
        .order("joined_at")
        .execute()
    )
    return data.data


async def update_participant_status(room_id: str, student_id: str, status: str) -> None:
    client = await _client()
    await (
        client.table("participants")
        .update({"status": status})
        .eq("room_id", room_id)
        .eq("student_id", student_id)
        .execute()
    )


async def set_all_participants_status(room_id: str, status: str) -> None:
    """Set all participants in a room to the given status."""
    client = await _client()
    await (
        client.table("participants")
        .update({"status": status})
        .eq("room_id", room_id)
        .execute()
    )


async def count_participants_by_status(room_id: str) -> dict[str, int]:
    """Return a dict like {"waiting": 0, "speaking": 2, "completed": 3}."""
    participants = await list_participants(room_id)
    counts: dict[str, int] = {}
    for p in participants:
        s = p.get("status", "waiting")
        counts[s] = counts.get(s, 0) + 1
    return counts


async def get_question(question_id: str) -> dict | None:
    client = await _client()
    data = (
        await client.table("questions")
        .select("*")
        .eq("id", question_id)
        .maybe_single()
        .execute()
    )
    return data.data if data else None


async def get_next_question(part: int, exclude_ids: list[str]) -> dict | None:
    client = await _client()
    query = client.table("questions").select("*").eq("part", part)
    if exclude_ids:
        query = query.not_.in_("id", exclude_ids)
    data = await query.limit(1).execute()
    rows = data.data or []
    return rows[0] if rows else None


async def get_student_history(student_id: str, limit: int = 5) -> list[dict]:
    """Return the student's previous evaluation feedback (weaknesses)."""
    client = await _client()
    data = (
        await client.table("evaluations")
        .select("feedback, created_at")
        .eq("student_id", student_id)
        .not_.is_("feedback", "null")
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )
    return data.data or []


async def insert_answer(payload: dict) -> dict:
    client = await _client()
    data = await client.table("answers").insert(payload).execute()
    return data.data[0]


async def insert_evaluation(payload: dict) -> dict:
    client = await _client()
    data = await client.table("evaluations").insert(payload).execute()
    return data.data[0]


async def list_evaluations_for_student(student_id: str) -> list[dict]:
    client = await _client()
    data = (
        await client.table("evaluations")
        .select(
            "id, answers(room_id, audio_url, rooms(room_code, title), question_id, questions(question), transcript), "
            "fluency, grammar, vocabulary, pronunciation, overall_band, feedback, created_at"
        )
        .eq("student_id", student_id)
        .order("created_at", desc=True)
        .execute()
    )
    return data.data or []


async def list_evaluations_for_room(room_id: str) -> list[dict]:
    client = await _client()
    data = (
        await client.table("evaluations")
        .select("*, answers!inner(room_id, student_id, audio_url, transcript, question_id, questions(question))")
        .eq("answers.room_id", room_id)
        .execute()
    )
    return data.data or []
