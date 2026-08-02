from supabase import AsyncClient, AsyncClientOptions, create_async_client

from app.core.config import settings

_client: AsyncClient | None = None


async def get_supabase_client() -> AsyncClient | None:
    global _client
    if _client is None:
        if not settings.supabase_url or not settings.supabase_service_role_key:
            return None
        _client = await create_async_client(
            settings.supabase_url,
            settings.supabase_service_role_key,
            options=AsyncClientOptions(
                postgrest_client_timeout=15,
                storage_client_timeout=15,
            ),
        )
    return _client
