import Link from "next/link";
import type { ActivityEvent, LeaderboardEntry } from "@/lib/types";

const KIND_EMOJI: Record<ActivityEvent["kind"], string> = {
  speaking_evaluation: "🎙️",
  writing_submission: "✍️",
  writing_feedback: "💡",
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

export function LeaderboardPreview({
  week,
  activity,
}: {
  week: LeaderboardEntry[];
  activity: ActivityEvent[];
}) {
  const top = week.slice(0, 5);
  const recent = activity.slice(0, 4);

  return (
    <div className="grid gap-4 lg:grid-cols-2">
      <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
        <div className="flex items-center justify-between gap-2">
          <h3 className="text-lg font-bold text-slate-900">Top Students This Week</h3>
          <Link
            href="/community"
            className="shrink-0 text-sm font-semibold text-indigo-600 hover:text-indigo-700"
          >
            View full community →
          </Link>
        </div>
        {top.length === 0 ? (
          <p className="py-8 text-center text-sm text-slate-500">
            No activity yet this week — be the first to get on the board!
          </p>
        ) : (
          <ul className="mt-3 divide-y divide-slate-100">
            {top.map((e, i) => (
              <li key={e.user_id} className="flex items-center gap-3 py-2.5">
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
                <span className="shrink-0 rounded-full bg-indigo-50 px-2 py-0.5 text-xs font-bold text-indigo-700 border border-indigo-100">
                  {e.badge_count} 🏅
                </span>
                <span className="w-14 shrink-0 text-right text-sm font-bold text-slate-700">
                  {e.week_points} <span className="text-[10px] font-medium text-slate-400">pts</span>
                </span>
              </li>
            ))}
          </ul>
        )}
      </div>

      <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
        <h3 className="text-lg font-bold text-slate-900">Recent Activity</h3>
        {recent.length === 0 ? (
          <p className="py-8 text-center text-sm text-slate-500">No recent activity yet.</p>
        ) : (
          <ul className="mt-3 space-y-2.5">
            {recent.map((ev) => (
              <li key={ev.id} className="flex items-start gap-2.5">
                <span className="text-lg" aria-hidden>
                  {KIND_EMOJI[ev.kind]}
                </span>
                <div className="min-w-0 flex-1">
                  <p className="text-sm text-slate-700">
                    <Link
                      href={`/profile/${ev.actor_id}`}
                      className="font-semibold text-slate-900 hover:text-indigo-600"
                    >
                      {ev.actor_name}
                    </Link>{" "}
                    {ev.detail}
                  </p>
                  <p className="text-[11px] text-slate-400">{timeAgo(ev.created_at)}</p>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
