from pydantic import BaseModel


class QuestionOut(BaseModel):
    id: str
    part: int
    topic: str | None = None
    question: str
    difficulty: str | None = None


class AnswerSubmit(BaseModel):
    room_id: str
    question_id: str
    audio_url: str
    transcript: str | None = None


class FeedbackItem(BaseModel):
    item: str


class EvaluationOut(BaseModel):
    id: str
    answer_id: str
    fluency: float
    grammar: float
    vocabulary: float
    pronunciation: float
    overall_band: float
    feedback: list[str]
