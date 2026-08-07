import { render, screen, within } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { LeaderboardPreview } from "@/components/landing/leaderboard-preview";
import type { ActivityEvent, LeaderboardEntry } from "@/lib/types";

const week: LeaderboardEntry[] = [
  { user_id: "u1", name: "Alice", badge_count: 3, week_points: 5, all_points: 12, avg_band: 7.0 },
  { user_id: "u2", name: "Bob", badge_count: 1, week_points: 2, all_points: 4, avg_band: 5.5 },
];

const leaderboard = () =>
  within(
    screen.getByRole("heading", { name: "Top Students This Week" }).closest(".rounded-2xl") as HTMLElement,
  );

const activity: ActivityEvent[] = [
  {
    id: "eval:1",
    actor_id: "u1",
    actor_name: "Alice",
    kind: "speaking_evaluation",
    detail: "completed a speaking exercise and scored Band 7",
    created_at: new Date().toISOString(),
  },
  {
    id: "sub:1",
    actor_id: "u2",
    actor_name: "Bob",
    kind: "writing_submission",
    detail: "submitted a Writing Task 2 essay",
    created_at: new Date().toISOString(),
  },
];

describe("LeaderboardPreview", () => {
  it("shows only the top students from the weekly board", () => {
    render(<LeaderboardPreview week={week} activity={activity} />);
    expect(screen.getByText("Top Students This Week")).toBeInTheDocument();
    expect(leaderboard().getByText("Alice")).toBeInTheDocument();
    expect(leaderboard().getByText("Bob")).toBeInTheDocument();
    expect(leaderboard().getByText((_, el) => el?.textContent === "5 pts")).toBeInTheDocument();
  });

  it("links to the full community page", () => {
    render(<LeaderboardPreview week={week} activity={activity} />);
    const link = screen.getByRole("link", { name: "View full community →" });
    expect(link).toHaveAttribute("href", "/community");
  });

  it("links each student to their public profile", () => {
    render(<LeaderboardPreview week={week} activity={activity} />);
    expect(leaderboard().getByRole("link", { name: "Alice" })).toHaveAttribute("href", "/profile/u1");
    expect(leaderboard().getByRole("link", { name: "Bob" })).toHaveAttribute("href", "/profile/u2");
  });

  it("shows recent activity with actor and detail", () => {
    render(<LeaderboardPreview week={week} activity={activity} />);
    expect(screen.getByText("Recent Activity")).toBeInTheDocument();
    expect(screen.getByText("completed a speaking exercise and scored Band 7")).toBeInTheDocument();
    expect(screen.getByText("submitted a Writing Task 2 essay")).toBeInTheDocument();
  });

  it("shows an empty state when the weekly board has no entries", () => {
    render(<LeaderboardPreview week={[]} activity={[]} />);
    expect(screen.getByText("No activity yet this week — be the first to get on the board!")).toBeInTheDocument();
    expect(screen.getByText("No recent activity yet.")).toBeInTheDocument();
  });
});
