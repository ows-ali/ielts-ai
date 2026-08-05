"use client";

import { useEffect, useRef, useState } from "react";

import { Button } from "@/components/ui/button";
import { Spinner } from "@/components/ui/spinner";

function countWords(text: string): number {
  const trimmed = text.trim();
  if (!trimmed) return 0;
  return trimmed.split(/\s+/).length;
}

function countChars(text: string): number {
  return text.replace(/\s/g, "").length;
}

export function WritingEditor({
  questionId,
  onSubmit,
  submitting,
  disabled,
}: {
  questionId: string;
  onSubmit: (text: string) => void;
  submitting?: boolean;
  disabled?: boolean;
}) {
  const storageKey = `writing-draft-${questionId}`;
  const [text, setText] = useState("");
  const [saved, setSaved] = useState(false);
  const [touched, setTouched] = useState(false);
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    try {
      const savedDraft = localStorage.getItem(storageKey);
      if (savedDraft) setText(savedDraft);
    } catch {
      /* ignore */
    }
  }, [storageKey]);

  useEffect(() => {
    if (!touched) return;
    if (timer.current) clearTimeout(timer.current);
    timer.current = setTimeout(() => {
      try {
        localStorage.setItem(storageKey, text);
        setSaved(true);
      } catch {
        /* ignore */
      }
    }, 500);
    return () => {
      if (timer.current) clearTimeout(timer.current);
    };
  }, [text, touched, storageKey]);

  const words = countWords(text);
  const chars = countChars(text);
  const meetTarget = words >= 150 && chars >= 150;
  const wordTone =
    words >= 150 ? "text-emerald-600" : words >= 100 ? "text-amber-600" : "text-slate-500";

  return (
    <div className="space-y-3">
      <div className="flex items-center justify-between gap-2">
        <div className="flex items-center gap-3 text-sm">
          <span className={`font-bold ${wordTone}`}>{words} words</span>
          <span className="text-slate-400">{chars} characters</span>
          {!meetTarget && (
            <span className="rounded-full bg-amber-100 px-2 py-0.5 text-xs font-semibold text-amber-700">
              IELTS Task 1 requires at least 150 words
            </span>
          )}
        </div>
        <span className="text-xs text-slate-400">
          {saved ? "Draft saved ✓" : touched ? "Saving…" : "Autosave on"}
        </span>
      </div>

      <textarea
        value={text}
        onChange={(e) => {
          setText(e.target.value);
          setTouched(true);
          setSaved(false);
        }}
        disabled={disabled}
        placeholder="Write your answer here. Your draft is saved automatically in your browser."
        rows={14}
        className="w-full rounded-xl border border-slate-300 bg-white p-4 font-mono text-[15px] leading-relaxed text-slate-800 shadow-sm outline-none transition-colors focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 disabled:opacity-60"
      />

      <div className="flex items-center justify-end gap-3">
        <Button
          variant="secondary"
          onClick={() => {
            setText("");
            setTouched(true);
            try {
              localStorage.removeItem(storageKey);
            } catch {
              /* ignore */
            }
          }}
          disabled={disabled || !text}
        >
          Clear draft
        </Button>
        <Button
          onClick={() => onSubmit(text)}
          disabled={disabled || !text.trim() || submitting}
        >
          {submitting ? <Spinner className="h-4 w-4" /> : null}
          {submitting ? "Submitting…" : "Submit for teacher feedback"}
        </Button>
      </div>
    </div>
  );
}
