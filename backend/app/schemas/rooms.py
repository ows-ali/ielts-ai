from datetime import datetime

from pydantic import BaseModel

from app.schemas.speaking import QuestionOut


class RoomCreate(BaseModel):
    title: str
    part: int = 1


class RoomOut(BaseModel):
    id: str
    room_code: str
    title: str
    part: int
    teacher_id: str
    status: str
    created_at: str | datetime | None = None


class JoinRoomRequest(BaseModel):
    room_code: str


class ParticipantOut(BaseModel):
    id: str
    room_id: str
    student_id: str
    student_name: str | None = None
    status: str
    joined_at: str | datetime | None = None


class RoomStatusUpdate(BaseModel):
    status: str


class TurnState(BaseModel):
    room_id: str
    current_student_id: str | None = None
    current_student_name: str | None = None
    question_id: str | None = None
    question: QuestionOut | None = None
    status: str
