"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import type { Session } from "@supabase/supabase-js";

import { AudioRecorder } from "@/components/student/audio-recorder";
import { Navbar } from "@/components/navbar";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Spinner } from "@/components/ui/spinner";
import { api } from "@/lib/api";
import { createClient } from "@/lib/supabase/client";
import { useUnauthorizedRedirect } from "@/lib/use-unauthorized";
import type { ClassReport, Evaluation, TurnState } from "@/lib/types";

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

export function StudentSpeakingSession({
  session,
  roomId,
  userId,
}: {
  session: Session;
  roomId: string;
  userId: string;
}) {
  const router = useRouter();
  const [turn, setTurn] = useState<TurnState | null>(null);
  const [evaluation, setEvaluation] = useState<Evaluation | null>(null);
  const [classReport, setClassReport] = useState<ClassReport | null>(null);
  const [error, setError] = useState<string | null>(null);
  const alreadyEvaluatedRef = useRef<string | null>(null);
  const busyRef = useRef(false);

  const handleUnauthorized = useUnauthorizedRedirect();

  const refresh = useCallback(async () => {
    try {
      const t = await api.turn(session, roomId);
      setTurn(t);
    } catch (err) {
      await handleUnauthorized(err);
    }
  }, [session, roomId, handleUnauthorized]);

  useEffect(() => {
    let mounted = true;
    async function doRefresh() {
      try {
        const t = await api.turn(session, roomId);
        if (mounted) setTurn(t);
      } catch (err) {
        if (mounted) await handleUnauthorized(err);
      }
    }

    doRefresh();

    const interval = setInterval(() => {
      if (!busyRef.current) doRefresh();
    }, 2000);

    const supabase = createClient();
    if (session?.access_token && typeof supabase.auth?.setSession === "function") {
      supabase.auth.setSession({
        access_token: session.access_token,
        refresh_token: session.refresh_token || "",
      }).catch(() => {});
    }

    const channel = supabase
      .channel(`student-room-${roomId}`)
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "rooms", filter: `id=eq.${roomId}` },
        () => {
          if (!busyRef.current) doRefresh();
        }
      )
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "participants", filter: `room_id=eq.${roomId}` },
        () => {
          if (!busyRef.current) doRefresh();
        }
      )
      .subscribe();

    return () => {
      mounted = false;
      clearInterval(interval);
      supabase.removeChannel(channel);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [roomId]);

  useEffect(() => {
    if (turn?.status === "ended") {
      api.classReport(session, roomId).then(setClassReport).catch(() => {});
    }
  }, [turn?.status, session, roomId]);

  async function handleRecorded(blob: Blob, mimeType: string) {
    busyRef.current = true;
    setError(null);
    try {
      const supabase = createClient();
      if (session?.access_token) {
        await supabase.auth.setSession({
          access_token: session.access_token,
          refresh_token: session.refresh_token || "",
        });
      }
      const path = `${roomId}/${userId}/${Date.now()}.webm`;
      const { error: uploadError } = await supabase.storage
        .from("audio")
        .upload(path, blob, { contentType: mimeType, upsert: true });
      if (uploadError) {
        throw new Error(`Upload failed: ${uploadError.message}`);
      }
      const { data } = supabase.storage.from("audio").getPublicUrl(path);
      if (!data?.publicUrl) throw new Error("Could not build audio URL");

      if (turn?.question_id) {
        alreadyEvaluatedRef.current = turn.question_id;
        const result = await api.submitAnswer(
          session,
          roomId,
          turn.question_id,
          data.publicUrl
        );
        setEvaluation(result);
        await refresh();
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to submit answer");
    } finally {
      busyRef.current = false;
    }
  }

  if (turn === null) {
    return (
      <main className="flex min-h-screen items-center justify-center">
        <Spinner className="h-8 w-8" />
      </main>
    );
  }

  if (turn.status === "ended") {
    return (
      <div className="min-h-screen bg-slate-50/50">
        <Navbar userRole="student" />
        <main className="mx-auto max-w-xl px-4 py-8 space-y-6">
          <Card className="shadow-sm">
            <CardContent className="p-8 text-center">
              <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-emerald-100 text-emerald-600 mb-3">
                <span className="font-bold text-lg">✓</span>
              </div>
              <h1 className="text-xl font-bold text-slate-900">Session ended</h1>
              <p className="mt-2 text-sm text-slate-500">
                Thanks for practicing! Check the class performance below or view your full report.
              </p>
              <Button className="mt-4 shadow-sm" onClick={() => router.push("/student/report")}>
                View my progress report
              </Button>
            </CardContent>
          </Card>

          {classReport && (
            <Card className="shadow-sm">
              <CardHeader>
                <CardTitle>Class Results</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-lg font-bold text-slate-800">
                  Average band score: {classReport.average_band ?? "—"}
                </p>
                <ul className="mt-4 space-y-2">
                  {classReport.participants.map((p) => (
                    <li
                      key={p.student_id}
                      className="flex items-center justify-between rounded-lg border border-slate-200 p-3"
                    >
                      <span className="font-medium text-slate-800">
                        {p.student_name ?? "Student"}
                      </span>
                      <span className="text-sm font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200">
                        {p.band !== null ? `Band ${p.band}` : "—"}
                      </span>
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          )}
        </main>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole="student" />

      <main className="mx-auto max-w-2xl px-4 py-8 sm:px-6">

      {turn.status !== "live" && (
        <Card className="mt-6">
          <CardContent className="p-8 text-center">
            <Spinner className="mx-auto h-6 w-6 text-emerald-600" />
            <p className="mt-4 text-slate-600">
              Waiting for the teacher to start the session...
            </p>
          </CardContent>
        </Card>
      )}

      {turn.status === "live" && !evaluation && (
        <Card className="mt-6 border-emerald-200">
          <CardHeader>
            <CardTitle>🎤 Record Your Answer</CardTitle>
          </CardHeader>
          <CardContent>
            {turn.question ? (
              <>
                <Badge className="bg-emerald-100 text-emerald-700">
                  Part {turn.question.part}
                  {turn.question.topic ? ` · ${turn.question.topic}` : ""}
                </Badge>
                <p className="mt-3 text-lg font-medium text-slate-800">
                  {turn.question.question}
                </p>
                <div className="mt-6">
                  <AudioRecorder
                    onRecorded={handleRecorded}
                    onStateChange={(rec) => {
                      busyRef.current = rec;
                      if (rec) setEvaluation(null);
                    }}
                    maxDuration={turn.question.part === 2 ? 120 : turn.question.part === 3 ? 90 : 60}
                    maxRetries={2}
                  />
                </div>
                {error && (
                  <div className="mt-4 rounded-lg border border-red-200 bg-red-50 p-3 text-sm font-medium text-red-700">
                    {error}
                  </div>
                )}
              </>
            ) : (
              <p className="text-slate-500">No question available.</p>
            )}
          </CardContent>
        </Card>
      )}

      {evaluation && (
        <Card className="mt-6 border-emerald-200 bg-emerald-50">
          <CardHeader>
            <CardTitle>
              Your result:{" "}
              {BAND_LABELS[Math.round(evaluation.overall_band)] ??
                `Band ${evaluation.overall_band}`}
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-4 gap-3 text-center">
              {(
                [
                  ["Fluency", evaluation.fluency],
                  ["Grammar", evaluation.grammar],
                  ["Vocabulary", evaluation.vocabulary],
                  ["Pronunciation", evaluation.pronunciation],
                ] as const
              ).map(([label, value]) => (
                <div key={label} className="rounded-lg bg-white p-3 shadow-sm">
                  <p className="text-xl font-bold">{value}</p>
                  <p className="text-xs text-slate-500">{label}</p>
                </div>
              ))}
            </div>
            <div className="mt-4 rounded-lg bg-white p-4 shadow-sm">
              <p className="text-sm font-semibold">Feedback</p>
              <ul className="mt-2 list-disc pl-5 text-sm text-slate-700">
                {evaluation.feedback.map((tip, i) => (
                  <li key={i}>{tip}</li>
                ))}
              </ul>
            </div>
            <p className="mt-4 text-sm text-slate-500">
              Your answer has been submitted. The teacher may continue the session.
            </p>
          </CardContent>
        </Card>
      )}

      {error && <p className="mt-4 text-sm text-rose-600">{error}</p>}
    </main>
  </div>
  );
}
