"use client";

import Link from "next/link";
import { useState } from "react";
import type { Session } from "@supabase/supabase-js";

import { Navbar } from "@/components/navbar";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { BandSampleCard } from "@/components/writing/band-sample-card";
import { WritingEditor } from "@/components/writing/writing-editor";
import { WritingVisual } from "@/components/writing/writing-visual";
import { api } from "@/lib/api";
import { useUnauthorizedRedirect } from "@/lib/use-unauthorized";
import type { WritingQuestionDetail } from "@/lib/types";

const TYPE_LABELS: Record<string, string> = {
  line: "Line graph",
  bar: "Bar chart",
  pie: "Pie chart",
  table: "Table",
  map: "Maps",
  process: "Process diagram",
  multi: "Multiple charts",
};

export function WritingPractice({
  session,
  question,
  userName,
}: {
  session: Session;
  question: WritingQuestionDetail;
  userName?: string | null;
}) {
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleUnauthorized = useUnauthorizedRedirect();

  async function handleSubmit(text: string) {
    setSubmitting(true);
    setError(null);
    try {
      await api.submitWriting(session, question.id, text);
      setSubmitted(true);
    } catch (err) {
      await handleUnauthorized(err);
      setError(err instanceof Error ? err.message : "Failed to submit");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole="student" userName={userName} />
      <main className="mx-auto max-w-5xl px-4 py-8 sm:px-6">
        <div className="mb-4 flex items-center gap-2">
          <Link href="/student/writing" className="text-sm font-semibold text-indigo-600 hover:text-indigo-700">
            ← All questions
          </Link>
        </div>

        <div className="grid gap-6 lg:grid-cols-5">
          {/* Left: question + editor */}
          <div className="space-y-6 lg:col-span-3">
            <Card>
              <CardHeader>
                <div className="flex items-center gap-2">
                  <Badge className="bg-indigo-100 text-indigo-700">
                    {TYPE_LABELS[question.type] ?? question.type}
                  </Badge>
                  {question.difficulty && (
                    <Badge className="bg-slate-100 text-slate-600">{question.difficulty}</Badge>
                  )}
                </div>
                <CardTitle className="text-lg">{question.title}</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <p className="whitespace-pre-wrap text-[15px] leading-relaxed text-slate-700">
                  {question.prompt}
                </p>
                <WritingVisual
                  data={question.data_description}
                  imageUrl={question.image_url}
                />
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Your answer</CardTitle>
              </CardHeader>
              <CardContent>
                {submitted ? (
                  <div className="rounded-xl border border-emerald-200 bg-emerald-50 p-6 text-center">
                    <p className="text-lg font-bold text-emerald-800">Answer submitted ✓</p>
                    <p className="mt-1 text-sm text-emerald-700">
                      A teacher will review your answer. Track feedback in your submission history.
                    </p>
                    <div className="mt-4 flex justify-center gap-2">
                      <Link href="/student/writing/history">
                        <Button>View my submissions</Button>
                      </Link>
                      <Button variant="secondary" onClick={() => setSubmitted(false)}>
                        Write another attempt
                      </Button>
                    </div>
                  </div>
                ) : (
                  <>
                    <WritingEditor
                      questionId={question.id}
                      onSubmit={handleSubmit}
                      submitting={submitting}
                    />
                    {error && (
                      <p className="mt-3 text-sm font-medium text-rose-600">{error}</p>
                    )}
                  </>
                )}
              </CardContent>
            </Card>
          </div>

          {/* Right: model answers */}
          <div className="space-y-3 lg:col-span-2">
            <div>
              <h2 className="text-base font-bold text-slate-800">Model answers</h2>
              <p className="text-xs text-slate-500">
                Compare the Band 5, 7 and 9 sample answers to understand what each band looks like.
              </p>
            </div>
            {question.samples.length === 0 ? (
              <p className="text-sm text-slate-400">No samples available yet.</p>
            ) : (
              question.samples.map((s, i) => (
                <BandSampleCard key={s.id} sample={s} defaultOpen={i === 0} />
              ))
            )}
          </div>
        </div>
      </main>
    </div>
  );
}
