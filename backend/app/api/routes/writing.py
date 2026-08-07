from fastapi import APIRouter, Depends, HTTPException, status

from app.core.security import CurrentUser, get_current_user, require_teacher
from app.schemas.writing import (
    WritingFeedbackCreate,
    WritingFeedbackOut,
    WritingQuestionDetailOut,
    WritingQuestionOut,
    WritingSampleOut,
    WritingSubmissionCreate,
    WritingSubmissionDetailOut,
    WritingSubmissionOut,
)
from app.services import db

router = APIRouter(prefix="/api/writing", tags=["writing"])

TASK1_TYPES = {"line", "bar", "pie", "table", "map", "process", "multi"}
TASK2_TYPES = {
    "opinion",
    "discussion",
    "advantages",
    "problem_solution",
    "positive_negative",
    "double_question",
}
ALL_TYPES = TASK1_TYPES | TASK2_TYPES


def _parse_feedback(row: dict, submission_id: str | None = None) -> dict:
    """Normalise a writing_feedback row (possibly nested) into a feedback dict."""
    teacher = row.get("users") or {}
    return {
        "id": row["id"],
        "submission_id": row.get("submission_id") or submission_id,
        "teacher_id": row.get("teacher_id"),
        "teacher_name": teacher.get("name") if isinstance(teacher, dict) else None,
        "task_achievement": row.get("task_achievement"),
        "coherence_cohesion": row.get("coherence_cohesion"),
        "lexical_resource": row.get("lexical_resource"),
        "grammatical_range": row.get("grammatical_range"),
        "overall_band": float(row.get("overall_band") or 0),
        "overall_comment": row.get("overall_comment"),
        "created_at": row.get("created_at"),
    }


def _question_out(row: dict) -> WritingQuestionOut:
    return WritingQuestionOut(
        id=row["id"],
        type=row["type"],
        title=row["title"],
        prompt=row["prompt"],
        data_description=row.get("data_description"),
        image_url=row.get("image_url"),
        difficulty=row.get("difficulty"),
        part=row.get("part") or 1,
    )


@router.get("/questions", response_model=list[WritingQuestionOut])
async def list_questions(
    type: str | None = None,
    difficulty: str | None = None,
    part: int = 1,
    user: CurrentUser = Depends(get_current_user),
) -> list[WritingQuestionOut]:
    allowed_types = TASK1_TYPES if part == 1 else TASK2_TYPES if part == 2 else ALL_TYPES
    rows = await db.list_writing_questions(
        question_type=type if type in allowed_types else None,
        difficulty=difficulty if difficulty in {"easy", "medium", "hard"} else None,
        part=part if part in (1, 2) else None,
    )
    return [_question_out(r) for r in rows]


