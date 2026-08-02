from fastapi import APIRouter, Depends, HTTPException

from app.core.security import CurrentUser, get_current_user, require_teacher
from app.schemas.reports import (
    ClassReportOut,
    ParticipantScore,
    StudentAttempt,
    StudentReportOut,
)
from app.services import db, gemini
from app.services.check import ensure_backend_ready
from app.services.supabase_client import get_supabase_client

router = APIRouter(prefix="/api", tags=["reports"])


@router.get("/students/me/report", response_model=StudentReportOut)
async def student_report(
    user: CurrentUser = Depends(get_current_user),
) -> StudentReportOut:
    rows = await db.list_evaluations_for_student(user.id)
    attempts: list[StudentAttempt] = []
    for r in rows:
        answer = r.get("answers") or {}
        room = answer.get("rooms") or {}
        question = answer.get("questions") or {}
        attempts.append(
            StudentAttempt(
                id=r["id"],
                room_code=room.get("room_code"),
                title=room.get("title"),
                question=question.get("question") or "",
                transcript=answer.get("transcript"),
                fluency=r.get("fluency"),
                grammar=r.get("grammar"),
                vocabulary=r.get("vocabulary"),
                pronunciation=r.get("pronunciation"),
                overall_band=r.get("overall_band"),
                feedback=r.get("feedback"),
                created_at=str(r.get("created_at")) if r.get("created_at") else None,
            )
        )
    return StudentReportOut(student_id=user.id, attempts=attempts)


@router.get("/rooms/{room_id}/report", response_model=ClassReportOut)
async def class_report(
    room_id: str, user: CurrentUser = Depends(require_teacher)
) -> ClassReportOut:
    room = await db.get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    if room["teacher_id"] != user.id:
        raise HTTPException(status_code=403, detail="Not your room")

    participants = await db.list_participants(room_id)
    evals = await db.list_evaluations_for_room(room_id)
    eval_by_student: dict[str, dict] = {}
    for e in evals:
        student_id = (e.get("answers") or {}).get("student_id")
        if student_id and student_id not in eval_by_student:
            eval_by_student[student_id] = e

    scores: list[ParticipantScore] = []
    for p in participants:
        student = p.get("users") or {}
        e = eval_by_student.get(p["student_id"])
        scores.append(
            ParticipantScore(
                student_id=p["student_id"],
                student_name=student.get("name") if isinstance(student, dict) else None,
                status=p["status"],
                band=e.get("overall_band") if e else None,
            )
        )

    bands = [s.band for s in scores if s.band is not None]
    average = round(sum(bands) / len(bands), 1) if bands else None

    common_problems: list[str] = []
    if evals:
        ensure_backend_ready(get_supabase_client(), "Supabase")
        try:
            common_problems = await gemini.summarize_class_problems(evals)
        except Exception:
            common_problems = []

    return ClassReportOut(
        room_id=room_id,
        room_code=room["room_code"],
        participants=scores,
        average_band=average,
        common_problems=common_problems,
    )
