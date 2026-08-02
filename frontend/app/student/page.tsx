import Link from "next/link";

import { JoinRoomForm } from "@/components/student/join-room-form";
import { SignOutButton } from "@/components/sign-out-button";
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
    <main className="mx-auto max-w-2xl p-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">Student Dashboard</h1>
          <p className="text-sm text-slate-500">Welcome, {user.name}</p>
        </div>
        <SignOutButton />
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
  );
}
