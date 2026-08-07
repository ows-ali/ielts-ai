import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { BadgeGrid } from "@/components/badges/badge-grid";
import type { Badge } from "@/lib/types";

const badges: Badge[] = [
  {
    id: "first_step",
    name: "First Step",
    emoji: "🎙️",
    category: "speaking",
    description: "Complete your first speaking exercise.",
    earned: true,
  },
  {
    id: "task1_explorer",
    name: "Task 1 Explorer",
    emoji: "📊",
    category: "writing",
    description: "Submit answers for all 7 Task 1 question types.",
    earned: false,
    progress: { current: 3, target: 7 },
  },
];

describe("BadgeGrid", () => {
  it("renders earned and locked badges with section headings", () => {
    render(<BadgeGrid badges={badges} />);

    expect(screen.getByText("Speaking")).toBeInTheDocument();
    expect(screen.getByText("Writing")).toBeInTheDocument();
    expect(screen.getByText("First Step")).toBeInTheDocument();
    expect(screen.getByText("Task 1 Explorer")).toBeInTheDocument();
  });

  it("marks locked badges with a lock and shows progress", () => {
    render(<BadgeGrid badges={badges} />);

    const locked = screen.getByText("Task 1 Explorer");
    expect(locked).toBeInTheDocument();
    expect(screen.getByText("3/7")).toBeInTheDocument();
    const card = locked.closest("[data-earned]");
    expect(card?.getAttribute("data-earned")).toBe("false");
    const earnedCard = screen.getByText("First Step").closest("[data-earned]");
    expect(earnedCard?.getAttribute("data-earned")).toBe("true");
  });

  it("hides locked badges when showLocked is false", () => {
    render(<BadgeGrid badges={badges} showLocked={false} />);

    expect(screen.getByText("First Step")).toBeInTheDocument();
    expect(screen.queryByText("Task 1 Explorer")).not.toBeInTheDocument();
  });

  it("shows an empty state when there are no badges", () => {
    render(<BadgeGrid badges={[]} />);
    expect(screen.getByText("No badges to show yet.")).toBeInTheDocument();
  });
});
