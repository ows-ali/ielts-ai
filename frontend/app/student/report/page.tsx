import Link from "next/link";

import { Navbar } from "@/components/navbar";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { api } from "@/lib/api";
import { requireStudent } from "@/lib/auth";

export const dynamic = "force-dynamic";

const BAND_LABELS: Record<number, string> = {
  1: "Band 1",
  2: "Band 2",
  3: "Band 3",
  4: "Band 4",
  5: "Band 5",
  6: "Band 6",
  7: "Band 7",
  8: "Band 8",
  9: "Band 9",
};

function ScoreBadge({ band, label }: { band: number | null | undefined; label: string }) {
  return (
    <div className="rounded-lg bg-slate-50 p-3 text-center">
      <p className="text-xl font-bold text-slate-900">{band ?? "—"}</p>
      <p className="text-xs text-slate-500">{label}</p>
    </div>
  );
}

export default async function StudentReportPage() {
  const { user, session } = await requireStudent();
  let report;
  try {
    report = await api.studentReport(session);
  } catch {
    report = { student_id: user.id, attempts: [] };
  }

  const latest = report.attempts[0];

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole="student" userName={user.name} />

      <main className="mx-auto max-w-3xl px-4 py-8 sm:px-6">
        <div className="mb-6 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-slate-900 tracking-tight sm:text-3xl">My Progress & Feedback</h1>
            <p className="text-sm text-slate-500">Comprehensive evaluation analysis for {user.name}</p>
          </div>
          <Link href="/student">
            <Button variant="secondary" className="shadow-sm">← Back to Dashboard</Button>
          </Link>
        </div>

      {latest && (
        <Card className="mt-6 border-emerald-200">
          <CardHeader>
            <CardTitle>
              Latest attempt:{" "}
              {BAND_LABELS[Math.round(latest.overall_band ?? 0)] ??
                `Band ${latest.overall_band}`}
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-4 gap-3 text-center">
              {(
                [
                  ["Fluency", latest.fluency],
                  ["Grammar", latest.grammar],
                  ["Vocabulary", latest.vocabulary],
                  ["Pronunciation", latest.pronunciation],
                ] as const
              ).map(([label, value]) => (
                <ScoreBadge key={label} band={value} label={label} />
              ))}
            </div>
            {latest.audio_url && (
              <div className="mt-4">
                <p className="mb-1 text-xs font-medium text-slate-500">Recorded Audio:</p>
                <audio controls src={latest.audio_url} className="w-full h-10" />
              </div>
            )}
            {latest.feedback && latest.feedback.length > 0 && (
              <div className="mt-4 rounded-lg bg-amber-50 p-4">
                <p className="text-sm font-semibold text-amber-800">Improve:</p>
                <ul className="mt-1 list-disc pl-5 text-sm text-amber-700">
                  {latest.feedback.map((tip, i) => (
                    <li key={i}>{tip}</li>
                  ))}
                </ul>
              </div>
            )}
          </CardContent>
        </Card>
      )}

      <Card className="mt-6">
        <CardHeader>
          <CardTitle>History ({report.attempts.length})</CardTitle>
        </CardHeader>
        <CardContent>
          {report.attempts.length === 0 ? (
            <p className="text-sm text-slate-500">
              No attempts yet. Join a room and practice speaking!
            </p>
          ) : (
            <ul className="space-y-3">
              {report.attempts.map((a) => (
                <li
                  key={a.id}
                  className="rounded-lg border border-slate-200 p-4"
                >
                  <div className="flex items-center justify-between">
                    <p className="font-medium">{a.question}</p>
                    <span className="text-sm font-semibold text-emerald-700">
                      {a.overall_band !== null ? `Band ${a.overall_band}` : "—"}
                    </span>
                  </div>
                  {a.transcript && (
                    <p className="mt-1 line-clamp-2 text-sm text-slate-500">
                      &ldquo;{a.transcript}&rdquo;
                    </p>
                  )}
                  {a.audio_url && (
                    <div className="mt-3">
                      <audio controls src={a.audio_url} className="w-full h-9" />
                    </div>
                  )}
                  <p className="mt-2 text-xs text-slate-400">
                    {a.title ? `${a.title} · ` : ""}
                    {a.created_at ? new Date(a.created_at).toLocaleString() : ""}
                  </p>
                </li>
              ))}
            </ul>
          )}
        </CardContent>
      </Card>
      </main>
    </div>
  );
}
