"use client";

import Link from "next/link";

import { Navbar } from "@/components/navbar";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { WritingVisual } from "@/components/writing/writing-visual";
import { FeedbackCard } from "@/components/writing/feedback-card";
import type { WritingSubmissionDetail } from "@/lib/types";

const TYPE_LABELS: Record<string, string> = {
  line: "Line graph",
  bar: "Bar chart",
  pie: "Pie chart",
  table: "Table",
  map: "Maps",
  process: "Process diagram",
  multi: "Multiple charts",
};

export function WritingSubmissionView({
  submission,
  userName,
}: {
  submission: WritingSubmissionDetail;
  userName?: string | null;
}) {
  const hasFeedback = submission.feedback.length > 0;

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole="student" userName={userName} />
      <main className="mx-auto max-w-4xl px-4 py-8 sm:px-6">
        <div className="mb-4 flex items-center gap-2">
          <Link href="/student/writing/history" className="text-sm font-semibold text-indigo-600 hover:text-indigo-700">
            ← My submissions
          </Link>
        </div>

        <Card>
          <CardHeader>
            <div className="flex items-center gap-2">
              {submission.question_type && (
                <Badge className="bg-indigo-100 text-indigo-700">
                  {TYPE_LABELS[submission.question_type] ?? submission.question_type}
                </Badge>
              )}
              {submission.question_difficulty && (
                <Badge className="bg-slate-100 text-slate-600">{submission.question_difficulty}</Badge>
              )}
              {hasFeedback && submission.overall_band !== null && (
                <Badge className="bg-emerald-100 text-emerald-700">
                  Overall Band {submission.overall_band}
                </Badge>
              )}
            </div>
            <CardTitle className="text-lg">{submission.question_title}</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            {submission.question_prompt && (
              <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
                {submission.question_prompt}
              </p>
            )}
            <WritingVisual
              data={submission.question_data}
              imageUrl={submission.question_image_url}
            />
          </CardContent>
        </Card>

        <Card className="mt-6">
          <CardHeader>
            <CardTitle>Your answer</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-slate-400">
              {submission.word_count !== null && submission.word_count !== undefined
                ? `${submission.word_count} words · `
                : ""}
              Submitted {submission.created_at ? new Date(submission.created_at).toLocaleString() : ""}
            </p>
            <div className="mt-3 rounded-lg bg-slate-50 p-4">
              <p className="whitespace-pre-wrap text-[15px] leading-relaxed text-slate-800">
                {submission.answer_text}
              </p>
            </div>
          </CardContent>
        </Card>

        <div className="mt-6 space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-bold text-slate-900">
              Teacher feedback{" "}
              {hasFeedback && (
                <span className="text-sm font-medium text-slate-400">({submission.feedback.length})</span>
              )}
            </h2>
            {!hasFeedback && (
              <Link href="/student/writing">
                <Button variant="secondary">Practice another question</Button>
              </Link>
            )}
          </div>

          {hasFeedback ? (
            submission.feedback.map((f) => <FeedbackCard key={f.id} feedback={f} />)
          ) : (
            <Card>
              <CardContent className="py-10 text-center">
                <p className="text-slate-500">
                  No feedback yet. Your teacher will review your answer and leave comments here.
                </p>
              </CardContent>
            </Card>
          )}
        </div>
      </main>
    </div>
  );
}
