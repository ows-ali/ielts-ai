from datetime import datetime
from typing import Any

from pydantic import BaseModel


class WritingQuestionOut(BaseModel):
    id: str
    type: str
    title: str
    prompt: str
    data_description: dict[str, Any] | None = None
    image_url: str | None = None
    difficulty: str | None = None
    part: int = 1


class WritingSampleOut(BaseModel):
    id: str
    band: int
    answer_text: str
    task_achievement: int
    coherence_cohesion: int
    lexical_resource: int
    grammatical_range: int
    explanation: str
    improvement_tips: list[str]


class WritingQuestionDetailOut(WritingQuestionOut):
    samples: list[WritingSampleOut]


class WritingSubmissionCreate(BaseModel):
    question_id: str
    answer_text: str
    part: int | None = None


class WritingFeedbackOut(BaseModel):
    id: str
    submission_id: str
    teacher_id: str
    teacher_name: str | None = None
    task_achievement: int
    coherence_cohesion: int
    lexical_resource: int
    grammatical_range: int
    overall_band: float
    overall_comment: str | None = None
    created_at: str | datetime | None = None


class WritingSubmissionOut(BaseModel):
    id: str
    question_id: str
    question_title: str | None = None
    question_type: str | None = None
    part: int = 1
    answer_text: str
    word_count: int | None = None
    created_at: str | datetime | None = None
    feedback: list[WritingFeedbackOut] = []
    overall_band: float | None = None


class WritingSubmissionDetailOut(WritingSubmissionOut):
    question_prompt: str | None = None
    question_data: dict[str, Any] | None = None
    question_image_url: str | None = None
    question_difficulty: str | None = None


class WritingFeedbackCreate(BaseModel):
    submission_id: str
    task_achievement: int
    coherence_cohesion: int
    lexical_resource: int
    grammatical_range: int
    overall_comment: str | None = None