@router.get("/questions/{question_id}", response_model=WritingQuestionDetailOut)
async def get_question(
    question_id: str, user: CurrentUser = Depends(get_current_user)
) -> WritingQuestionDetailOut:
    question = await db.get_writing_question(question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    samples = await db.list_writing_samples(question_id)
    return WritingQuestionDetailOut(
        **WritingQuestionOut(**question).model_dump(),
        samples=[WritingSampleOut(**s) for s in samples],
    )


@router.get("/questions/{question_id}/samples", response_model=list[WritingSampleOut])
async def list_samples(
    question_id: str, user: CurrentUser = Depends(get_current_user)
) -> list[WritingSampleOut]:
    question = await db.get_writing_question(question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    samples = await db.list_writing_samples(question_id)
    return [WritingSampleOut(**s) for s in samples]


@router.post(
    "/submissions",
    response_model=WritingSubmissionOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_submission(
    body: WritingSubmissionCreate,
    user: CurrentUser = Depends(get_current_user),
) -> WritingSubmissionOut:
    if len(body.answer_text.strip()) < 20:
        raise HTTPException(
            status_code=422, detail="Answer is too short to submit (min 20 characters)."
        )
    question = await db.get_writing_question(body.question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    part = body.part or question.get("part") or 1
    submission = await db.insert_writing_submission(
        {
            "student_id": user.id,
            "question_id": body.question_id,
            "answer_text": body.answer_text,
            "part": part,
        }
    )
    return WritingSubmissionOut(
        id=submission["id"],
        question_id=submission["question_id"],
        question_title=question["title"],
        question_type=question["type"],
        part=part,
        answer_text=submission["answer_text"],
        word_count=submission.get("word_count"),
        created_at=submission.get("created_at"),
        feedback=[],
        overall_band=None,
    )


@router.get("/submissions/me", response_model=list[WritingSubmissionOut])
async def my_submissions(
    part: int = 1,
    user: CurrentUser = Depends(get_current_user),
) -> list[WritingSubmissionOut]:
    rows = await db.list_writing_submissions_for_student(
        user.id, part=part if part in (1, 2) else None
    )
    out: list[WritingSubmissionOut] = []
    for r in rows:
        question = r.get("writing_questions") or {}
        feedback_rows = r.get("writing_feedback") or []
        feedback = [_parse_feedback(f, r["id"]) for f in feedback_rows]
        bands = [f["overall_band"] for f in feedback if f["overall_band"]]
        overall = round(sum(bands) / len(bands), 1) if bands else None
        out.append(
            WritingSubmissionOut(
                id=r["id"],
                question_id=r["question_id"],
                question_title=question.get("title") if isinstance(question, dict) else None,
                question_type=question.get("type") if isinstance(question, dict) else None,
                part=r.get("part") or 1,
                answer_text=r["answer_text"],
                word_count=r.get("word_count"),
                created_at=r.get("created_at"),
                feedback=feedback,
                overall_band=overall,
            )
        )
    return out


@router.get("/submissions", response_model=list[WritingSubmissionOut])
async def all_submissions(
    part: int = 1,
    user: CurrentUser = Depends(require_teacher),
) -> list[WritingSubmissionOut]:
    rows = await db.list_all_writing_submissions(
        part=part if part in (1, 2) else None
    )
    out: list[WritingSubmissionOut] = []
    for r in rows:
        student = r.get("users") or {}
        question = r.get("writing_questions") or {}
        feedback_rows = r.get("writing_feedback") or []
        feedback = [_parse_feedback(f, r["id"]) for f in feedback_rows]
        bands = [f["overall_band"] for f in feedback if f["overall_band"]]
        overall = round(sum(bands) / len(bands), 1) if bands else None
        out.append(
            WritingSubmissionOut(
                id=r["id"],
                question_id=r["question_id"],
                question_title=question.get("title") if isinstance(question, dict) else None,
                question_type=question.get("type") if isinstance(question, dict) else None,
                part=r.get("part") or 1,
                answer_text=r["answer_text"],
                word_count=r.get("word_count"),
                created_at=r.get("created_at"),
                feedback=feedback,
                overall_band=overall,
            )
        )
    return out


@router.get("/submissions/{submission_id}", response_model=WritingSubmissionDetailOut)
async def get_submission(
    submission_id: str, user: CurrentUser = Depends(get_current_user)
) -> WritingSubmissionDetailOut:
    submission = await db.get_writing_submission(submission_id)
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")
    is_owner = submission["student_id"] == user.id
    is_teacher = user.role == "teacher"
    if not is_owner and not is_teacher:
        raise HTTPException(status_code=403, detail="Not authorized to view this submission")

    question = submission.get("writing_questions") or {}
    feedback_rows = submission.get("writing_feedback") or []
    feedback = [_parse_feedback(f, submission["id"]) for f in feedback_rows]
    bands = [f["overall_band"] for f in feedback if f["overall_band"]]
    overall = round(sum(bands) / len(bands), 1) if bands else None

    return WritingSubmissionDetailOut(
        id=submission["id"],
        question_id=submission["question_id"],
        question_title=question.get("title") if isinstance(question, dict) else None,
        question_type=question.get("type") if isinstance(question, dict) else None,
        part=submission.get("part") or 1,
        question_prompt=question.get("prompt") if isinstance(question, dict) else None,
        question_data=question.get("data_description") if isinstance(question, dict) else None,
        question_image_url=question.get("image_url") if isinstance(question, dict) else None,
        question_difficulty=question.get("difficulty") if isinstance(question, dict) else None,
        answer_text=submission["answer_text"],
        word_count=submission.get("word_count"),
        created_at=submission.get("created_at"),
        feedback=feedback,
        overall_band=overall,
    )


@router.post("/feedback", response_model=WritingFeedbackOut)
async def create_feedback(
    body: WritingFeedbackCreate,
    user: CurrentUser = Depends(require_teacher),
) -> WritingFeedbackOut:
    for val in (
        body.task_achievement,
        body.coherence_cohesion,
        body.lexical_resource,
        body.grammatical_range,
    ):
        if val < 4 or val > 9:
            raise HTTPException(
                status_code=422, detail="Each criterion score must be between 4 and 9."
            )
    submission = await db.get_writing_submission(body.submission_id)
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")
    row = await db.insert_writing_feedback(
        {
            "submission_id": body.submission_id,
            "teacher_id": user.id,
            "task_achievement": body.task_achievement,
            "coherence_cohesion": body.coherence_cohesion,
            "lexical_resource": body.lexical_resource,
            "grammatical_range": body.grammatical_range,
            "overall_comment": body.overall_comment,
        }
    )
    parsed = _parse_feedback({**row, "users": {"name": user.name}})
    return WritingFeedbackOut(**parsed)


@router.delete("/feedback/{feedback_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_feedback(
    feedback_id: str, user: CurrentUser = Depends(require_teacher)
) -> None:
    await db.delete_writing_feedback(feedback_id)
