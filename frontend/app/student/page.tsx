import Link from "next/link";

import { JoinRoomForm } from "@/components/student/join-room-form";
import { Navbar } from "@/components/navbar";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { api } from "@/lib/api";
import { requireStudent } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function StudentPage() {
  const { user, session } = await requireStudent();

  let attempts: Awaited<ReturnType<typeof api.studentReport>>["attempts"] = [];
  try {
    const report = await api.studentReport(session);
    attempts = report.attempts || [];
  } catch {
    attempts = [];
  }

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole="student" userName={user.name} />

      <main className="mx-auto max-w-3xl px-4 py-8 sm:px-6">
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
                Join your teacher's practice session or review your speaking feedback history below.
              </p>
            </div>
          </div>
        </div>

      <div className="mt-6 grid gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Join a session</CardTitle>
          </CardHeader>
          <CardContent>
            <JoinRoomForm session={session} />
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between">
            <CardTitle>Practice History ({attempts.length})</CardTitle>
            <Link href="/student/report">
              <Button variant="secondary">
                Full Progress Report
              </Button>
            </Link>
          </CardHeader>
          <CardContent>
            {attempts.length === 0 ? (
              <p className="text-sm text-slate-500">
                No past sessions found. Enter a room code above to join a practice room!
              </p>
            ) : (
              <ul className="space-y-3">
                {attempts.slice(0, 5).map((a) => (
                  <li key={a.id} className="rounded-lg border border-slate-200 p-4 space-y-2">
                    <div className="flex items-center justify-between">
                      <p className="font-medium text-slate-900">{a.question}</p>
                      <span className="text-sm font-semibold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                        {a.overall_band !== null ? `Band ${a.overall_band}` : "—"}
                      </span>
                    </div>
                    {a.audio_url && (
                      <div className="pt-1">
                        <audio controls src={a.audio_url} className="w-full h-9" />
                      </div>
                    )}
                    <p className="text-xs text-slate-400">
                      {a.title ? `${a.title} · ` : ""}
                      {a.room_code ? `Code: ${a.room_code} · ` : ""}
                      {a.created_at ? new Date(a.created_at).toLocaleString() : ""}
                    </p>
                  </li>
                ))}
              </ul>
            )}
          </CardContent>
        </Card>
      </div>
      </main>
    </div>
  );
}
