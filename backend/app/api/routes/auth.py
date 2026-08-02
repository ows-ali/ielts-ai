from fastapi import APIRouter, Depends

from app.core.security import CurrentUser, get_current_user
from app.schemas.auth import UserOut
from app.services import db

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.get("/me", response_model=UserOut)
async def me(user: CurrentUser = Depends(get_current_user)) -> UserOut:
    profile = await db.upsert_user(user)
    return UserOut(
        id=profile["id"],
        email=profile.get("email"),
        name=profile.get("name"),
        role=profile["role"],
    )
