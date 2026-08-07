import { BadgeCard } from "@/components/badges/badge-card";
import type { Badge } from "@/lib/types";

export function BadgeGrid({
  badges,
  showLocked = true,
}: {
  badges: Badge[];
  showLocked?: boolean;
}) {
  const visible = showLocked ? badges : badges.filter((b) => b.earned);
  const speaking = visible.filter((b) => b.category === "speaking");
  const writing = visible.filter((b) => b.category === "writing");

  const renderSection = (title: string, items: Badge[]) => {
    if (items.length === 0) return null;
    return (
      <div>
        <h3 className="mb-3 text-xs font-bold uppercase tracking-wider text-slate-500">
          {title}
        </h3>
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-4">
          {items.map((b) => (
            <BadgeCard key={b.id} badge={b} />
          ))}
        </div>
      </div>
    );
  };

  return (
    <div className="space-y-6">
      {renderSection("Speaking", speaking)}
      {renderSection("Writing", writing)}
      {visible.length === 0 && (
        <p className="text-sm text-slate-500">No badges to show yet.</p>
      )}
    </div>
  );
}
