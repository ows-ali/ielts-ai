from pydantic import BaseModel


class StudentAttempt(BaseModel):
    id: str
    room_code: str | None = None
    title: str | None = None
    question: str
    audio_url: str | None = None
    transcript: str | None = None
    fluency: float | None = None
    grammar: float | None = None
    vocabulary: float | None = None
    pronunciation: float | None = None
    overall_band: float | None = None
    feedback: list[str] | None = None
    created_at: str | None = None


class StudentReportOut(BaseModel):
    student_id: str
    attempts: list[StudentAttempt]


class ParticipantScore(BaseModel):
    student_id: str
    student_name: str
    status: str
    band: float | None = None


class ClassReportOut(BaseModel):
    room_id: str
    room_code: str
    participants: list[ParticipantScore]
    average_band: float | None = None
    common_problems: list[str]
