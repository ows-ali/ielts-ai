import { CommunityTabs } from "@/components/community/community-tabs";
import { Navbar } from "@/components/navbar";
import { api } from "@/lib/api";
import { getUserOrNull } from "@/lib/auth";
import type { Community } from "@/lib/types";

export const dynamic = "force-dynamic";

const EMPTY: Community = { week: [], all: [], improvers: [], activity: [] };

export default async function CommunityPage() {
  const { user, session } = await getUserOrNull();

  let data: Community = EMPTY;
  try {
    data = await api.community(session);
  } catch {
    data = EMPTY;
  }

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole={user?.role ?? null} userName={user?.name ?? null} />

      <main className="mx-auto max-w-4xl px-4 py-8 sm:px-6">
        <div className="mb-6 rounded-2xl bg-gradient-to-r from-indigo-900 via-indigo-850 to-slate-900 p-6 text-white shadow-xl shadow-indigo-950/10">
          <span className="rounded-full bg-indigo-500/20 px-3 py-1 text-xs font-semibold text-indigo-300 border border-indigo-500/30">
            COMMUNITY
          </span>
          <h1 className="mt-2 text-2xl font-bold tracking-tight sm:text-3xl">
            Leaderboards & Activity
          </h1>
          <p className="mt-1 text-sm text-indigo-200/80">
            Compete on the weekly board, chase the all-time greats, or cheer on the improvers.
            Every new practice gets you on the board.
          </p>
        </div>

        <CommunityTabs data={data} />
      </main>
    </div>
  );
}
