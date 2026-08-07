"""Seed the writing Task 1 practice content into Supabase.

Idempotent and non-destructive: matches questions by title and updates them
in place (preserving their id), so existing student submissions and teacher
feedback keep pointing at the same questions. Samples are re-seeded per
question (nothing references them).

Usage:
    python -m scripts.seed_writing
    python -m scripts.seed_writing --reset   # full clear + reinsert (destructive)

Requires SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY in .env.
"""

import argparse
import asyncio
import os

from dotenv import load_dotenv
from supabase import AsyncClientOptions, create_async_client

from scripts.writing_data import QUESTIONS, SAMPLES

load_dotenv()

NIL_UUID = "00000000-0000-0000-0000-000000000000"


async def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Clear and reinsert all writing content (destructive)")
    args = parser.parse_args()

    supabase = await create_async_client(
        os.environ["SUPABASE_URL"],
        os.environ["SUPABASE_SERVICE_ROLE_KEY"],
        options=AsyncClientOptions(postgrest_client_timeout=30, storage_client_timeout=30),
    )

    if args.reset:
        await supabase.table("writing_samples").delete().neq("id", NIL_UUID).execute()
        await supabase.table("writing_questions").delete().neq("id", NIL_UUID).execute()
        print("Reset: cleared existing writing content.")

    existing = (
        await supabase.table("writing_questions").select("id", "title").execute()
    ).data or []
    existing_by_title = {row["title"]: row["id"] for row in existing}
    print(f"Found {len(existing_by_title)} existing question(s).")

    total_samples = 0
    updated = 0
    inserted = 0

    for idx, q in enumerate(QUESTIONS):
        question_payload = {
            "type": q["type"],
            "title": q["title"],
            "prompt": q["prompt"],
            "data_description": q.get("data_description"),
            "image_url": q.get("image_url"),
            "difficulty": q.get("difficulty", "medium"),
        }

        question_id = existing_by_title.get(q["title"])
        if question_id:
            await supabase.table("writing_questions").update(question_payload).eq("id", question_id).execute()
            updated += 1
        else:
            created = (
                await supabase.table("writing_questions").insert(question_payload).execute()
            )
            question_id = created.data[0]["id"]
            inserted += 1

        # Re-seed this question's samples (safe: nothing references writing_samples)
        await supabase.table("writing_samples").delete().eq("question_id", question_id).execute()

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

    print(f"Done. Updated {updated}, inserted {inserted} questions, re-seeded {total_samples} samples.")
    if not args.reset:
        print("Existing submissions and feedback were preserved.")


if __name__ == "__main__":
    asyncio.run(main())
