import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it } from "vitest";

import { ContextualGuide } from "@/components/guide/contextual-guide";
import { writingTask1Topic } from "@/lib/guide";

describe("ContextualGuide", () => {
  it("is collapsed by default and expands on click", async () => {
    const user = userEvent.setup();
    render(
      <ContextualGuide
        topic={writingTask1Topic}
        bandInfo={{ band: 6, hasData: true }}
        title="How to attempt Writing Task 1"
      />,
    );

    expect(screen.getByText("How to attempt Writing Task 1")).toBeInTheDocument();
    expect(screen.queryByText("How to attempt it")).not.toBeInTheDocument();

    await user.click(screen.getByRole("button", { name: /How to attempt Writing Task 1/ }));

    expect(screen.getByText("How to attempt it")).toBeInTheDocument();
    expect(screen.getByText("Word & time limits")).toBeInTheDocument();
    expect(screen.getByText("Band-specific advice")).toBeInTheDocument();
  });
});
