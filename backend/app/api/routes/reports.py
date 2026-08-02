from fastapi import APIRouter, Depends, HTTPException

from app.core.security import CurrentUser, get_current_user, require_teacher
from app.schemas.reports import (
    ClassReportOut,
    ParticipantScore,
    RoomScoresOut,
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
                room_id=answer.get("room_id"),
                room_code=room.get("room_code"),
                title=room.get("title"),
                question=question.get("question") or "",
                audio_url=answer.get("audio_url"),
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
    room_id: str, user: CurrentUser = Depends(get_current_user)
) -> ClassReportOut:
    room = await db.get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    participants = await db.list_participants(room_id)
    is_teacher = (room["teacher_id"] == user.id)
    is_participant = any(p["student_id"] == user.id for p in participants)
    if not is_teacher and not is_participant:
        raise HTTPException(status_code=403, detail="Not authorized to view this room report")

    evals = await db.list_evaluations_for_room(room_id)
    eval_by_student: dict[str, dict] = {}
    for e in evals:
        student_id = e.get("student_id") or (e.get("answers") or {}).get("student_id")
        if student_id and student_id not in eval_by_student:
            eval_by_student[student_id] = e

    scores: list[ParticipantScore] = []
    for p in participants:
        student = p.get("users") or {}
        e = eval_by_student.get(p["student_id"])
        answer = (e.get("answers") or {}) if e else {}
        q_obj = (answer.get("questions") or {}) if isinstance(answer, dict) else {}
        
        # Audio, transcript, sub-scores, and feedback are only visible to the teacher or the student themselves
        show_private = is_teacher or (p["student_id"] == user.id)
        
        scores.append(
            ParticipantScore(
                student_id=p["student_id"],
                student_name=student.get("name") if isinstance(student, dict) else None,
                status=p["status"],
                band=e.get("overall_band") if e else None,
                audio_url=answer.get("audio_url") if (e and show_private) else None,
                transcript=answer.get("transcript") if (e and show_private) else None,
                question=q_obj.get("question") if (e and show_private) else None,
                fluency=e.get("fluency") if (e and show_private) else None,
                grammar=e.get("grammar") if (e and show_private) else None,
                vocabulary=e.get("vocabulary") if (e and show_private) else None,
                pronunciation=e.get("pronunciation") if (e and show_private) else None,
                feedback=e.get("feedback") if (e and show_private) else None,
            )
        )

    bands = [s.band for s in scores if s.band is not None]
    average = round(sum(bands) / len(bands), 1) if bands else None

    common_problems: list[str] = []
    if evals:
        ensure_backend_ready(await get_supabase_client(), "Supabase")
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


@router.get("/rooms/{room_id}/scores", response_model=RoomScoresOut)
async def room_scores(
    room_id: str, user: CurrentUser = Depends(get_current_user)
) -> RoomScoresOut:
    room = await db.get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    participants = await db.list_participants(room_id)
    is_participant = any(p["student_id"] == user.id for p in participants)
    if not is_participant:
        raise HTTPException(status_code=403, detail="Not authorized to view this room scores")
    
    evals = await db.list_evaluations_for_room(room_id)
    eval_by_student: dict[str, dict] = {}
    for e in evals:
        student_id = e.get("student_id") or (e.get("answers") or {}).get("student_id")
        if student_id and student_id not in eval_by_student:
            eval_by_student[student_id] = e

    scores: list[ParticipantScore] = []
    for p in participants:
        student = p.get("users") or {}
        e = eval_by_student.get(p["student_id"])
        # Only show scores (band and sub-scores), no audio/transcript for other students
        scores.append(
            ParticipantScore(
                student_id=p["student_id"],
                student_name=student.get("name") if isinstance(student, dict) else None,
                status=p["status"],
                band=e.get("overall_band") if e else None,
                fluency=e.get("fluency") if e else None,
                grammar=e.get("grammar") if e else None,
                vocabulary=e.get("vocabulary") if e else None,
                pronunciation=e.get("pronunciation") if e else None,
            )
        )

    return RoomScoresOut(
        room_id=room_id,
        room_code=room["room_code"],
        participants=scores,
    )
