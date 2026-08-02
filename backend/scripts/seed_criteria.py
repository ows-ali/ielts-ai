"""Seed the IELTS band-descriptor knowledge base (RAG) with embeddings.

Usage:
    python -m scripts.seed_criteria

Requires SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY and GEMINI_API_KEY in .env.
"""

import asyncio
import json
import os

import httpx
from dotenv import load_dotenv

from supabase import create_client

load_dotenv()

EMBEDDING_MODEL = "text-embedding-004"

CRITERIA: list[dict] = [
    # Fluency & Coherence
    {"part": 1, "criterion": "fluency", "band": "9",
     "content": "Speaks fluently with only rare repetition or self-correction. Uses full range of cohesion and linking devices. Topics developed at length."},
    {"part": 1, "criterion": "fluency", "band": "8",
     "content": "Speaks fluently with occasional repetition or self-correction. Uses a wide range of cohesive devices flexibly. Develops topics fully."},
    {"part": 1, "criterion": "fluency", "band": "7",
     "content": "Speaks at length without noticeable effort. Some hesitation, repetition or self-correction. Uses a range of connectives flexibly."},
    {"part": 1, "criterion": "fluency", "band": "6",
     "content": "Willing to speak at length though may lose coherence at times. Some hesitation, repetition and self-correction. Uses some linking words."},
    {"part": 1, "criterion": "fluency", "band": "5",
     "content": "Keeps going but with noticeable hesitation, repetition and self-correction. May lose coherence. Uses basic connectives."},
    # Lexical Resource (vocabulary)
    {"part": 1, "criterion": "vocabulary", "band": "9",
     "content": "Uses vocabulary with full flexibility and precision in all topics. Idiomatic language naturally and accurately."},
    {"part": 1, "criterion": "vocabulary", "band": "8",
     "content": "Uses a wide vocabulary resource readily and flexibly. Less common and idiomatic vocabulary with occasional inaccuracies."},
    {"part": 1, "criterion": "vocabulary", "band": "7",
     "content": "Uses vocabulary resource flexibly to discuss a variety of topics. Uses some less common and idiomatic vocabulary."},
    {"part": 1, "criterion": "vocabulary", "band": "6",
     "content": "Has a wide enough vocabulary to discuss topics at length. Uses some less common vocabulary with some inaccuracy."},
    {"part": 1, "criterion": "vocabulary", "band": "5",
     "content": "Uses vocabulary limited to common topics. Repetition of the same words and frequent errors in word choice."},
    # Grammatical Range & Accuracy
    {"part": 1, "criterion": "grammar", "band": "9",
     "content": "Uses a full range of structures naturally and appropriately. Errors rare; errors occur only as slips."},
    {"part": 1, "criterion": "grammar", "band": "8",
     "content": "Uses a wide range of structures flexibly. Most sentences error-free, with only occasional inappropriacies."},
    {"part": 1, "criterion": "grammar", "band": "7",
     "content": "Uses a range of complex structures with some flexibility. Frequently produces error-free sentences."},
    {"part": 1, "criterion": "grammar", "band": "6",
     "content": "Uses a mix of simple and complex structures but with limited flexibility. Errors occur but rarely cause comprehension problems."},
    {"part": 1, "criterion": "grammar", "band": "5",
     "content": "Uses only a limited range of structures. Errors may cause frequent comprehension problems."},
    # Pronunciation
    {"part": 1, "criterion": "pronunciation", "band": "9",
     "content": "Uses a full range of pronunciation features with precision and subtlety. Effortlessly easy to understand."},
    {"part": 1, "criterion": "pronunciation", "band": "8",
     "content": "Uses a wide range of pronunciation features and sustains flexible use. Easy to understand throughout."},
    {"part": 1, "criterion": "pronunciation", "band": "7",
     "content": "Shows all the positive features of Band 6 and some of Band 8. Generally easy to understand."},
    {"part": 1, "criterion": "pronunciation", "band": "6",
     "content": "Uses a range of pronunciation features with mixed control. Can be understood throughout though occasional lapses occur."},
    {"part": 1, "criterion": "pronunciation", "band": "5",
     "content": "Shows all the positive features of Band 4. Can generally be understood though mispronunciations may cause strain."},
]


async def embed(client: httpx.AsyncClient, text: str) -> list[float]:
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{EMBEDDING_MODEL}:embedContent?key={os.environ['GEMINI_API_KEY']}"
    )
    body = {"model": f"models/{EMBEDDING_MODEL}", "content": {"parts": [{"text": text}]}}
    resp = await client.post(url, json=body)
    resp.raise_for_status()
    return resp.json()["embedding"]["values"]


async def main() -> None:
    supabase = create_client(
        os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_ROLE_KEY"]
    )
    async with httpx.AsyncClient(timeout=60) as client:
        for row in CRITERIA:
            query = (
                f"IELTS Speaking band descriptor for {row['criterion']} band {row['band']}: "
                f"{row['content']}"
            )
            vec = await embed(client, query)
            supabase.table("ielts_criteria").insert(
                {
                    "part": row["part"],
                    "criterion": row["criterion"],
                    "band": row["band"],
                    "content": row["content"],
                    "embedding": vec,
                }
            ).execute()
            print(f"seeded band {row['band']} {row['criterion']}")
    print("Done.")


if __name__ == "__main__":
    asyncio.run(main())
