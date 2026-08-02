import { act, fireEvent, render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import { AudioRecorder } from "@/components/student/audio-recorder";

class MockMediaRecorder {
  static isTypeSupported: (type: string) => boolean;
  mimeType: string;
  ondataavailable: ((e: { data: Blob }) => void) | null;
  onstop: (() => void) | null;
  start: ReturnType<typeof vi.fn>;
  stop: ReturnType<typeof vi.fn>;

  constructor(stream?: MediaStream, options?: MediaRecorderOptions) {
    this.mimeType = options?.mimeType ?? "audio/webm";
    this.ondataavailable = null;
    this.onstop = null;
    this.start = vi.fn(() => {
      this.ondataavailable?.({
        data: new Blob([new Uint8Array([1, 2, 3])], { type: this.mimeType }),
      });
    });
    this.stop = vi.fn(() => {
      this.onstop?.();
    });
  }
}
MockMediaRecorder.isTypeSupported = vi.fn().mockReturnValue(true);

function mockMedia() {
  MockMediaRecorder.isTypeSupported = vi.fn().mockReturnValue(true);
  const tracks = [{ stop: vi.fn() }];
  const getUserMedia = vi.fn().mockResolvedValue({ getTracks: () => tracks });
  Object.defineProperty(window.navigator, "mediaDevices", {
    value: { getUserMedia },
    configurable: true,
  });
  vi.stubGlobal("MediaRecorder", MockMediaRecorder);
  return { getUserMedia, tracks };
}

describe("AudioRecorder", () => {
  beforeEach(() => {
    mockMedia();
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  it("renders the idle state", () => {
    render(<AudioRecorder onRecorded={vi.fn()} />);
    expect(screen.getByRole("button", { name: "Start recording" })).toBeInTheDocument();
    expect(screen.getByText(/Tap to record your answer/)).toBeInTheDocument();
  });

  it("starts recording and reports state changes", async () => {
    const user = userEvent.setup();
    const onStateChange = vi.fn();
    render(<AudioRecorder onRecorded={vi.fn()} onStateChange={onStateChange} />);

    await user.click(screen.getByRole("button", { name: "Start recording" }));

    await waitFor(() => expect(onStateChange).toHaveBeenCalledWith(true));
    expect(screen.getByRole("button", { name: "Stop recording" })).toBeInTheDocument();
    expect(screen.getByText(/Recording\.\.\./)).toBeInTheDocument();
  });

  it("ticks the elapsed time while recording", async () => {
    vi.useFakeTimers();
    render(<AudioRecorder onRecorded={vi.fn()} />);

    fireEvent.click(screen.getByRole("button", { name: "Start recording" }));
    await act(async () => {});
    expect(screen.getByText(/Recording\.\.\. 0s/)).toBeInTheDocument();

    await act(async () => {
      vi.advanceTimersByTime(4000);
    });
    expect(screen.getByText(/Recording\.\.\. 4s/)).toBeInTheDocument();
  });

  it("delivers the recorded blob and stops on user stop", async () => {
    const user = userEvent.setup();
    const onRecorded = vi.fn();
    const onStateChange = vi.fn();
    render(<AudioRecorder onRecorded={onRecorded} onStateChange={onStateChange} />);

    await user.click(screen.getByRole("button", { name: "Start recording" }));
    await waitFor(() => expect(screen.getByRole("button", { name: "Stop recording" })).toBeInTheDocument());
    await user.click(screen.getByRole("button", { name: "Stop recording" }));

    await waitFor(() => expect(onRecorded).toHaveBeenCalledTimes(1));
    const [blob, mime] = onRecorded.mock.calls[0] as [Blob, string];
    expect(blob.size).toBeGreaterThan(0);
    expect(mime).toBe("audio/mp4;codecs=mp4a.40.2");
    expect(onStateChange).toHaveBeenLastCalledWith(false);
    expect(screen.getByRole("button", { name: "Start recording" })).toBeInTheDocument();
  });

  it("shows an error when microphone access is denied", async () => {
    const getUserMedia = vi.fn().mockRejectedValue(new Error("denied"));
    Object.defineProperty(window.navigator, "mediaDevices", {
      value: { getUserMedia },
      configurable: true,
    });
    const user = userEvent.setup();
    render(<AudioRecorder onRecorded={vi.fn()} />);

    await user.click(screen.getByRole("button", { name: "Start recording" }));

    expect(await screen.findByText("Microphone access was denied.")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Start recording" })).toBeInTheDocument();
  });
});
