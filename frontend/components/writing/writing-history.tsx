"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import type { Session } from "@supabase/supabase-js";

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

export function WritingHistory({ session, part = 1 }: { session: Session; part?: number }) {
  const [submissions, setSubmissions] = useState<WritingSubmission[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleUnauthorized = useUnauthorizedRedirect();

  useEffect(() => {
    let mounted = true;
    api
      .myWritingSubmissions(session, part)
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

  if (submissions.length === 0) {
    return (
      <Card>
        <CardContent className="py-12 text-center">
          <p className="text-slate-500">
            You haven&apos;t submitted any writing answers yet.{" "}
            <Link
              href={part === 2 ? "/student/writing/part2" : "/student/writing"}
              className="font-semibold text-indigo-600 hover:underline"
            >
              Start practicing now
            </Link>
          </p>
        </CardContent>
      </Card>
    );
  }

  return (
    <ul className="space-y-4">
      {submissions.map((s) => (
        <li key={s.id}>
          <Link
            href={`/student/writing/submission/${s.id}`}
            className="block rounded-xl border border-slate-200 bg-white p-4 shadow-sm transition-colors hover:border-indigo-300"
          >
            <div className="flex items-start justify-between gap-3">
              <div>
                <p className="font-semibold text-slate-800">{s.question_title ?? "Writing question"}</p>
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
                <span
                  className={`rounded-full px-2.5 py-1 text-xs font-semibold ${
                    s.feedback.length > 0
                      ? "bg-indigo-50 text-indigo-700 border border-indigo-200"
                      : "bg-slate-100 text-slate-500"
                  }`}
                >
                  {s.feedback.length > 0 ? `${s.feedback.length} feedback` : "Pending review"}
                </span>
              </div>
            </div>
            <p className="mt-2 line-clamp-2 text-sm text-slate-500">“{s.answer_text}”</p>
          </Link>
        </li>
      ))}
    </ul>
  );
}
