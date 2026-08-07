"use client";

import { useState } from "react";

import { GuideTopicView } from "@/components/guide/guide-topic-view";
import type { BandInfo, GuideTopic, GuideTopicId } from "@/lib/guide";

const SKILL_LABELS: Record<GuideTopicId, string> = {
  speaking: "Speaking",
  "writing-task1": "Writing",
  "writing-task2": "Writing",
  scoring: "Overall IELTS",
};

export function ContextualGuide({
  topic,
  bandInfo,
  title,
}: {
  topic: GuideTopic;
  bandInfo: BandInfo;
  title: string;
}) {
  const [open, setOpen] = useState(false);

  return (
    <div className="overflow-hidden rounded-xl border border-indigo-200 bg-white shadow-sm">
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        className="flex w-full items-center justify-between gap-3 px-4 py-3 text-left transition-colors hover:bg-indigo-50/40"
      >
        <div className="flex items-center gap-3">
          <span className="flex h-9 w-9 items-center justify-center rounded-lg bg-indigo-100 text-lg">
            {topic.emoji}
          </span>
          <div>
            <p className="text-sm font-semibold text-slate-800">{title}</p>
            <p className="text-xs text-slate-500">
              Structure · how to attempt · scoring · band-specific tips
            </p>
          </div>
        </div>
        <svg
          className={`h-4 w-4 shrink-0 text-slate-400 transition-transform ${open ? "rotate-180" : ""}`}
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fillRule="evenodd"
            d="M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
            clipRule="evenodd"
          />
        </svg>
      </button>

      {open && (
        <div className="space-y-6 border-t border-indigo-100 bg-slate-50/50 px-4 py-4 sm:px-5">
          <GuideTopicView topic={topic} bandInfo={bandInfo} skillLabel={SKILL_LABELS[topic.id]} />
        </div>
      )}
    </div>
  );
}
