"""Community leaderboards and activity feed.

Everything is derived from existing tables' timestamps so new students always
have a way to surface: the weekly board resets, improvers reward progress, and
the activity feed shows whoever acted most recently.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from app.services.badges import TASK1_TYPES, TASK2_TYPES, compute_badges

TASK1_TYPE_LABELS = {
    "line": "line graph",
    "bar": "bar chart",
    "pie": "pie chart",
    "table": "table",
    "map": "map",
    "process": "process diagram",
    "multi": "mixed chart",
}
TASK2_TYPE_LABELS = {
    "opinion": "opinion essay",
    "discussion": "discussion essay",
    "advantages": "advantages / disadvantages essay",
    "problem_solution": "problem-solution essay",
    "positive_negative": "positive / negative essay",
    "double_question": "double-question essay",
}

IMPROVEMENT_WINDOW = timedelta(days=30)
ACTIVITY_LIMIT = 30


def _parse_ts(value: object) -> datetime | None:
    if not value:
        return None
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return None


def _iso_week_start(now: datetime | None = None) -> datetime:
    now = now or datetime.now(timezone.utc)
    monday = now - timedelta(days=now.weekday())
    return monday.replace(hour=0, minute=0, second=0, microsecond=0)


def _nested(obj: dict | None, key: str) -> dict | None:
    if not isinstance(obj, dict):
        return None
    val = obj.get(key)
    return val if isinstance(val, dict) else None


def _group(rows: list[dict], key: str) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}
    for row in rows:
        k = row.get(key)
        if k:
            grouped.setdefault(k, []).append(row)
    return grouped


def _parts_by_user(answers: list[dict]) -> dict[str, set[int]]:
    parts: dict[str, set[int]] = {}
    for row in answers:
        sid = row.get("student_id")
        if not sid:
            continue
        room = _nested(row, "rooms")
        part = room.get("part") if room else None
        if part is not None:
            parts.setdefault(sid, set()).add(int(part))
    return parts


def build_community(
    students: list[dict],
    evals: list[dict],
    subs: list[dict],
    feedback: list[dict],
    answers: list[dict],
    now: datetime | None = None,
) -> dict:
    now = now or datetime.now(timezone.utc)
    week_start = _iso_week_start(now)
    window_start = now - IMPROVEMENT_WINDOW
    mid = now - IMPROVEMENT_WINDOW / 2

    evals_by_user = _group(evals, "student_id")
    subs_by_user = _group(subs, "student_id")
    fb_by_user: dict[str, list[dict]] = {}
    for f in feedback:
        sid = _nested(f, "writing_submissions")
        sid = sid.get("student_id") if sid else None
        if sid:
            fb_by_user.setdefault(sid, []).append(f)
    parts_by_user = _parts_by_user(answers)

    students = [s for s in students if s.get("role") == "student"]
    name_by_id = {s["id"]: (s.get("name") or "Student") for s in students}

    week: list[dict] = []
    all_board: list[dict] = []
    improvers: list[dict] = []

    for s in students:
        sid = s["id"]
        u_evals = evals_by_user.get(sid, [])
        u_subs = subs_by_user.get(sid, [])
        u_fb = fb_by_user.get(sid, [])
        name = name_by_id[sid]

        badges = compute_badges(
            u_evals,
            sorted(parts_by_user.get(sid, set())),
            u_subs,
            u_fb,
        )
        badge_count = sum(1 for b in badges if b["earned"])

        def in_week(ts: object) -> bool:
            parsed = _parse_ts(ts) or now
            return parsed >= week_start

        week_points = (
            sum(1 for e in u_evals if in_week(e.get("created_at")))
            + sum(1 for x in u_subs if in_week(x.get("created_at")))
            + sum(1 for x in u_fb if in_week(x.get("created_at")))
        )
        all_points = len(u_evals) + len(u_subs) + len(u_fb)
        bands = [
            float(e.get("overall_band"))
            for e in u_evals
            if e.get("overall_band") is not None
        ]
        avg_band = round(sum(bands) / len(bands), 1) if bands else None

        entry = {
            "user_id": sid,
            "name": name,
            "badge_count": badge_count,
            "week_points": week_points,
            "all_points": all_points,
            "avg_band": avg_band,
            "improvement": None,
        }
        week.append(entry)
        all_board.append(entry)

        recent = [
            e for e in u_evals
            if (_parse_ts(e.get("created_at")) or now) >= window_start
        ]
        first_half = [
            e for e in recent
            if (_parse_ts(e.get("created_at")) or now) < mid
        ]
        second_half = [
            e for e in recent
            if (_parse_ts(e.get("created_at")) or now) >= mid
        ]
        first_bands = [float(e["overall_band"]) for e in first_half if e.get("overall_band") is not None]
        second_bands = [float(e["overall_band"]) for e in second_half if e.get("overall_band") is not None]
        if first_bands and second_bands:
            delta = round(
                sum(second_bands) / len(second_bands)
                - sum(first_bands) / len(first_bands),
                1,
            )
            improvers.append({**entry, "improvement": delta})

    def _sort_key(e: dict) -> tuple:
        avg = e.get("avg_band") if e.get("avg_band") is not None else -1
        return (-e["week_points"], -avg, e["name"])

    week.sort(key=_sort_key)
    all_board.sort(
        key=lambda e: (-e["all_points"], -(e.get("avg_band") or -1), e["name"])
    )
    improvers.sort(
        key=lambda e: (
            -(e.get("improvement") or -1),
            -e["all_points"],
            e["name"],
        )
    )

    return {
        "week": week,
        "all": all_board,
        "improvers": improvers,
        "activity": build_activity(students, evals, subs, feedback, now),
    }


def build_activity(
    students: list[dict],
    evals: list[dict],
    subs: list[dict],
    feedback: list[dict],
    now: datetime | None = None,
) -> list[dict]:
    """Chronological feed of recent user actions (newest first)."""
    del now
    name_by_id = {s["id"]: (s.get("name") or "Student") for s in students}
    events: list[dict] = []

    for e in evals:
        ts = _parse_ts(e.get("created_at"))
        if not ts:
            continue
        sid = e.get("student_id")
        band = e.get("overall_band")
        detail = "completed a speaking exercise"
        if band is not None:
            detail += f" and scored Band {band}"
        events.append(
            {
                "id": f"eval:{e.get('id')}",
                "actor_id": sid,
                "actor_name": name_by_id.get(sid, "Student"),
                "kind": "speaking_evaluation",
                "detail": detail,
                "created_at": ts.isoformat(),
            }
        )

    for s in subs:
        ts = _parse_ts(s.get("created_at"))
        if not ts:
            continue
        sid = s.get("student_id")
        qtype_obj = _nested(s, "writing_questions")
        qtype = qtype_obj.get("type") if qtype_obj else None
        part = int(s.get("part") or 1)
        label = TASK1_TYPE_LABELS.get(qtype) or TASK2_TYPE_LABELS.get(qtype) or "answer"
        events.append(
            {
                "id": f"sub:{s.get('id')}",
                "actor_id": sid,
                "actor_name": name_by_id.get(sid, "Student"),
                "kind": "writing_submission",
                "detail": f"submitted a Task {part} {label}",
                "created_at": ts.isoformat(),
            }
        )

    for f in feedback:
        ts = _parse_ts(f.get("created_at"))
        if not ts:
            continue
        sub_obj = _nested(f, "writing_submissions")
        sid = sub_obj.get("student_id") if sub_obj else None
        band = f.get("overall_band")
        detail = "received writing feedback"
        if band is not None:
            detail += f" (Band {band})"
        events.append(
            {
                "id": f"fb:{f.get('id')}",
                "actor_id": sid,
                "actor_name": name_by_id.get(sid, "Student"),
                "kind": "writing_feedback",
                "detail": detail,
                "created_at": ts.isoformat(),
            }
        )

    events.sort(key=lambda ev: ev["created_at"], reverse=True)
    return events[:ACTIVITY_LIMIT]
