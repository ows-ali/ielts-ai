"""Badge catalog and computation for the IELTS app.

Badges are computed on-the-fly from the existing data model (no extra tables).
Each badge exposes an earned state plus optional progress (e.g. 3/7 task types).
"""

from __future__ import annotations

TASK1_TYPES = {"line", "bar", "pie", "table", "map", "process", "multi"}
TASK2_TYPES = {
    "opinion",
    "discussion",
    "advantages",
    "problem_solution",
    "positive_negative",
    "double_question",
}

_BADGE_DEFS = [
    # --- Speaking ---
    ("first_step", "First Step", "🎙️", "speaking",
     "Complete your first speaking exercise."),
    ("talker", "Talker", "🗣️", "speaking",
     "Complete 10 speaking exercises."),
    ("chatterbox", "Chatterbox", "💬", "speaking",
     "Complete 25 speaking exercises."),
    ("band6_speaker", "Band 6 Speaker", "🥈", "speaking",
     "Score Band 6 or higher in a speaking exercise."),
    ("band7_speaker", "Band 7 Speaker", "🥇", "speaking",
     "Score Band 7 or higher in a speaking exercise."),
    ("band8_speaker", "Band 8 Speaker", "👑", "speaking",
     "Score Band 8 or higher in a speaking exercise."),
    ("part1_explorer", "Part 1 Explorer", "🗺️", "speaking",
     "Speak in a Part 1 practice room."),
    ("part2_explorer", "Part 2 Explorer", "🗺️", "speaking",
     "Speak in a Part 2 practice room."),
    ("part3_explorer", "Part 3 Explorer", "🗺️", "speaking",
     "Speak in a Part 3 practice room."),
    ("balanced_speaker", "Balanced Speaker", "⚖️", "speaking",
     "Score 7+ in all four speaking criteria in a single exercise."),
    # --- Writing ---
    ("first_draft", "First Draft", "✍️", "writing",
     "Submit your first writing answer."),
    ("prolific_writer", "Prolific Writer", "📝", "writing",
     "Submit 10 writing answers."),
    ("task1_explorer", "Task 1 Explorer", "📊", "writing",
     "Submit answers for all 7 Task 1 question types."),
    ("task2_explorer", "Task 2 Explorer", "🎯", "writing",
     "Submit answers for all 6 Task 2 essay types."),
    ("feedback_seeker", "Feedback Seeker", "💡", "writing",
     "Receive your first piece of writing feedback."),
    ("band7_writer", "Band 7 Writer", "🥇", "writing",
     "Score Band 7 or higher in writing feedback."),
    ("band8_writer", "Band 8 Writer", "👑", "writing",
     "Score Band 8 or higher in writing feedback."),
]

_BADGE_IDS = [b[0] for b in _BADGE_DEFS]


def compute_badges(
    evals: list[dict],
    parts: list[int],
    writing_subs: list[dict],
    writing_feedback: list[dict],
) -> list[dict]:
    """Evaluate the full badge catalog for one user.

    Args:
        evals: speaking evaluations with overall_band / sub-scores.
        parts: distinct speaking room parts the user has answered in.
        writing_subs: writing submissions with a ``type`` key.
        writing_feedback: writing feedback rows with an ``overall_band`` key.
    """
    eval_count = len(evals)
    best_band = max(
        (float(e.get("overall_band") or 0) for e in evals), default=0.0
    )
    balanced = any(
        all((e.get(k) or 0) >= 7 for k in ("fluency", "grammar", "vocabulary", "pronunciation"))
        for e in evals
    )
    parts_set = set(parts)

    sub_count = len(writing_subs)
    types_done = {s.get("type") for s in writing_subs}
    task1_done = TASK1_TYPES & types_done
    task2_done = TASK2_TYPES & types_done

    feedback_count = len(writing_feedback)
    best_writer_band = max(
        (float(f.get("overall_band") or 0) for f in writing_feedback), default=0.0
    )

    def progress(current: int, target: int) -> dict:
        return {"current": current, "target": target}

    earned = {
        "first_step": eval_count >= 1,
        "talker": eval_count >= 10,
        "chatterbox": eval_count >= 25,
        "band6_speaker": best_band >= 6,
        "band7_speaker": best_band >= 7,
        "band8_speaker": best_band >= 8,
        "part1_explorer": 1 in parts_set,
        "part2_explorer": 2 in parts_set,
        "part3_explorer": 3 in parts_set,
        "balanced_speaker": balanced,
        "first_draft": sub_count >= 1,
        "prolific_writer": sub_count >= 10,
        "task1_explorer": len(task1_done) == len(TASK1_TYPES),
        "task2_explorer": len(task2_done) == len(TASK2_TYPES),
        "feedback_seeker": feedback_count >= 1,
        "band7_writer": best_writer_band >= 7,
        "band8_writer": best_writer_band >= 8,
    }

    progress_map = {
        "talker": progress(eval_count, 10),
        "chatterbox": progress(eval_count, 25),
        "prolific_writer": progress(sub_count, 10),
        "task1_explorer": progress(len(task1_done), len(TASK1_TYPES)),
        "task2_explorer": progress(len(task2_done), len(TASK2_TYPES)),
    }

    out: list[dict] = []
    for bid, name, emoji, category, description in _BADGE_DEFS:
        out.append(
            {
                "id": bid,
                "name": name,
                "emoji": emoji,
                "category": category,
                "description": description,
                "earned": earned[bid],
                "progress": progress_map.get(bid),
            }
        )
    return out


def compute_stats(
    evals: list[dict],
    parts: list[int],
    writing_subs: list[dict],
    writing_feedback: list[dict],
) -> dict:
    """Aggregate public-facing stats for a user profile."""
    bands = [
        float(e.get("overall_band"))
        for e in evals
        if e.get("overall_band") is not None
    ]
    avg_band = round(sum(bands) / len(bands), 1) if bands else None
    best_band = round(max(bands), 1) if bands else None

    types_done = {s.get("type") for s in writing_subs}
    task1_done = sorted(TASK1_TYPES & types_done)
    task2_done = sorted(TASK2_TYPES & types_done)

    fb_bands = [
        float(f.get("overall_band"))
        for f in writing_feedback
        if f.get("overall_band") is not None
    ]

    return {
        "total_speaking_attempts": len(evals),
        "avg_speaking_band": avg_band,
        "best_speaking_band": best_band,
        "speaking_parts": sorted(set(parts)),
        "writing_submissions": len(writing_subs),
        "task1_types_done": task1_done,
        "task2_types_done": task2_done,
        "writing_feedback_count": len(writing_feedback),
        "best_writing_band": round(max(fb_bands), 1) if fb_bands else None,
    }
