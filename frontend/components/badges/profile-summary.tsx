import type { ProfileStats } from "@/lib/types";

const PART_LABELS: Record<number, string> = {
  1: "Part 1",
  2: "Part 2",
  3: "Part 3",
};

export function ProfileSummary({ stats }: { stats: ProfileStats }) {
  const items = [
    { label: "Speaking attempts", value: String(stats.total_speaking_attempts) },
    { label: "Avg speaking band", value: stats.avg_speaking_band ?? "—" },
    { label: "Best speaking band", value: stats.best_speaking_band ?? "—" },
    { label: "Writing submissions", value: String(stats.writing_submissions) },
    { label: "Feedback received", value: String(stats.writing_feedback_count) },
    { label: "Best writing band", value: stats.best_writing_band ?? "—" },
  ];

  return (
    <div className="space-y-4">
      <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
        {items.map((item) => (
          <div key={item.label} className="rounded-lg bg-slate-50 p-3 text-center">
            <p className="text-xl font-bold text-slate-900">{item.value}</p>
            <p className="mt-0.5 text-[11px] text-slate-500">{item.label}</p>
          </div>
        ))}
      </div>

      <div className="grid gap-3 sm:grid-cols-2">
        <div className="rounded-lg border border-slate-200 p-4">
          <p className="text-xs font-bold uppercase tracking-wider text-slate-500">
            Speaking parts covered
          </p>
          <div className="mt-2 flex flex-wrap gap-1.5">
            {stats.speaking_parts.length === 0 ? (
              <span className="text-sm text-slate-400">None yet</span>
            ) : (
              stats.speaking_parts.map((p) => (
                <span
                  key={p}
                  className="rounded-full bg-indigo-50 px-2.5 py-1 text-xs font-semibold text-indigo-700 border border-indigo-100"
                >
                  {PART_LABELS[p] ?? `Part ${p}`}
                </span>
              ))
            )}
          </div>
        </div>
        <div className="rounded-lg border border-slate-200 p-4">
          <p className="text-xs font-bold uppercase tracking-wider text-slate-500">
            Writing task coverage
          </p>
          <p className="mt-2 text-sm text-slate-700">
            Task 1: <span className="font-semibold">{stats.task1_types_done.length}/7 types</span>
          </p>
          <p className="mt-1 text-sm text-slate-700">
            Task 2: <span className="font-semibold">{stats.task2_types_done.length}/6 types</span>
          </p>
        </div>
      </div>
    </div>
  );
}
