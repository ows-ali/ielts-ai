import secrets

from fastapi import APIRouter, Depends, HTTPException, status

from app.core.security import CurrentUser, get_current_user, require_teacher
from app.schemas.rooms import (
    JoinRoomRequest,
    ParticipantOut,
    RoomCreate,
    RoomOut,
    RoomStatusUpdate,
    TurnState,
)
from app.services import db

router = APIRouter(prefix="/api/rooms", tags=["rooms"])


def _generate_room_code() -> str:
    alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return "".join(secrets.choice(alphabet) for _ in range(6))


@router.post("", response_model=RoomOut, status_code=status.HTTP_201_CREATED)
async def create_room(
    body: RoomCreate, user: CurrentUser = Depends(require_teacher)
) -> RoomOut:
    room = await db.create_room(
        {
            "title": body.title,
            "part": body.part,
            "room_code": _generate_room_code(),
            "teacher_id": user.id,
            "status": "waiting",
        }
    )
    return RoomOut(**room)


@router.get("", response_model=list[RoomOut])
async def list_rooms(user: CurrentUser = Depends(require_teacher)) -> list[RoomOut]:
    rooms = await db.list_rooms_for_teacher(user.id)
    return [RoomOut(**r) for r in rooms]


@router.get("/{room_id}", response_model=RoomOut)
async def get_room(
    room_id: str, user: CurrentUser = Depends(get_current_user)
) -> RoomOut:
    room = await db.get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return RoomOut(**room)


@router.post("/join", response_model=RoomOut)
async def join_room(
    body: JoinRoomRequest, user: CurrentUser = Depends(get_current_user)
) -> RoomOut:
    room = await db.get_room_by_code(body.room_code.strip().upper())
    if not room:
        raise HTTPException(status_code=404, detail="Invalid room code")
    if room["status"] != "waiting":
        raise HTTPException(
            status_code=409, detail="Room is no longer accepting participants"
        )
    existing = await db.get_participant(room["id"], user.id)
    if not existing:
        await db.add_participant(
            {
                "room_id": room["id"],
                "student_id": user.id,
                "status": "waiting",
            }
        )
    return RoomOut(**room)


@router.get("/{room_id}/participants", response_model=list[ParticipantOut])
async def participants(
    room_id: str, user: CurrentUser = Depends(get_current_user)
) -> list[ParticipantOut]:
    rows = await db.list_participants(room_id)
    out = []
    for r in rows:
        student = r.get("users") or {}
        out.append(
            ParticipantOut(
                id=r["id"],
                room_id=r["room_id"],
                student_id=r["student_id"],
                student_name=student.get("name") if isinstance(student, dict) else None,
                status=r["status"],
                joined_at=r.get("joined_at"),
            )
        )
    return out


@router.post("/{room_id}/status", response_model=RoomOut)
async def update_room_status(
    room_id: str,
    body: RoomStatusUpdate,
    user: CurrentUser = Depends(require_teacher),
) -> RoomOut:
    room = await db.get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    if room["teacher_id"] != user.id:
        raise HTTPException(status_code=403, detail="Not your room")
    if body.status not in {"waiting", "live", "ended"}:
        raise HTTPException(status_code=422, detail="Invalid status")
    updated = await db.update_room(room_id, {"status": body.status})
    return RoomOut(**updated)

@router.get("/{room_id}/turn", response_model=TurnState)
async def current_turn(
    room_id: str, user: CurrentUser = Depends(get_current_user)
) -> TurnState:
    room = await db.get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    question = (
        await db.get_question(room["current_question_id"])
        if room.get("current_question_id")
        else None
    )

    # In async mode, every student is "current" — return the calling user's own ID
    # so the frontend shows the recording UI to everyone simultaneously.
    participant = await db.get_participant(room_id, user.id)
    is_participant = participant is not None
    student_name = user.name if is_participant else None

    return TurnState(
        room_id=room_id,
        current_student_id=user.id if (is_participant and room["status"] == "live") else None,
        current_student_name=student_name if (is_participant and room["status"] == "live") else None,
        question_id=room.get("current_question_id"),
        question=question,
        status=room["status"],
    )


@router.post("/{room_id}/start", response_model=TurnState)
async def start_session(
    room_id: str, user: CurrentUser = Depends(require_teacher)
) -> TurnState:
    room = await db.get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    if room["teacher_id"] != user.id:
        raise HTTPException(status_code=403, detail="Not your room")

    participants = await db.list_participants(room_id)
    if not participants:
        raise HTTPException(status_code=400, detail="No students have joined yet")

    # Pick one question for the whole room
    question = await db.get_next_question(room["part"], [])

    # Set ALL participants to "speaking" simultaneously
    await db.set_all_participants_status(room_id, "speaking")

    # Update room to live with the shared question
    await db.update_room(
        room_id,
        {
            "current_student_id": None,  # No single student — all are speaking
            "current_question_id": question["id"] if question else None,
            "status": "live",
        },
    )

    return await current_turn(room_id, user)


@router.post("/{room_id}/end", response_model=RoomOut)
async def end_session(
    room_id: str, user: CurrentUser = Depends(require_teacher)
) -> RoomOut:
    room = await db.get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    if room["teacher_id"] != user.id:
        raise HTTPException(status_code=403, detail="Not your room")
    updated = await db.update_room(
        room_id, {"status": "ended", "current_student_id": None}
    )
    return RoomOut(**updated)
