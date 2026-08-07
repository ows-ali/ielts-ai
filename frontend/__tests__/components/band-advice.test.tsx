import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it } from "vitest";

import { BandAdviceBlock } from "@/components/guide/band-advice";
import type { BandAdvice, BandLevel } from "@/lib/guide";

const advice: Record<BandLevel, BandAdvice> = {
  5: { do: ["Answer every question"], dont: ["Don't give one-word answers"], tip: "Focus on fluency first." },
  6: { do: ["Speak at length"], dont: ["Don't overuse the same words"], tip: "Broaden your vocabulary." },
  7: { do: ["Use idiomatic vocabulary"], dont: ["Don't force idioms"], tip: "Work on Part 3 depth." },
  8: { do: ["Speak effortlessly"], dont: ["Don't rehearse"], tip: "Polish the last 5%." },
};

describe("BandAdviceBlock", () => {
  it("shows the current band's advice by default", () => {
    render(<BandAdviceBlock advice={advice} currentBand={6} hasData skillLabel="Speaking" />);

    expect(screen.getByText("Band-specific advice")).toBeInTheDocument();
    expect(screen.getByText(/Based on your current speaking band/)).toBeInTheDocument();
    expect(screen.getByText("Speak at length")).toBeInTheDocument();
    expect(screen.getByText("Don't overuse the same words")).toBeInTheDocument();
    expect(screen.getByText(/To move to Band 7/)).toBeInTheDocument();
    expect(screen.getByText("Broaden your vocabulary.")).toBeInTheDocument();
  });

  it("switches to another band when a pill is clicked", async () => {
    const user = userEvent.setup();
    render(<BandAdviceBlock advice={advice} currentBand={5} hasData skillLabel="Writing" />);

    expect(screen.getByText("Answer every question")).toBeInTheDocument();

    await user.click(screen.getByRole("button", { name: "Band 8" }));

    expect(screen.getByText("Speak effortlessly")).toBeInTheDocument();
    expect(screen.getByText("Don't rehearse")).toBeInTheDocument();
    expect(screen.getByText(/To move to Band 9/)).toBeInTheDocument();
  });

  it("prompts for an attempt when there is no data yet", () => {
    render(<BandAdviceBlock advice={advice} currentBand={5} hasData={false} skillLabel="Speaking" />);

    expect(
      screen.getByText("Complete an attempt to get personalised advice — showing Band 5 guidance for now."),
    ).toBeInTheDocument();
    expect(screen.getByText("Answer every question")).toBeInTheDocument();
  });
});
