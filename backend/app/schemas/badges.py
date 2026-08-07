from pydantic import BaseModel


class BadgeProgress(BaseModel):
    current: int
    target: int


class BadgeOut(BaseModel):
    id: str
    name: str
    emoji: str
    category: str
    description: str
    earned: bool
    progress: BadgeProgress | None = None


class ProfileStatsOut(BaseModel):
    total_speaking_attempts: int = 0
    avg_speaking_band: float | None = None
    best_speaking_band: float | None = None
    speaking_parts: list[int] = []
    writing_submissions: int = 0
    task1_types_done: list[str] = []
    task2_types_done: list[str] = []
    writing_feedback_count: int = 0
    best_writing_band: float | None = None


class BadgeSummaryOut(BaseModel):
    user_id: str
    earned_count: int
    total_count: int
    badges: list[BadgeOut]
    stats: ProfileStatsOut


class PublicProfileOut(BaseModel):
    id: str
    name: str
    role: str
    created_at: str | None = None
    earned_count: int
    total_count: int
    badges: list[BadgeOut]
    stats: ProfileStatsOut


class LeaderboardEntryOut(BaseModel):
    user_id: str
    name: str
    badge_count: int
    week_points: int
    all_points: int
    avg_band: float | None = None
    improvement: float | None = None


class ActivityOut(BaseModel):
    id: str
    actor_id: str
    actor_name: str
    kind: str
    detail: str
    created_at: str


class CommunityOut(BaseModel):
    week: list[LeaderboardEntryOut]
    all: list[LeaderboardEntryOut]
    improvers: list[LeaderboardEntryOut]
    activity: list[ActivityOut]
