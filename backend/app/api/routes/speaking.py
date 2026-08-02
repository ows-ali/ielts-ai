import mimetypes

import httpx
from fastapi import APIRouter, Depends, HTTPException, status

from app.core.config import settings
from app.core.security import CurrentUser, get_current_user
from app.schemas.speaking import AnswerSubmit, EvaluationOut
from app.services import db, gemini, rag
from app.services.check import ensure_backend_ready
from app.services.supabase_client import get_supabase_client

router = APIRouter(prefix="/api/rooms", tags=["speaking"])


async def _fetch_audio(url: str) -> tuple[bytes, str]:
    async with httpx.AsyncClient(timeout=60, follow_redirects=True) as client:
        resp = await client.get(url)
        if resp.status_code != 200:
            raise HTTPException(
                status_code=400, detail="Could not download the audio file"
            )
        mime = resp.headers.get("content-type") or mimetypes.guess_type(url)[0] or "audio/wav"
        return resp.content, mime


@router.post("/{room_id}/answers", response_model=EvaluationOut)
async def submit_answer(
    room_id: str,
    body: AnswerSubmit,
    user: CurrentUser = Depends(get_current_user),
) -> EvaluationOut:
    room = await db.get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    if room["status"] != "live":
        raise HTTPException(status_code=409, detail="Session is not live")
    if room.get("current_student_id") != user.id:
        raise HTTPException(status_code=403, detail="It is not your turn")

    question = await db.get_question(body.question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    ensure_backend_ready(get_supabase_client(), "Supabase")
    if not settings.gemini_api_key:
        raise HTTPException(
            status_code=503,
            detail="Gemini API is not configured on this server.",
        )

    audio_bytes, mime = await _fetch_audio(body.audio_url)
    transcript = body.transcript or await gemini.transcribe_audio(audio_bytes, mime)
    if not transcript.strip():
        raise HTTPException(
            status_code=422, detail="No speech detected in the audio"
        )

    criteria = await rag.retrieve_ielts_criteria(
        f"IELTS Speaking Part {question['part']} scoring band descriptors"
    )
    history_rows = await db.get_student_history(user.id)
    history = "\n".join(
        "- " + tip
        for row in history_rows
        if isinstance(row.get("feedback"), list)
        for tip in row["feedback"][:3]
    )

    try:
        score = await gemini.evaluate_answer(
            transcript=transcript,
            criteria=criteria,
            part=question["part"],
            question=question["question"],
            history=history,
        )
    except ValueError as exc:
        raise HTTPException(status_code=502, detail=str(exc))

    answer = await db.insert_answer(
        {
            "room_id": room_id,
            "student_id": user.id,
            "question_id": body.question_id,
            "audio_url": body.audio_url,
            "transcript": transcript,
        }
    )
    evaluation = await db.insert_evaluation(
        {
            "answer_id": answer["id"],
            "student_id": user.id,
            "fluency": float(score["fluency"]),
            "grammar": float(score["grammar"]),
            "vocabulary": float(score["vocabulary"]),
            "pronunciation": float(score["pronunciation"]),
            "overall_band": float(score["overall"]),
            "feedback": score["feedback"],
        }
    )

    await db.update_participant_status(room_id, user.id, "completed")
    await _advance_or_end(room_id)

    return EvaluationOut(
        id=evaluation["id"],
        answer_id=answer["id"],
        fluency=evaluation["fluency"],
        grammar=evaluation["grammar"],
        vocabulary=evaluation["vocabulary"],
        pronunciation=evaluation["pronunciation"],
        overall_band=evaluation["overall_band"],
        feedback=evaluation["feedback"],
    )


async def _advance_or_end(room_id: str) -> None:
    from app.api.routes.rooms import _pick_next

    await _pick_next(room_id)
