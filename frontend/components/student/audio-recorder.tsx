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
  maxDuration = 120,
  maxRetries = 2,
}: {
  onRecorded: (blob: Blob, mimeType: string) => Promise<void>;
  onStateChange?: (recording: boolean) => void;
  /** Max recording duration in seconds (auto-stops). Default 120s. */
  maxDuration?: number;
  /** How many times the user can re-record before submitting. Default 2. */
  maxRetries?: number;
}) {
  const [recording, setRecording] = useState(false);
  const [time, setTime] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const [pendingBlob, setPendingBlob] = useState<{ blob: Blob; mime: string } | null>(null);
  const [blobUrl, setBlobUrl] = useState<string | null>(null);
  const [retriesLeft, setRetriesLeft] = useState(maxRetries);
  const [submitting, setSubmitting] = useState(false);

  const mediaRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const autoStopRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const onStateChangeRef = useRef(onStateChange);
  useEffect(() => {
    onStateChangeRef.current = onStateChange;
  }, [onStateChange]);

  const onRecordedRef = useRef(onRecorded);
  useEffect(() => {
    onRecordedRef.current = onRecorded;
  }, [onRecorded]);

  // Manage Blob URL lifecycle safely
  useEffect(() => {
    if (pendingBlob) {
      const url = URL.createObjectURL(pendingBlob.blob);
      setBlobUrl(url);
      return () => {
        URL.revokeObjectURL(url);
      };
    } else {
      setBlobUrl(null);
    }
  }, [pendingBlob]);

  const stopInternal = useCallback(() => {
    if (autoStopRef.current) {
      clearTimeout(autoStopRef.current);
      autoStopRef.current = null;
    }
    if (mediaRef.current && mediaRef.current.state !== "inactive") {
      try {
        mediaRef.current.stop();
      } catch {
        /* ignore */
      }
    }
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }
    setRecording(false);
    setTime(0);
    onStateChangeRef.current?.(false);
  }, []);

  // Cleanup ON UNMOUNT ONLY
  useEffect(() => {
    return () => {
      if (autoStopRef.current) clearTimeout(autoStopRef.current);
      if (intervalRef.current) clearInterval(intervalRef.current);
      if (mediaRef.current && mediaRef.current.state !== "inactive") {
        try {
          mediaRef.current.stop();
        } catch {
          /* ignore */
        }
      }
    };
  }, []);

  async function start() {
    setError(null);
    setPendingBlob(null);
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mime = pickMimeType();
      const recorder = new MediaRecorder(stream, mime ? { mimeType: mime } : undefined);
      chunksRef.current = [];
      recorder.ondataavailable = (e) => {
        if (e.data && e.data.size > 0) chunksRef.current.push(e.data);
      };
      recorder.onstop = () => {
        stream.getTracks().forEach((t) => t.stop());
        const blob = new Blob(chunksRef.current, {
          type: recorder.mimeType || "audio/webm",
        });
        setRecording(false);
        setTime(0);
        if (intervalRef.current) {
          clearInterval(intervalRef.current);
          intervalRef.current = null;
        }
        if (autoStopRef.current) {
          clearTimeout(autoStopRef.current);
          autoStopRef.current = null;
        }
        onStateChangeRef.current?.(false);
        if (blob.size > 0) {
          setPendingBlob({ blob, mime: recorder.mimeType || "audio/webm" });
        }
      };
      // Record in 500ms slices so chunks are continuously generated
      recorder.start(500);
      mediaRef.current = recorder;
      setRecording(true);
      onStateChangeRef.current?.(true);
      setTime(0);
      intervalRef.current = setInterval(() => setTime((t) => t + 1), 1000);

      // Auto-stop after maxDuration
      autoStopRef.current = setTimeout(() => {
        if (mediaRef.current?.state === "recording") {
          mediaRef.current.stop();
        }
      }, maxDuration * 1000);
    } catch {
      setError("Microphone access was denied.");
    }
  }

  function stop() {
    stopInternal();
  }

  function handleReRecord() {
    setPendingBlob(null);
    setRetriesLeft((r) => r - 1);
    start();
  }

  async function handleSubmit() {
    if (!pendingBlob) return;
    setSubmitting(true);
    try {
      await onRecordedRef.current(pendingBlob.blob, pendingBlob.mime);
    } finally {
      setSubmitting(false);
    }
  }

  const remainingTime = maxDuration - time;

  return (
    <div className="flex flex-col items-center gap-3">
      {/* Recording / Idle button */}
      {!pendingBlob && !submitting && (
        <>
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
            {recording
              ? `Recording... ${time}s / ${maxDuration}s (${remainingTime}s left)`
              : "Tap to record your answer"}
          </p>
          {recording && remainingTime <= 10 && (
            <p className="text-xs font-semibold text-amber-600 animate-pulse">
              ⚠ Recording will auto-stop in {remainingTime}s
            </p>
          )}
        </>
      )}

      {/* Preview & confirm / re-record */}
      {pendingBlob && !submitting && (
        <div className="flex flex-col items-center gap-3 w-full">
          <div className="flex items-center gap-2 rounded-full bg-emerald-50 border border-emerald-200 px-4 py-1.5 text-sm font-medium text-emerald-700">
            <span>✓</span> Recording captured
          </div>
          <audio
            controls
            src={blobUrl || undefined}
            className="w-full max-w-sm h-10"
          />
          <div className="flex items-center gap-3">
            <button
              type="button"
              onClick={handleSubmit}
              className="rounded-lg bg-emerald-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-emerald-700 transition-colors"
            >
              Submit answer
            </button>
            {retriesLeft > 0 && (
              <button
                type="button"
                onClick={handleReRecord}
                className="rounded-lg border border-slate-300 bg-white px-5 py-2.5 text-sm font-medium text-slate-700 shadow-sm hover:bg-slate-50 transition-colors"
              >
                Re-record ({retriesLeft} left)
              </button>
            )}
          </div>
        </div>
      )}

      {/* Submitting state */}
      {submitting && (
        <div className="flex flex-col items-center gap-2">
          <div className="h-8 w-8 animate-spin rounded-full border-2 border-emerald-600 border-t-transparent" />
          <p className="text-sm text-slate-500">Evaluating your answer...</p>
        </div>
      )}

      {error && <p className="text-sm text-rose-600">{error}</p>}
    </div>
  );
}
