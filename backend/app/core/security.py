import httpx
from fastapi import Depends, HTTPException, Request, status
from pydantic import BaseModel

from app.core.config import settings


class CurrentUser(BaseModel):
    id: str
    email: str | None = None
    name: str | None = None
    role: str = "student"
    raw: dict


async def _verify_token_with_auth_server(token: str) -> dict:
    """Validate the access token against the Supabase Auth server.

    Works with both legacy HS256 and the new asymmetric JWT signing keys.
    """
    if not settings.supabase_url or not settings.supabase_anon_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Supabase is not configured on this server.",
        )
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(
            f"{settings.supabase_url.rstrip('/')}/auth/v1/user",
            headers={
                "apikey": settings.supabase_anon_key,
                "Authorization": f"Bearer {token}",
            },
        )
    if resp.status_code == 200:
        return resp.json()
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
        headers={"WWW-Authenticate": "Bearer"},
    )


async def get_current_user(request: Request) -> CurrentUser:
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing bearer token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    data = await _verify_token_with_auth_server(auth.removeprefix("Bearer ").strip())

    user_metadata = data.get("user_metadata") or {}
    app_metadata = data.get("app_metadata") or {}
    role = user_metadata.get("role") or app_metadata.get("role") or "student"

    return CurrentUser(
        id=data["id"],
        email=data.get("email"),
        name=user_metadata.get("name") or data.get("email"),
        role=role,
        raw=data,
    )


def require_teacher(user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
    if user.role != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Teacher access required"
        )
    return user
