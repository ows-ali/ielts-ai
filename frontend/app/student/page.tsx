import Link from "next/link";

import { BadgeGrid } from "@/components/badges/badge-grid";
import { Navbar } from "@/components/navbar";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { api } from "@/lib/api";
import { requireStudent } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function StudentPage() {
  const { user, session } = await requireStudent();

  let badges;
  try {
    badges = await api.myBadges(session);
  } catch {
    badges = null;
  }

  const earned = badges ? badges.badges.filter((b) => b.earned) : [];

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole="student" userName={user.name} />

      <main className="mx-auto max-w-4xl px-4 py-8 sm:px-6">
        <div className="mb-6 rounded-2xl bg-gradient-to-r from-indigo-900 via-indigo-850 to-slate-900 p-6 text-white shadow-xl shadow-indigo-950/10">
          <div className="flex items-center justify-between">
            <div>
              <span className="rounded-full bg-indigo-500/20 px-3 py-1 text-xs font-semibold text-indigo-300 border border-indigo-500/30">
                STUDENT DASHBOARD
              </span>
              <h1 className="mt-2 text-2xl font-bold tracking-tight sm:text-3xl">
                Welcome back, {user.name} 👋
              </h1>
              <p className="mt-1 text-sm text-indigo-200/80">
                {badges
                  ? `You've earned ${badges.earned_count} of ${badges.total_count} badges. Keep going!`
                  : "Practice speaking and writing, then watch your badges grow."}
              </p>
            </div>
            {badges && badges.earned_count > 0 && (
              <div className="hidden sm:block shrink-0 rounded-xl bg-white/10 px-4 py-3 text-center backdrop-blur-md border border-white/15">
                <p className="text-2xl font-extrabold">{badges.earned_count}</p>
                <p className="text-xs font-semibold text-indigo-200/90">Badges</p>
              </div>
            )}
          </div>
        </div>

        <div className="mt-6 grid gap-4 sm:grid-cols-2">
          <Link
            href="/student/speaking"
            className="group rounded-2xl border border-slate-200 bg-white p-5 shadow-sm transition-all hover:-translate-y-0.5 hover:border-indigo-400 hover:shadow-md"
          >
            <div className="flex items-center gap-3">
              <span className="flex h-11 w-11 items-center justify-center rounded-xl bg-indigo-50 text-xl">
                🎙️
              </span>
              <h2 className="text-lg font-bold text-slate-900 group-hover:text-indigo-700">
                Speaking
              </h2>
            </div>
            <p className="mt-2 text-sm text-slate-500">
              Join live practice rooms, answer Part 1–3 questions, and get instant AI feedback.
            </p>
            <p className="mt-3 text-sm font-semibold text-indigo-600 group-hover:text-indigo-700">
              Open Speaking →
            </p>
          </Link>

          <Link
            href="/student/writing"
            className="group rounded-2xl border border-slate-200 bg-white p-5 shadow-sm transition-all hover:-translate-y-0.5 hover:border-indigo-400 hover:shadow-md"
          >
            <div className="flex items-center gap-3">
              <span className="flex h-11 w-11 items-center justify-center rounded-xl bg-emerald-50 text-xl">
                ✍️
              </span>
              <h2 className="text-lg font-bold text-slate-900 group-hover:text-indigo-700">
                Writing
              </h2>
            </div>
            <p className="mt-2 text-sm text-slate-500">
              Practice Task 1 and Task 2 essays, read model answers, and get teacher feedback.
            </p>
            <p className="mt-3 text-sm font-semibold text-indigo-600 group-hover:text-indigo-700">
              Open Writing →
            </p>
          </Link>
        </div>

        <Card className="mt-6">
          <CardHeader className="flex flex-row items-center justify-between">
            <CardTitle>My Badges</CardTitle>
            <div className="flex gap-2">
              <Link href="/community">
                <Button variant="secondary">Community</Button>
              </Link>
              <Link href="/profile">
                <Button variant="secondary">Full Profile</Button>
              </Link>
            </div>
          </CardHeader>
          <CardContent>
            {badges ? (
              <BadgeGrid badges={earned.length > 0 ? earned : badges.badges} />
            ) : (
              <p className="text-sm text-slate-500">
                Could not load badges right now. Try again later.
              </p>
            )}
          </CardContent>
        </Card>

        <div className="mt-6 rounded-2xl border border-slate-200 bg-white p-5 text-center shadow-sm">
          <h2 className="text-lg font-bold text-slate-900">Want detailed feedback?</h2>
          <p className="mt-1 text-sm text-slate-500">
            Review every speaking attempt with sub-scores, transcripts and improvement tips.
          </p>
          <div className="mt-4">
            <Link href="/student/report">
              <Button>View My Progress Report</Button>
            </Link>
          </div>
        </div>
      </main>
    </div>
  );
}
