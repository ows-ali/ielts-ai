import functools

from supabase import AsyncClient, create_async_client

from app.core.config import settings


@functools.lru_cache
def get_supabase_client() -> AsyncClient | None:
    if not settings.supabase_url or not settings.supabase_service_role_key:
        return None
    client = create_async_client(
        settings.supabase_url,
        settings.supabase_service_role_key,
        postgrest_client_timeout=15,
        storage_client_timeout=15,
    )
    return client
