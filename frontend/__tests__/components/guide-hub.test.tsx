import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it } from "vitest";

import { GuideHub } from "@/components/guide/guide-hub";
import { guideTopics } from "@/lib/guide";
import type { BandInfo, GuideTopicId } from "@/lib/guide";

const bandInfo: Record<GuideTopicId, BandInfo> = {
  speaking: { band: 6, hasData: true },
  "writing-task1": { band: 5, hasData: false },
  "writing-task2": { band: 5, hasData: false },
  scoring: { band: 6, hasData: true },
};

describe("GuideHub", () => {
  it("shows the first topic by default", () => {
    render(<GuideHub topics={guideTopics} bandInfo={bandInfo} />);

    expect(screen.getByRole("heading", { name: "🎙️ Speaking" })).toBeInTheDocument();
    expect(screen.getByText("How to attempt it")).toBeInTheDocument();
    expect(screen.getByText(/The Speaking test takes 11–14 minutes/)).toBeInTheDocument();
  });

  it("switches topics via the pill tabs", async () => {
    const user = userEvent.setup();
    render(<GuideHub topics={guideTopics} bandInfo={bandInfo} />);

    await user.click(screen.getByRole("button", { name: "📊 Writing Task 1" }));

    expect(screen.getByText(/Write at least 150 words in 20 minutes/)).toBeInTheDocument();
    expect(screen.getByText("Word & time limits")).toBeInTheDocument();
  });

  it("shows band-specific advice within each topic", async () => {
    const user = userEvent.setup();
    render(<GuideHub topics={guideTopics} bandInfo={bandInfo} />);

    expect(screen.getByText("Band-specific advice")).toBeInTheDocument();

    await user.click(screen.getByRole("button", { name: "🎯 How Scoring Works" }));

    expect(screen.getByText(/IELTS is scored on a 9-band scale/)).toBeInTheDocument();
    expect(screen.getByText("The 9-band scale")).toBeInTheDocument();
    expect(screen.getByText("Band-specific advice")).toBeInTheDocument();
  });
});
