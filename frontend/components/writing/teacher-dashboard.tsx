"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import type { Session } from "@supabase/supabase-js";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Spinner } from "@/components/ui/spinner";
import { api } from "@/lib/api";
import { useUnauthorizedRedirect } from "@/lib/use-unauthorized";
import type { WritingSubmission } from "@/lib/types";

const TYPE_LABELS: Record<string, string> = {
  line: "Line",
  bar: "Bar",
  pie: "Pie",
  table: "Table",
  map: "Map",
  process: "Process",
  multi: "Mixed",
  opinion: "Opinion",
  discussion: "Discussion",
  advantages: "Advantages",
  problem_solution: "Problem/Solution",
  positive_negative: "Positive/Negative",
  double_question: "Two-part",
};

export function TeacherWritingDashboard({ session, part = 1 }: { session: Session; part?: number }) {
  const [submissions, setSubmissions] = useState<WritingSubmission[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [filter, setFilter] = useState<"all" | "pending" | "reviewed">("all");

  const handleUnauthorized = useUnauthorizedRedirect();

  useEffect(() => {
    let mounted = true;
    api
      .allWritingSubmissions(session, part)
      .then((rows) => {
        if (mounted) setSubmissions(rows);
      })
      .catch((err) => {
        if (mounted) {
          handleUnauthorized(err);
          setError(err instanceof Error ? err.message : "Failed to load submissions");
        }
      });
    return () => {
      mounted = false;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [session, part]);

  if (!submissions) {
    return (
      <div className="flex items-center justify-center py-20">
        <Spinner className="h-8 w-8" />
      </div>
    );
  }

  if (error) {
    return <p className="text-sm text-rose-600">{error}</p>;
  }

  const filtered = submissions.filter((s) => {
    if (filter === "pending") return s.feedback.length === 0;
    if (filter === "reviewed") return s.feedback.length > 0;
    return true;
  });

  return (
    <div className="space-y-5">
      <div className="flex flex-wrap items-center gap-2">
        <button
          type="button"
          onClick={() => setFilter("all")}
          className={`rounded-full px-3 py-1.5 text-xs font-semibold transition-colors ${
            filter === "all" ? "bg-indigo-600 text-white" : "bg-slate-100 text-slate-600 hover:bg-slate-200"
          }`}
        >
          All ({submissions.length})
        </button>
        <button
          type="button"
          onClick={() => setFilter("pending")}
          className={`rounded-full px-3 py-1.5 text-xs font-semibold transition-colors ${
            filter === "pending" ? "bg-amber-500 text-white" : "bg-slate-100 text-slate-600 hover:bg-slate-200"
          }`}
        >
          Needs feedback ({submissions.filter((s) => s.feedback.length === 0).length})
        </button>
        <button
          type="button"
          onClick={() => setFilter("reviewed")}
          className={`rounded-full px-3 py-1.5 text-xs font-semibold transition-colors ${
            filter === "reviewed" ? "bg-emerald-600 text-white" : "bg-slate-100 text-slate-600 hover:bg-slate-200"
          }`}
        >
          Reviewed ({submissions.filter((s) => s.feedback.length > 0).length})
        </button>
      </div>

      {filtered.length === 0 ? (
        <Card>
          <CardContent className="py-12 text-center">
            <p className="text-slate-500">
              {submissions.length === 0
                ? `No writing submissions yet. Share the Writing Task ${part} practice page with your students.`
                : "No submissions match this filter."}
            </p>
          </CardContent>
        </Card>
      ) : (
        <ul className="space-y-3">
          {filtered.map((s) => (
            <li key={s.id}>
              <Link
                href={`/teacher/writing/${s.id}`}
                className="block rounded-xl border border-slate-200 bg-white p-4 shadow-sm transition-colors hover:border-indigo-300"
              >
                <div className="flex flex-wrap items-start justify-between gap-3">
                  <div className="min-w-0">
                    <p className="font-semibold text-slate-800">{s.question_title ?? "Question"}</p>
                    <p className="mt-0.5 text-xs text-slate-500">
                      {s.question_type ? `${TYPE_LABELS[s.question_type] ?? s.question_type} · ` : ""}
                      {s.word_count !== null && s.word_count !== undefined ? `${s.word_count} words · ` : ""}
                      {s.created_at ? new Date(s.created_at).toLocaleString() : ""}
                    </p>
                  </div>
                  <div className="flex shrink-0 items-center gap-2">
                    {s.overall_band !== null && s.overall_band !== undefined && (
                      <span className="rounded-full bg-emerald-50 px-2.5 py-1 text-sm font-bold text-emerald-700 border border-emerald-200">
                        Band {s.overall_band}
                      </span>
                    )}
                    {s.feedback.length > 0 ? (
                      <Badge className="bg-emerald-50 text-emerald-700 border-emerald-200">
                        {s.feedback.length} feedback
                      </Badge>
                    ) : (
                      <Badge className="bg-amber-50 text-amber-700 border-amber-200">Needs review</Badge>
                    )}
                  </div>
                </div>
                <p className="mt-2 line-clamp-2 text-sm text-slate-500">“{s.answer_text}”</p>
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
