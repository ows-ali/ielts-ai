"use client";

import Link from "next/link";
import { useState } from "react";
import type { Session } from "@supabase/supabase-js";

import { Navbar } from "@/components/navbar";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { FeedbackCard } from "@/components/writing/feedback-card";
import { WritingVisual } from "@/components/writing/writing-visual";
import { api } from "@/lib/api";
import { useUnauthorizedRedirect } from "@/lib/use-unauthorized";
import type { WritingSubmissionDetail } from "@/lib/types";

const CRITERIA: { key: "task_achievement" | "coherence_cohesion" | "lexical_resource" | "grammatical_range"; label: string }[] = [
  { key: "task_achievement", label: "Task Achievement" },
  { key: "coherence_cohesion", label: "Coherence & Cohesion" },
  { key: "lexical_resource", label: "Lexical Resource" },
  { key: "grammatical_range", label: "Grammar" },
];

const TYPE_LABELS: Record<string, string> = {
  line: "Line graph",
  bar: "Bar chart",
  pie: "Pie chart",
  table: "Table",
  map: "Maps",
  process: "Process diagram",
  multi: "Multiple charts",
  opinion: "Opinion essay",
  discussion: "Discussion essay",
  advantages: "Advantages & disadvantages",
  problem_solution: "Problem & solution",
  positive_negative: "Positive / negative development",
  double_question: "Two-part question",
};

export function TeacherWritingReview({
  session,
  submission,
  userName,
}: {
  session: Session;
  submission: WritingSubmissionDetail;
  userName?: string | null;
}) {
  const [scores, setScores] = useState<Record<string, number | null>>({
    task_achievement: null,
    coherence_cohesion: null,
    lexical_resource: null,
    grammatical_range: null,
  });
  const [comment, setComment] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const handleUnauthorized = useUnauthorizedRedirect();

  const filled = CRITERIA.every((c) => scores[c.key] != null);
  const overall = filled
    ? Math.round(
        (CRITERIA.reduce((sum, c) => sum + (scores[c.key] ?? 0), 0) / 4) * 10
      ) / 10
    : null;

  async function handleSubmit() {
    if (!filled) {
      setError("Please score all four criteria.");
      return;
    }
    setSubmitting(true);
    setError(null);
    setSuccess(false);
    try {
      await api.giveWritingFeedback(session, submission.id, {
        task_achievement: scores.task_achievement!,
        coherence_cohesion: scores.coherence_cohesion!,
        lexical_resource: scores.lexical_resource!,
        grammatical_range: scores.grammatical_range!,
        overall_comment: comment || null,
      });
      setSuccess(true);
      setScores({ task_achievement: null, coherence_cohesion: null, lexical_resource: null, grammatical_range: null });
      setComment("");
    } catch (err) {
      await handleUnauthorized(err);
      setError(err instanceof Error ? err.message : "Failed to submit feedback");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole="teacher" userName={userName} />
      <main className="mx-auto max-w-6xl px-4 py-8 sm:px-6">
        <div className="mb-4 flex items-center gap-2">
          <Link
            href={submission.part === 2 ? "/teacher/writing/part2" : "/teacher/writing"}
            className="text-sm font-semibold text-indigo-600 hover:text-indigo-700"
          >
            ← All submissions
          </Link>
        </div>

        <div className="grid gap-6 lg:grid-cols-2">
          {/* Left: student answer */}
          <div className="space-y-5">
            <Card>
              <CardHeader>
                <div className="flex items-center gap-2">
                  {submission.question_type && (
                    <Badge className="bg-indigo-100 text-indigo-700">
                      {TYPE_LABELS[submission.question_type] ?? submission.question_type}
                    </Badge>
                  )}
                  <Badge className="bg-slate-100 text-slate-600">
                    {submission.word_count !== null && submission.word_count !== undefined
                      ? `${submission.word_count} words`
                      : "—"}
                  </Badge>
                </div>
                <CardTitle className="text-lg">{submission.question_title}</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                {submission.question_prompt && (
                  <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
                    {submission.question_prompt}
                  </p>
                )}
                {submission.part !== 2 && (
                  <WritingVisual
                    data={submission.question_data}
                    imageUrl={submission.question_image_url}
                  />
                )}
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Student answer</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="rounded-lg bg-slate-50 p-4">
                  <p className="whitespace-pre-wrap text-[15px] leading-relaxed text-slate-800">
                    {submission.answer_text}
                  </p>
                </div>
              </CardContent>
            </Card>

            {submission.feedback.length > 0 && (
              <div className="space-y-3">
                <h2 className="text-base font-bold text-slate-800">Previous feedback</h2>
                {submission.feedback.map((f) => (
                  <FeedbackCard key={f.id} feedback={f} />
                ))}
              </div>
            )}
          </div>

          {/* Right: rubric */}
          <div>
            <Card className="sticky top-20">
              <CardHeader>
                <CardTitle>Leave feedback</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="space-y-3">
                  {CRITERIA.map((c) => (
                    <div key={c.key}>
                      <p className="mb-1.5 text-sm font-semibold text-slate-700">{c.label}</p>
                      <div className="flex gap-1">
                        {[4, 5, 6, 7, 8, 9].map((v) => (
                          <button
                            key={v}
                            type="button"
                            onClick={() => setScores((s) => ({ ...s, [c.key]: v }))}
                            className={`h-9 flex-1 rounded-lg text-sm font-bold transition-colors ${
                              scores[c.key] === v
                                ? "bg-indigo-600 text-white shadow-sm"
                                : "bg-slate-100 text-slate-600 hover:bg-slate-200"
                            }`}
                          >
                            {v}
                          </button>
                        ))}
                      </div>
                    </div>
                  ))}
                </div>

                <div className="rounded-lg bg-slate-50 p-3 text-center">
                  <p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
                    Estimated overall band
                  </p>
                  <p className="text-2xl font-bold text-slate-900">
                    {overall !== null ? overall : "—"}
                  </p>
                </div>

                <div>
                  <label className="mb-1.5 block text-sm font-semibold text-slate-700">
                    Overall comment
                  </label>
                  <textarea
                    value={comment}
                    onChange={(e) => setComment(e.target.value)}
                    rows={5}
                    placeholder="Summarise strengths, weaknesses, and specific suggestions for improvement."
                    className="w-full rounded-xl border border-slate-300 bg-white p-3 text-sm leading-relaxed text-slate-800 shadow-sm outline-none transition-colors focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100"
                  />
                </div>

                {success && (
                  <div className="rounded-lg border border-emerald-200 bg-emerald-50 p-3 text-sm font-medium text-emerald-700">
                    Feedback submitted. Students can see it in their history.
                  </div>
                )}
                {error && <p className="text-sm font-medium text-rose-600">{error}</p>}

                <Button className="w-full" onClick={handleSubmit} disabled={submitting || !filled}>
                  {submitting ? "Submitting…" : "Submit feedback"}
                </Button>
                {!filled && (
                  <p className="text-center text-xs text-slate-400">
                    Score all four criteria to enable submission.
                  </p>
                )}
              </CardContent>
            </Card>
          </div>
        </div>
      </main>
    </div>
  );
}
