"use client";

import type { WritingFeedback } from "@/lib/types";

const CRITERIA: { key: keyof WritingFeedback; label: string }[] = [
  { key: "task_achievement", label: "Task Achievement" },
  { key: "coherence_cohesion", label: "Coherence & Cohesion" },
  { key: "lexical_resource", label: "Lexical Resource" },
  { key: "grammatical_range", label: "Grammar" },
];

export function FeedbackCard({ feedback }: { feedback: WritingFeedback }) {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
      <div className="flex items-center justify-between gap-3">
        <div className="flex items-center gap-2">
          <span className="flex h-8 w-8 items-center justify-center rounded-full bg-indigo-100 text-sm font-bold text-indigo-700">
            {feedback.teacher_name?.[0]?.toUpperCase() ?? "T"}
          </span>
          <div>
            <p className="text-sm font-semibold text-slate-800">
              {feedback.teacher_name ?? "Teacher"}
            </p>
            <p className="text-xs text-slate-400">
              {feedback.created_at ? new Date(feedback.created_at).toLocaleString() : ""}
            </p>
          </div>
        </div>
        <span className="rounded-full bg-emerald-50 px-3 py-1 text-sm font-bold text-emerald-700 border border-emerald-200">
          Band {feedback.overall_band}
        </span>
      </div>

      <div className="mt-4 grid grid-cols-2 gap-2 sm:grid-cols-4">
        {CRITERIA.map((c) => (
          <div key={c.key} className="rounded-lg border border-slate-200 bg-slate-50 p-2.5 text-center">
            <p className="text-lg font-bold text-slate-800">{feedback[c.key]}</p>
            <p className="text-[11px] text-slate-500">{c.label}</p>
          </div>
        ))}
      </div>

      {feedback.overall_comment && (
        <div className="mt-4 rounded-lg bg-indigo-50/60 p-3">
          <p className="mb-1 text-xs font-bold uppercase tracking-wide text-indigo-700">Teacher comment</p>
          <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
            {feedback.overall_comment}
          </p>
        </div>
      )}
    </div>
  );
}
