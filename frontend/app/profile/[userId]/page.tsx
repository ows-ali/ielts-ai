import Link from "next/link";
import { notFound } from "next/navigation";

import { BadgeGrid } from "@/components/badges/badge-grid";
import { ProfileSummary } from "@/components/badges/profile-summary";
import { Navbar } from "@/components/navbar";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { api } from "@/lib/api";
import { getUserOrNull } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function PublicProfilePage({
  params,
}: {
  params: Promise<{ userId: string }>;
}) {
  const { userId } = await params;
  const { session, user } = await getUserOrNull();

  let profile;
  try {
    profile = await api.publicProfile(session, userId);
  } catch {
    notFound();
  }

  const isSelf = !!user && profile.id === user.id;

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole={user?.role ?? null} userName={user?.name ?? null} />

      <main className="mx-auto max-w-4xl px-4 py-8 sm:px-6">
        <div className="mb-6 rounded-2xl bg-gradient-to-r from-indigo-900 via-indigo-850 to-slate-900 p-6 text-white shadow-xl shadow-indigo-950/10">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-2xl font-bold tracking-tight sm:text-3xl">
                  {profile.name}
                </h1>
                {isSelf && (
                  <span className="rounded-full bg-emerald-500/20 px-2.5 py-0.5 text-xs font-bold text-emerald-300 border border-emerald-500/30">
                    You
                  </span>
                )}
              </div>
              <p className="mt-1 text-sm text-indigo-200/80">
                {profile.role === "teacher" ? "Teacher" : "Student"} · Joined{" "}
                {profile.created_at
                  ? new Date(profile.created_at).toLocaleDateString()
                  : "—"}
              </p>
            </div>
            <div className="rounded-xl bg-white/10 px-4 py-3 text-center backdrop-blur-md border border-white/15">
              <p className="text-2xl font-extrabold">
                {profile.earned_count}
                <span className="text-base font-semibold text-indigo-300">/{profile.total_count}</span>
              </p>
              <p className="text-xs font-semibold text-indigo-200/90">Badges earned</p>
            </div>
          </div>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Overview</CardTitle>
          </CardHeader>
          <CardContent>
            <ProfileSummary stats={profile.stats} />
          </CardContent>
        </Card>

        <Card className="mt-6">
          <CardHeader>
            <CardTitle>Achievement Badges</CardTitle>
          </CardHeader>
          <CardContent>
            <BadgeGrid badges={profile.badges} showLocked={false} />
          </CardContent>
        </Card>

        {isSelf && (
          <div className="mt-6 text-center">
            <Link href="/student">
              <Button variant="secondary">← Back to Dashboard</Button>
            </Link>
          </div>
        )}
      </main>
    </div>
  );
}
