from fastapi import APIRouter, Depends, HTTPException

from app.core.security import CurrentUser, get_current_user
from app.schemas.badges import (
    BadgeOut,
    BadgeSummaryOut,
    CommunityOut,
    ProfileStatsOut,
    PublicProfileOut,
)
from app.services import badges as badges_svc
from app.services import community as community_svc
from app.services import db

router = APIRouter(prefix="/api", tags=["profiles"])


async def _build_badge_summary(user_id: str) -> BadgeSummaryOut:
    evals = await db.get_student_evaluations(user_id)
    parts = await db.get_student_speaking_parts(user_id)
    subs, feedback = await db.get_student_writing_progress(user_id)
    badges = badges_svc.compute_badges(evals, parts, subs, feedback)
    stats = badges_svc.compute_stats(evals, parts, subs, feedback)
    return BadgeSummaryOut(
        user_id=user_id,
        earned_count=sum(1 for b in badges if b["earned"]),
        total_count=len(badges),
        badges=[BadgeOut(**b) for b in badges],
        stats=ProfileStatsOut(**stats),
    )


@router.get("/me/badges", response_model=BadgeSummaryOut)
async def my_badges(
    user: CurrentUser = Depends(get_current_user),
) -> BadgeSummaryOut:
    return await _build_badge_summary(user.id)


@router.get("/users/{user_id}/profile", response_model=PublicProfileOut)
async def public_profile(user_id: str) -> PublicProfileOut:
    """Public profile. No auth required — returns only public-safe data
    (name, role, joined date, earned badges and aggregate stats)."""
    public_user = await db.get_public_user(user_id)
    if not public_user:
        raise HTTPException(status_code=404, detail="User not found")
    summary = await _build_badge_summary(user_id)
    earned = [b for b in summary.badges if b.earned]
    return PublicProfileOut(
        id=public_user["id"],
        name=public_user.get("name") or "Student",
        role=public_user.get("role") or "student",
        created_at=str(public_user["created_at"]) if public_user.get("created_at") else None,
        earned_count=summary.earned_count,
        total_count=summary.total_count,
        badges=earned,
        stats=summary.stats,
    )


@router.get("/community", response_model=CommunityOut)
async def community() -> CommunityOut:
    """Public community leaderboards + activity feed. No auth required."""
    students = await db.list_students()
    evals = await db.list_all_evaluations_brief()
    subs = await db.list_all_writing_submissions_brief()
    feedback = await db.list_all_writing_feedback_brief()
    answers = await db.list_all_answers_brief()
    data = community_svc.build_community(students, evals, subs, feedback, answers)
    return CommunityOut(**data)
