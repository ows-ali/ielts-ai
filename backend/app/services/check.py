from fastapi import HTTPException

from app.core.config import settings


def ensure_backend_ready(service: object, name: str) -> object:
    if service is None:
        raise HTTPException(
            status_code=503,
            detail=(
                f"{name} is not configured on this server. "
                "Set the Supabase/Gemini environment variables before use."
            ),
        )
    return service
