"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import type { Session } from "@supabase/supabase-js";

import { AudioRecorder } from "@/components/student/audio-recorder";
import { SignOutButton } from "@/components/sign-out-button";
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
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const alreadyEvaluatedRef = useRef<string | null>(null);

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

    const supabase = createClient();
    const channel = supabase
      .channel(`student-room-${roomId}`)
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "rooms", filter: `id=eq.${roomId}` },
        () => {
          doRefresh();
        }
      )
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "participants", filter: `room_id=eq.${roomId}` },
        () => {
          doRefresh();
        }
      )
      .subscribe();

    return () => {
      mounted = false;
      supabase.removeChannel(channel);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [roomId]);

  useEffect(() => {
    if (turn?.status === "ended") {
      api.classReport(session, roomId).then(setClassReport).catch(() => {});
    }
  }, [turn?.status, session, roomId]);

  const myTurn =
    turn?.status === "live" && turn.current_student_id === userId;

  async function handleRecorded(blob: Blob, mimeType: string) {
    setSubmitting(true);
    setError(null);
    try {
      const supabase = createClient();
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
      setSubmitting(false);
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
      <main className="mx-auto max-w-lg p-6 space-y-6">
        <Card>
          <CardContent className="p-8 text-center">
            <h1 className="text-xl font-bold">Session ended</h1>
            <p className="mt-2 text-sm text-slate-500">
              Thanks for practicing! Check the class performance below or view your full report.
            </p>
            <Button className="mt-4" onClick={() => router.push("/student/report")}>
              View my progress report
            </Button>
          </CardContent>
        </Card>

        {classReport && (
          <Card>
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
    );
  }

  return (
    <main className="mx-auto max-w-2xl p-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold">Speaking practice</h1>
        <SignOutButton />
      </div>

      {!myTurn && !evaluation && (
        <Card className="mt-6">
          <CardContent className="p-8 text-center">
            <Spinner className="mx-auto h-6 w-6 text-emerald-600" />
            <p className="mt-4 text-slate-600">
              {turn.current_student_name
                ? `${turn.current_student_name} is speaking. Wait for your turn.`
                : "Waiting for the teacher to start the session..."}
            </p>
          </CardContent>
        </Card>
      )}

      {myTurn && !evaluation && (
        <Card className="mt-6 border-emerald-200">
          <CardHeader>
            <CardTitle>Your turn</CardTitle>
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
                      if (rec) setEvaluation(null);
                    }}
                  />
                </div>
                {submitting && (
                  <p className="mt-3 flex items-center justify-center gap-2 text-sm text-slate-500">
                    <Spinner className="h-4 w-4" /> Evaluating your answer...
                  </p>
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
  );
}
