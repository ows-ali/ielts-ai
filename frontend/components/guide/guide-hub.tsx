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

export function GuideHub({
  topics,
  bandInfo,
}: {
  topics: GuideTopic[];
  bandInfo: Record<GuideTopicId, BandInfo>;
}) {
  const [tab, setTab] = useState<GuideTopicId>(topics[0].id);
  const active = topics.find((t) => t.id === tab) ?? topics[0];

  return (
    <div>
      <div className="flex flex-wrap items-center gap-1.5">
        {topics.map((t) => (
          <button
            key={t.id}
            type="button"
            onClick={() => setTab(t.id)}
            aria-pressed={tab === t.id}
            className={`rounded-full px-3.5 py-1.5 text-xs font-semibold transition-colors ${
              tab === t.id
                ? "bg-indigo-600 text-white shadow-sm"
                : "bg-slate-100 text-slate-600 hover:bg-slate-200"
            }`}
          >
            {t.emoji} {t.label}
          </button>
        ))}
      </div>

      <div className="mt-4 rounded-xl border border-slate-200 bg-white p-4 shadow-sm sm:p-5">
        <h2 className="text-lg font-bold text-slate-900">
          {active.emoji} {active.label}
        </h2>
        <div className="mt-4">
          <GuideTopicView
            topic={active}
            bandInfo={bandInfo[active.id]}
            skillLabel={SKILL_LABELS[active.id]}
          />
        </div>
      </div>
    </div>
  );
}
