"use client";

import { useEffect, useState } from "react";
import type { Session } from "@supabase/supabase-js";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Spinner } from "@/components/ui/spinner";
import { api } from "@/lib/api";
import type { RoomScoresOut } from "@/lib/types";

export function ClassScoresCollapsible({
  roomId,
  session,
  currentStudentId,
}: {
  roomId: string;
  session: Session;
  currentStudentId?: string;
}) {
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [scores, setScores] = useState<RoomScoresOut | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (open && !scores && !loading) {
      setLoading(true);
      setError(null);
      api
        .roomScores(session, roomId)
        .then((data) => {
          setScores(data);
        })
        .catch((err) => {
          setError(err instanceof Error ? err.message : "Failed to load class scores");
        })
        .finally(() => {
          setLoading(false);
        });
    }
  }, [open, scores, loading, session, roomId]);

  return (
    <div className="mt-3 rounded-xl border border-indigo-100 bg-indigo-50/30 overflow-hidden">
      <Button
        type="button"
        variant="ghost"
        onClick={() => setOpen((prev) => !prev)}
        className="flex w-full items-center justify-between px-4 py-2.5 text-left text-xs font-semibold text-indigo-900 hover:bg-indigo-100/50"
      >
        <span className="flex items-center gap-2">
          <span>📊</span>
          <span>Classroom Scores & Peer Comparison</span>
        </span>
        <span className="text-indigo-600 font-bold">{open ? "▲ Hide" : "▼ Expand"}</span>
      </Button>

      {open && (
        <div className="border-t border-indigo-100/80 p-4 space-y-3 bg-white/70">
          {loading && (
            <div className="flex items-center justify-center py-4 gap-2 text-xs text-slate-500">
              <Spinner className="h-4 w-4 text-indigo-600" /> Loading class scores...
            </div>
          )}

          {error && <p className="text-xs text-rose-600 font-medium py-1">{error}</p>}

          {scores && scores.participants.length > 0 && (
            <div className="space-y-2.5">
              <p className="text-[11px] font-semibold uppercase tracking-wider text-slate-500">
                Room Code: <span className="font-mono text-slate-700 font-bold">{scores.room_code}</span> · {scores.participants.length} Participants
              </p>
              <ul className="space-y-2">
                {scores.participants.map((p) => {
                  const isYou = currentStudentId && p.student_id === currentStudentId;
                  return (
                    <li
                      key={p.student_id}
                      className={`rounded-lg border p-3 text-xs transition-colors ${
                        isYou
                          ? "border-emerald-300 bg-emerald-50/60 shadow-xs"
                          : "border-slate-200 bg-white"
                      }`}
                    >
                      <div className="flex items-center justify-between mb-1.5">
                        <div className="flex items-center gap-1.5 font-semibold text-slate-900">
                          <span>{p.student_name ?? "Student"}</span>
                          {isYou && (
                            <Badge className="bg-emerald-600 text-white text-[10px] px-1.5 py-0">
                              You
                            </Badge>
                          )}
                        </div>
                        <span className="font-bold text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded border border-indigo-200">
                          {p.band !== null ? `Band ${p.band}` : "Pending"}
                        </span>
                      </div>

                      {/* Sub-scores breakdown */}
                      {p.band !== null && (
                        <div className="grid grid-cols-4 gap-1.5 pt-1 text-center text-[10px]">
                          <div className="rounded bg-slate-50 p-1 border border-slate-100">
                            <span className="text-slate-400 block text-[9px]">Fluency</span>
                            <span className="font-bold text-slate-700">{p.fluency ?? "—"}</span>
                          </div>
                          <div className="rounded bg-slate-50 p-1 border border-slate-100">
                            <span className="text-slate-400 block text-[9px]">Grammar</span>
                            <span className="font-bold text-slate-700">{p.grammar ?? "—"}</span>
                          </div>
                          <div className="rounded bg-slate-50 p-1 border border-slate-100">
                            <span className="text-slate-400 block text-[9px]">Vocab</span>
                            <span className="font-bold text-slate-700">{p.vocabulary ?? "—"}</span>
                          </div>
                          <div className="rounded bg-slate-50 p-1 border border-slate-100">
                            <span className="text-slate-400 block text-[9px]">Pron</span>
                            <span className="font-bold text-slate-700">{p.pronunciation ?? "—"}</span>
                          </div>
                        </div>
                      )}
                    </li>
                  );
                })}
              </ul>
            </div>
          )}

          {scores && scores.participants.length === 0 && (
            <p className="text-xs text-slate-500 py-1">No other participant scores found for this session.</p>
          )}
        </div>
      )}
    </div>
  );
}
