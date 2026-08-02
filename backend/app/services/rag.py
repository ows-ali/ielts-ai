import json

import httpx

from app.core.config import settings
from app.services.check import ensure_backend_ready
from app.services.supabase_client import get_supabase_client

EMBEDDING_MODEL = "gemini-embedding-2"
EMBEDDING_DIMENSIONS = 768


async def _embed(text: str) -> list[float]:
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{EMBEDDING_MODEL}:embedContent?key={settings.gemini_api_key}"
    )
    body = {
        "model": f"models/{EMBEDDING_MODEL}",
        "content": {"parts": [{"text": text}]},
        "outputDimensionality": EMBEDDING_DIMENSIONS,
    }
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.post(url, json=body)
        resp.raise_for_status()
        return resp.json()["embedding"]["values"]


async def retrieve_ielts_criteria(query: str, top_k: int = 4) -> str:
    """Vector search over the IELTS band-descriptor knowledge base."""
    client = get_supabase_client()
    ensure_backend_ready(client, "Supabase")
    embedding = await _embed(query)
    data = await client.rpc(
        "match_criteria",
        {"query_embedding": json.dumps(embedding), "match_count": top_k},
    ).execute()
    rows = data.data or []
    return "\n\n".join(
        f"[{r.get('part')} | {r.get('criterion')} | {r.get('band')}] {r.get('content')}"
        for r in rows
    )
