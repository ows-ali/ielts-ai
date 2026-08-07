import type { Badge } from "@/lib/types";

export function BadgeCard({ badge }: { badge: Badge }) {
  const pct = badge.progress
    ? Math.min(100, Math.round((badge.progress.current / badge.progress.target) * 100))
    : 0;

  return (
    <div
      data-earned={badge.earned}
      title={badge.description}
      className={`relative rounded-xl border p-4 text-center transition-all ${
        badge.earned
          ? "border-amber-200 bg-gradient-to-b from-amber-50/70 to-white shadow-sm hover:shadow-md"
          : "border-slate-200 bg-slate-50/70 hover:bg-slate-100"
      }`}
    >
      <div className="text-3xl" aria-hidden>
        {badge.earned ? badge.emoji : "🔒"}
      </div>
      <p className={`mt-2 text-sm font-bold ${badge.earned ? "text-slate-800" : "text-slate-500"}`}>
        {badge.name}
      </p>
      <p className="mt-1 text-[11px] leading-snug text-slate-500">{badge.description}</p>
      {badge.progress && (
        <div className="mt-2">
          <div className="h-1.5 w-full overflow-hidden rounded-full bg-slate-200">
            <div
              className="h-full rounded-full bg-indigo-500 transition-all"
              style={{ width: `${pct}%` }}
            />
          </div>
          <p className="mt-1 text-[10px] font-semibold text-slate-400">
            {badge.progress.current}/{badge.progress.target}
          </p>
        </div>
      )}
    </div>
  );
}
