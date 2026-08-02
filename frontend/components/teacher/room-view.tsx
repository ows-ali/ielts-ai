"use client";

import { useEffect, useState } from "react";
import type { Session } from "@supabase/supabase-js";

import { SignOutButton } from "@/components/sign-out-button";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Spinner } from "@/components/ui/spinner";
import { api } from "@/lib/api";
import { createClient } from "@/lib/supabase/client";
import type { ClassReport, Participant, Room, TurnState } from "@/lib/types";

const STATUS_STYLES: Record<string, string> = {
  waiting: "bg-slate-100 text-slate-600",
  live: "bg-emerald-100 text-emerald-700",
  ended: "bg-amber-100 text-amber-700",
};

const PARTICIPANT_STYLES: Record<string, string> = {
  waiting: "bg-slate-100 text-slate-600",
  speaking: "bg-sky-100 text-sky-700",
  completed: "bg-emerald-100 text-emerald-700",
};

export function TeacherRoomView({
  session,
  room: initialRoom,
  initialParticipants,
}: {
  session: Session;
  room: Room;
  initialParticipants: Participant[];
}) {
  const [room, setRoom] = useState(initialRoom);
  const [participants, setParticipants] = useState(initialParticipants);
  const [turn, setTurn] = useState<TurnState | null>(null);
  const [report, setReport] = useState<ClassReport | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function refresh() {
    try {
      const [r, p, t] = await Promise.all([
        api.getRoom(session, initialRoom.id),
        api.participants(session, initialRoom.id),
        api.turn(session, initialRoom.id),
      ]);
      setRoom(r);
      setParticipants(p);
      setTurn(t);
      if (r.status === "ended") {
        const rep = await api.classReport(session, initialRoom.id);
        setReport(rep);
      } else {
        setReport(null);
      }
    } catch {
      /* transient */
    }
  }

  useEffect(() => {
    refresh();
    const supabase = createClient();
    const channel = supabase
      .channel(`room-${initialRoom.id}`)
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "rooms", filter: `id=eq.${initialRoom.id}` },
        refresh
      )
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "participants", filter: `room_id=eq.${initialRoom.id}` },
        refresh
      )
      .subscribe();
    const interval = setInterval(refresh, 5000);
    return () => {
      supabase.removeChannel(channel);
      clearInterval(interval);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [initialRoom.id]);

  async function start() {
    setLoading(true);
    setError(null);
    try {
      const t = await api.startRoom(session, initialRoom.id);
      setTurn(t);
      await refresh();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to start");
    } finally {
      setLoading(false);
    }
  }

  async function end() {
    setLoading(true);
    setError(null);
    try {
      const r = await api.endRoom(session, initialRoom.id);
      setRoom(r);
      const rep = await api.classReport(session, initialRoom.id);
      setReport(rep);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to end");
    } finally {
      setLoading(false);
    }
  }

  const canStart = room.status === "waiting" && participants.length > 0;

  return (
    <main className="mx-auto max-w-4xl p-6">
      <div className="flex items-start justify-between">
        <div>
          <h1 className="text-2xl font-bold">{room.title}</h1>
          <p className="text-sm text-slate-500">
            Room code:{" "}
            <span className="rounded bg-slate-100 px-2 py-0.5 font-mono text-lg font-semibold tracking-widest">
              {room.room_code}
            </span>{" "}
            · Part {room.part}
          </p>
          <p className="mt-1 text-xs text-slate-400">
            Share this code with your students.
          </p>
        </div>
        <div className="flex items-center gap-2">
          <Badge className={STATUS_STYLES[room.status] ?? ""}>{room.status}</Badge>
          <SignOutButton />
        </div>
      </div>

      <div className="mt-6 flex items-center gap-3">
        <Button onClick={start} disabled={!canStart || loading}>
          {loading && room.status === "waiting" ? <Spinner /> : null}
          {room.status === "live" ? "Session live" : "Start session"}
        </Button>
        {room.status === "live" && (
          <Button variant="danger" onClick={end} disabled={loading}>
            End session
          </Button>
        )}
      </div>
      {error && <p className="mt-2 text-sm text-rose-600">{error}</p>}

      {turn?.status === "live" && turn.current_student_name && (
        <Card className="mt-6 border-emerald-200 bg-emerald-50">
          <CardContent>
            <p className="text-sm text-emerald-700">
              Now speaking:{" "}
              <span className="font-semibold">{turn.current_student_name}</span>
            </p>
          </CardContent>
        </Card>
      )}

      <div className="mt-6 grid gap-6 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Students ({participants.length})</CardTitle>
          </CardHeader>
          <CardContent>
            {participants.length === 0 ? (
              <p className="text-sm text-slate-500">
                Waiting for students to join...
              </p>
            ) : (
              <ul className="space-y-2">
                {participants.map((p) => (
                  <li
                    key={p.id}
                    className="flex items-center justify-between rounded-lg border border-slate-200 p-3"
                  >
                    <span className="font-medium">
                      {p.student_name ?? "Student"}
                    </span>
                    <Badge className={PARTICIPANT_STYLES[p.status] ?? ""}>
                      {p.status}
                    </Badge>
                  </li>
                ))}
              </ul>
            )}
          </CardContent>
        </Card>

        {report && (
          <Card>
            <CardHeader>
              <CardTitle>Class report</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-2xl font-bold">
                Average band: {report.average_band ?? "—"}
              </p>
              <ul className="mt-4 space-y-2">
                {report.participants.map((p) => (
                  <li
                    key={p.student_id}
                    className="flex items-center justify-between rounded-lg border border-slate-200 p-3"
                  >
                    <span className="font-medium">{p.student_name ?? "Student"}</span>
                    <span className="text-sm font-semibold">
                      {p.band !== null ? `Band ${p.band}` : "—"}
                    </span>
                  </li>
                ))}
              </ul>
              {report.common_problems.length > 0 && (
                <div className="mt-4 rounded-lg bg-amber-50 p-3">
                  <p className="text-sm font-semibold text-amber-800">
                    Common problems
                  </p>
                  <ul className="mt-1 list-disc pl-5 text-sm text-amber-700">
                    {report.common_problems.map((problem, i) => (
                      <li key={i}>{problem}</li>
                    ))}
                  </ul>
                </div>
              )}
            </CardContent>
          </Card>
        )}
      </div>
    </main>
  );
}
