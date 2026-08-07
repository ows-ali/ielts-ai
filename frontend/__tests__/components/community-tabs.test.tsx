import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it } from "vitest";

import { CommunityTabs } from "@/components/community/community-tabs";
import type { Community } from "@/lib/types";

const data: Community = {
  week: [
    { user_id: "u1", name: "Alice", badge_count: 3, week_points: 5, all_points: 12, avg_band: 7.0 },
    { user_id: "u2", name: "Bob", badge_count: 1, week_points: 2, all_points: 4, avg_band: 5.5 },
  ],
  all: [
    { user_id: "u2", name: "Bob", badge_count: 1, week_points: 2, all_points: 4, avg_band: 5.5 },
    { user_id: "u1", name: "Alice", badge_count: 3, week_points: 5, all_points: 12, avg_band: 7.0 },
  ],
  improvers: [{ user_id: "u1", name: "Alice", badge_count: 3, week_points: 5, all_points: 12, avg_band: 7.0, improvement: 0.5 }],
  activity: [
    {
      id: "eval:1",
      actor_id: "u1",
      actor_name: "Alice",
      kind: "speaking_evaluation",
      detail: "completed a speaking exercise and scored Band 7",
      created_at: new Date().toISOString(),
    },
  ],
};

describe("CommunityTabs", () => {
  it("shows the This Week board by default", () => {
    render(<CommunityTabs data={data} />);
    expect(screen.getByText("Alice")).toBeInTheDocument();
    expect(screen.getByText("Bob")).toBeInTheDocument();
    expect(screen.getByText("Points reset every Monday — everyone gets a fresh chance.")).toBeInTheDocument();
  });

  it("switches to the All Time board", async () => {
    const user = userEvent.setup();
    render(<CommunityTabs data={data} />);

    await user.click(screen.getByRole("button", { name: "All Time" }));

    expect(screen.getByText("Lifetime points from speaking, writing and feedback.")).toBeInTheDocument();
  });

  it("shows improvement on the Improvers tab", async () => {
    const user = userEvent.setup();
    render(<CommunityTabs data={data} />);

    await user.click(screen.getByRole("button", { name: "Improvers" }));

    expect(screen.getByText("+0.5")).toBeInTheDocument();
    expect(screen.getByText("Most improved average speaking band over the last 30 days.")).toBeInTheDocument();
  });

  it("shows the activity feed with actor and detail", async () => {
    const user = userEvent.setup();
    render(<CommunityTabs data={data} />);

    await user.click(screen.getByRole("button", { name: "Activity" }));

    expect(screen.getByText("completed a speaking exercise and scored Band 7")).toBeInTheDocument();
    expect(screen.getByText(/Speaking ·/)).toBeInTheDocument();
  });

  it("shows an empty state when a board has no entries", () => {
    render(<CommunityTabs data={{ ...data, week: [], all: [], improvers: [], activity: [] }} />);
    expect(screen.getByText("No activity yet — be the first!")).toBeInTheDocument();
  });
});
