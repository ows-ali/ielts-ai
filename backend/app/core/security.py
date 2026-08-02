from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt
from pydantic import BaseModel

from app.core.config import settings


class CurrentUser(BaseModel):
    id: str
    email: str | None = None
    name: str | None = None
    role: str = "student"
    raw: dict


def _decode_token(token: str) -> dict:
    if not settings.supabase_jwt_secret:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Supabase JWT secret is not configured on the server.",
        )
    try:
        return jwt.decode(token, settings.supabase_jwt_secret, algorithms=["HS256"])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )


def get_current_user(request: Request) -> CurrentUser:
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing bearer token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    payload = _decode_token(auth.removeprefix("Bearer ").strip())

    if not payload.get("sub"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user_metadata = payload.get("user_metadata") or {}
    app_metadata = payload.get("app_metadata") or {}
    role = user_metadata.get("role") or app_metadata.get("role") or "student"

    return CurrentUser(
        id=payload["sub"],
        email=payload.get("email"),
        name=user_metadata.get("name") or payload.get("email"),
        role=role,
        raw=payload,
    )


def require_teacher(user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
    if user.role != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Teacher access required"
        )
    return user
