"use client";

import { useState } from "react";

import type { WritingSample } from "@/lib/types";

const CRITERIA: { key: keyof Omit<WritingSample, "id" | "band" | "answer_text" | "explanation" | "improvement_tips">; label: string }[] = [
  { key: "task_achievement", label: "Task Achievement" },
  { key: "coherence_cohesion", label: "Coherence & Cohesion" },
  { key: "lexical_resource", label: "Lexical Resource" },
  { key: "grammatical_range", label: "Grammatical Range & Accuracy" },
];

export function BandSampleCard({ sample, defaultOpen = false }: { sample: WritingSample; defaultOpen?: boolean }) {
  const [open, setOpen] = useState(defaultOpen);

  const bandTone =
    sample.band >= 8
      ? "bg-emerald-600 text-white"
      : sample.band >= 6
        ? "bg-indigo-600 text-white"
        : "bg-amber-500 text-white";

  return (
    <div className="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        className="flex w-full items-center justify-between gap-3 px-4 py-3 text-left transition-colors hover:bg-slate-50"
      >
        <div className="flex items-center gap-3">
          <span className={`flex h-9 w-9 items-center justify-center rounded-lg text-sm font-bold ${bandTone}`}>
            {sample.band}
          </span>
          <div>
            <p className="text-sm font-semibold text-slate-800">Model answer — Band {sample.band}</p>
            <p className="text-xs text-slate-500">
              Why it is Band {sample.band} · {sample.answer_text.split(/\s+/).length} words
            </p>
          </div>
        </div>
        <svg
          className={`h-4 w-4 shrink-0 text-slate-400 transition-transform ${open ? "rotate-180" : ""}`}
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path fillRule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clipRule="evenodd" />
        </svg>
      </button>

      {open && (
        <div className="space-y-4 border-t border-slate-100 px-4 py-4">
          <div className="rounded-lg bg-slate-50 p-4">
            <p className="whitespace-pre-wrap text-[15px] leading-relaxed text-slate-800">
              {sample.answer_text}
            </p>
          </div>

          <div className="grid grid-cols-2 gap-2 sm:grid-cols-4">
            {CRITERIA.map((c) => (
              <div key={c.key} className="rounded-lg border border-slate-200 bg-white p-2.5 text-center">
                <p className="text-lg font-bold text-slate-800">{sample[c.key]}</p>
                <p className="text-[11px] text-slate-500">{c.label}</p>
              </div>
            ))}
          </div>

          <div>
            <p className="mb-1 text-xs font-bold uppercase tracking-wide text-slate-500">
              Why this is Band {sample.band}
            </p>
            <p className="text-sm leading-relaxed text-slate-700">{sample.explanation}</p>
          </div>

          {sample.improvement_tips.length > 0 && (
            <div className="rounded-lg bg-amber-50 p-3">
              <p className="mb-1 text-xs font-bold uppercase tracking-wide text-amber-700">
                How this answer could improve
              </p>
              <ul className="list-disc pl-4 text-sm text-amber-800">
                {sample.improvement_tips.map((tip, i) => (
                  <li key={i}>{tip}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
