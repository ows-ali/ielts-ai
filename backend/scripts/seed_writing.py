"""Seed the writing Task 1 practice content into Supabase.

Creates writing_questions, writing_samples tables if missing and populates
them with the curated question bank and model answers from writing_data.py.

Usage:
    python -m scripts.seed_writing

Requires SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY in .env.
"""

import asyncio
import os

from dotenv import load_dotenv
from supabase import AsyncClientOptions, create_async_client

from scripts.writing_data import QUESTIONS, SAMPLES

load_dotenv()


async def main() -> None:
    supabase = await create_async_client(
        os.environ["SUPABASE_URL"],
        os.environ["SUPABASE_SERVICE_ROLE_KEY"],
        options=AsyncClientOptions(postgrest_client_timeout=30, storage_client_timeout=30),
    )

    # Clear any previous content so the seed is idempotent
    await supabase.table("writing_samples").delete().neq("id", "00000000-0000-0000-0000-000000000000").execute()
    await supabase.table("writing_questions").delete().neq("id", "00000000-0000-0000-0000-000000000000").execute()
    print("Cleared existing writing content.")

    total_samples = 0
    for idx, q in enumerate(QUESTIONS):
        question_payload = {
            "type": q["type"],
            "title": q["title"],
            "prompt": q["prompt"],
            "data_description": q.get("data_description"),
            "image_url": q.get("image_url"),
            "difficulty": q.get("difficulty", "medium"),
        }
        created = (
            await supabase.table("writing_questions")
            .insert(question_payload)
            .execute()
        )
        question_id = created.data[0]["id"]

        samples = SAMPLES.get(idx, {})
        for band in ("5", "7", "9"):
            sample = samples.get(band)
            if not sample:
                print(f"  WARNING: no band {band} sample for Q{idx}")
                continue
            await supabase.table("writing_samples").insert(
                {
                    "question_id": question_id,
                    "band": sample["band"],
                    "answer_text": sample["answer_text"],
                    "task_achievement": sample["task_achievement"],
                    "coherence_cohesion": sample["coherence_cohesion"],
                    "lexical_resource": sample["lexical_resource"],
                    "grammatical_range": sample["grammatical_range"],
                    "explanation": sample["explanation"],
                    "improvement_tips": sample["improvement_tips"],
                }
            ).execute()
            total_samples += 1

        print(f"  Seeded Q{idx}: {q['type']} - {q['title']}")

    print(f"Done. Inserted {len(QUESTIONS)} questions and {total_samples} samples.")


if __name__ == "__main__":
    asyncio.run(main())
