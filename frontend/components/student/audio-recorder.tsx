"use client";

import { useCallback, useEffect, useRef, useState } from "react";

function pickMimeType(): string | undefined {
  const candidates = [
    "audio/mp4;codecs=mp4a.40.2",
    "audio/webm;codecs=opus",
    "audio/webm",
  ];
  for (const c of candidates) {
    if (typeof MediaRecorder !== "undefined" && MediaRecorder.isTypeSupported(c)) {
      return c;
    }
  }
  return undefined;
}

export function AudioRecorder({
  onRecorded,
  onStateChange,
}: {
  onRecorded: (blob: Blob, mimeType: string) => Promise<void>;
  onStateChange?: (recording: boolean) => void;
}) {
  const [recording, setRecording] = useState(false);
  const [time, setTime] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const mediaRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const stopInternal = useCallback(() => {
    mediaRef.current?.stop();
    if (intervalRef.current) clearInterval(intervalRef.current);
    setRecording(false);
    setTime(0);
    onStateChange?.(false);
  }, [onStateChange]);

  useEffect(() => {
    return () => stopInternal();
  }, [stopInternal]);

  async function start() {
    setError(null);
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mime = pickMimeType();
      const recorder = new MediaRecorder(stream, mime ? { mimeType: mime } : undefined);
      chunksRef.current = [];
      recorder.ondataavailable = (e) => {
        if (e.data.size > 0) chunksRef.current.push(e.data);
      };
      recorder.onstop = async () => {
        stream.getTracks().forEach((t) => t.stop());
        const blob = new Blob(chunksRef.current, {
          type: recorder.mimeType || "audio/webm",
        });
        setRecording(false);
        setTime(0);
        if (intervalRef.current) clearInterval(intervalRef.current);
        onStateChange?.(false);
        if (blob.size > 0) {
          await onRecorded(blob, recorder.mimeType || "audio/webm");
        }
      };
      recorder.start();
      mediaRef.current = recorder;
      setRecording(true);
      onStateChange?.(true);
      setTime(0);
      intervalRef.current = setInterval(() => setTime((t) => t + 1), 1000);
    } catch {
      setError("Microphone access was denied.");
    }
  }

  function stop() {
    stopInternal();
  }

  return (
    <div className="flex flex-col items-center gap-3">
      <button
        type="button"
        onClick={recording ? stop : start}
        className={
          "flex h-24 w-24 items-center justify-center rounded-full text-white transition-transform " +
          (recording
            ? "animate-pulse bg-rose-600"
            : "bg-emerald-600 hover:scale-105")
        }
        aria-label={recording ? "Stop recording" : "Start recording"}
      >
        {recording ? (
          <span className="text-3xl">■</span>
        ) : (
          <span className="text-3xl">●</span>
        )}
      </button>
      <p className="text-sm text-slate-500">
        {recording ? `Recording... ${time}s (click to stop)` : "Tap to record your answer"}
      </p>
      {error && <p className="text-sm text-rose-600">{error}</p>}
    </div>
  );
}
