"use client";

import { useState } from "react";
import Link from "next/link";
import type { ActivityEvent, Community, LeaderboardEntry } from "@/lib/types";

type TabId = "week" | "all" | "improvers" | "activity";

const TABS: { id: TabId; label: string }[] = [
  { id: "week", label: "This Week" },
  { id: "all", label: "All Time" },
  { id: "improvers", label: "Improvers" },
  { id: "activity", label: "Activity" },
];

const KIND_META: Record<ActivityEvent["kind"], { emoji: string; label: string }> = {
  speaking_evaluation: { emoji: "🎙️", label: "Speaking" },
  writing_submission: { emoji: "✍️", label: "Writing" },
  writing_feedback: { emoji: "💡", label: "Feedback" },
};

function rankStyle(rank: number): string {
  if (rank === 1) return "bg-amber-100 text-amber-800 border-amber-200";
  if (rank === 2) return "bg-slate-200 text-slate-700 border-slate-300";
  if (rank === 3) return "bg-orange-100 text-orange-800 border-orange-200";
  return "bg-slate-100 text-slate-500 border-slate-200";
}

function timeAgo(iso: string): string {
  const diff = Date.now() - new Date(iso).getTime();
  const minutes = Math.floor(diff / 60000);
  if (minutes < 1) return "just now";
  if (minutes < 60) return `${minutes}m ago`;
  const hours = Math.floor(minutes / 60);
  if (hours < 24) return `${hours}h ago`;
  const days = Math.floor(hours / 24);
  if (days < 7) return `${days}d ago`;
  return new Date(iso).toLocaleDateString();
}

function LeaderboardTable({
  entries,
  pointsKey,
  showImprovement,
}: {
  entries: LeaderboardEntry[];
  pointsKey: "week_points" | "all_points";
  showImprovement?: boolean;
}) {
  if (entries.length === 0) {
    return <p className="py-8 text-center text-sm text-slate-500">No activity yet — be the first!</p>;
  }
  return (
    <ul className="divide-y divide-slate-100">
      {entries.map((e, i) => (
        <li key={e.user_id} className="flex items-center gap-3 py-3">
          <span
            className={`flex h-7 w-7 shrink-0 items-center justify-center rounded-full border text-xs font-bold ${rankStyle(i + 1)}`}
          >
            {i + 1}
          </span>
          <Link
            href={`/profile/${e.user_id}`}
            className="flex-1 truncate text-sm font-semibold text-slate-800 hover:text-indigo-600"
          >
            {e.name}
          </Link>
          {showImprovement && e.improvement !== null && e.improvement !== undefined && (
            <span
              className={`shrink-0 rounded-full px-2 py-0.5 text-xs font-bold ${
                e.improvement > 0
                  ? "bg-emerald-50 text-emerald-700 border border-emerald-200"
                  : "bg-slate-100 text-slate-500 border border-slate-200"
              }`}
            >
              {e.improvement > 0 ? `+${e.improvement}` : e.improvement}
            </span>
          )}
          <span className="shrink-0 rounded-full bg-indigo-50 px-2 py-0.5 text-xs font-bold text-indigo-700 border border-indigo-100">
            {e.badge_count} 🏅
          </span>
          <span className="w-16 shrink-0 text-right text-sm font-bold text-slate-700">
            {e[pointsKey]} <span className="text-[10px] font-medium text-slate-400">pts</span>
          </span>
          <span className="w-16 shrink-0 text-right text-sm font-semibold text-slate-500">
            {e.avg_band !== null ? `B${e.avg_band}` : "—"}
          </span>
        </li>
      ))}
    </ul>
  );
}

function ActivityFeed({ events }: { events: ActivityEvent[] }) {
  if (events.length === 0) {
    return <p className="py-8 text-center text-sm text-slate-500">No recent activity.</p>;
  }
  return (
    <ul className="space-y-2.5">
      {events.map((ev) => {
        const meta = KIND_META[ev.kind];
        return (
          <li
            key={ev.id}
            className="flex items-start gap-3 rounded-lg border border-slate-200 bg-white p-3.5"
          >
            <span className="text-xl" aria-hidden>
              {meta.emoji}
            </span>
            <div className="flex-1 min-w-0">
              <p className="text-sm text-slate-700">
                <Link
                  href={`/profile/${ev.actor_id}`}
                  className="font-semibold text-slate-900 hover:text-indigo-600"
                >
                  {ev.actor_name}
                </Link>{" "}
                {ev.detail}
              </p>
              <p className="mt-0.5 text-[11px] text-slate-400">
                {meta.label} · {timeAgo(ev.created_at)}
              </p>
            </div>
          </li>
        );
      })}
    </ul>
  );
}

export function CommunityTabs({ data }: { data: Community }) {
  const [tab, setTab] = useState<TabId>("week");

  return (
    <div>
      <div className="flex flex-wrap items-center gap-1.5">
        {TABS.map((t) => (
          <button
            key={t.id}
            type="button"
            onClick={() => setTab(t.id)}
            className={`rounded-full px-3.5 py-1.5 text-xs font-semibold transition-colors ${
              tab === t.id
                ? "bg-indigo-600 text-white shadow-sm"
                : "bg-slate-100 text-slate-600 hover:bg-slate-200"
            }`}
          >
            {t.label}
          </button>
        ))}
      </div>

      <div className="mt-4 rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
        {tab === "week" && <LeaderboardTable entries={data.week} pointsKey="week_points" />}
        {tab === "all" && <LeaderboardTable entries={data.all} pointsKey="all_points" />}
        {tab === "improvers" && (
          <LeaderboardTable entries={data.improvers} pointsKey="all_points" showImprovement />
        )}
        {tab === "activity" && <ActivityFeed events={data.activity} />}
      </div>

      {tab !== "activity" && (
        <p className="mt-3 text-xs text-slate-400">
          {tab === "week"
            ? "Points reset every Monday — everyone gets a fresh chance."
            : tab === "improvers"
              ? "Most improved average speaking band over the last 30 days."
              : "Lifetime points from speaking, writing and feedback."}
        </p>
      )}
    </div>
  );
}
