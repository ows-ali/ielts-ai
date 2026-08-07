import { GuideHub } from "@/components/guide/guide-hub";
import { Navbar } from "@/components/navbar";
import { api } from "@/lib/api";
import { requireStudent } from "@/lib/auth";
import { currentBandFor, guideTopics } from "@/lib/guide";
import type { BandInfo, GuideTopicId } from "@/lib/guide";

export const dynamic = "force-dynamic";

export default async function GuidePage() {
  const { user, session } = await requireStudent();

  let stats = null;
  try {
    const badges = await api.myBadges(session);
    stats = badges.stats;
  } catch {
    stats = null;
  }

  const bandInfo = Object.fromEntries(
    guideTopics.map((t) => [t.id, currentBandFor(t.id, stats)]),
  ) as Record<GuideTopicId, BandInfo>;

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole="student" userName={user.name} />
      <main className="mx-auto max-w-4xl px-4 py-8 sm:px-6">
        <div className="mb-6 rounded-2xl bg-gradient-to-r from-indigo-950 via-slate-900 to-indigo-900 p-6 text-white shadow-xl shadow-indigo-950/10">
          <span className="rounded-full bg-indigo-500/20 px-3 py-1 text-xs font-semibold text-indigo-300 border border-indigo-500/30">
            IELTS GUIDE
          </span>
          <h1 className="mt-2 text-2xl font-bold tracking-tight sm:text-3xl">
            How to attempt IELTS
          </h1>
          <p className="mt-1 text-sm text-indigo-200/80">
            Learn the structure and requirements of each section, how the bands are scored, and
            what to focus on to move from your current band to Band 8.
          </p>
        </div>

        <GuideHub topics={guideTopics} bandInfo={bandInfo} />
      </main>
    </div>
  );
}
