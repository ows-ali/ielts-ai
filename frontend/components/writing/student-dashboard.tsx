"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import type { Session } from "@supabase/supabase-js";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Spinner } from "@/components/ui/spinner";
import { api } from "@/lib/api";
import { useUnauthorizedRedirect } from "@/lib/use-unauthorized";
import type { WritingQuestion, WritingQuestionType } from "@/lib/types";

const TYPE_META: Record<WritingQuestionType, { label: string; emoji: string }> = {
  line: { label: "Line Graphs", emoji: "📈" },
  bar: { label: "Bar Charts", emoji: "📊" },
  pie: { label: "Pie Charts", emoji: "🥧" },
  table: { label: "Tables", emoji: "🧮" },
  map: { label: "Maps", emoji: "🗺️" },
  process: { label: "Processes", emoji: "⚙️" },
  multi: { label: "Mixed Charts", emoji: "📚" },
};

const DIFFICULTY_STYLES: Record<string, string> = {
  easy: "bg-emerald-50 text-emerald-700 border-emerald-200",
  medium: "bg-amber-50 text-amber-700 border-amber-200",
  hard: "bg-rose-50 text-rose-700 border-rose-200",
};

const FILTERS: ("all" | WritingQuestionType)[] = [
  "all",
  "line",
  "bar",
  "pie",
  "table",
  "map",
  "process",
  "multi",
];

export function WritingDashboard({ session }: { session: Session }) {
  const [questions, setQuestions] = useState<WritingQuestion[]>([]);
  const [loading, setLoading] = useState(true);
  const [type, setType] = useState<"all" | WritingQuestionType>("all");
  const [difficulty, setDifficulty] = useState<string>("all");
  const [error, setError] = useState<string | null>(null);

  const handleUnauthorized = useUnauthorizedRedirect();

  useEffect(() => {
    let mounted = true;
    setLoading(true);
    api
      .writingQuestions(session, {
        type: type === "all" ? undefined : type,
        difficulty: difficulty === "all" ? undefined : difficulty,
      })
      .then((qs) => {
        if (mounted) {
          setQuestions(qs);
          setLoading(false);
        }
      })
      .catch((err) => {
        if (mounted) {
          handleUnauthorized(err);
          setError(err instanceof Error ? err.message : "Failed to load questions");
          setLoading(false);
        }
      });
    return () => {
      mounted = false;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [session, type, difficulty]);

  const grouped = useMemo(() => {
    if (type !== "all") {
      return [[type, questions]] as const;
    }
    const map = new Map<WritingQuestionType, WritingQuestion[]>();
    for (const q of questions) {
      if (!map.has(q.type)) map.set(q.type, []);
      map.get(q.type)!.push(q);
    }
    return Array.from(map.entries());
  }, [questions, type]);

  return (
    <div className="space-y-6">
      <Card>
        <CardContent className="py-4">
          <div className="flex flex-wrap items-center gap-1.5">
            {FILTERS.map((f) => (
              <button
                key={f}
                type="button"
                onClick={() => setType(f)}
                className={`rounded-full px-3 py-1.5 text-xs font-semibold transition-colors ${
                  type === f
                    ? "bg-indigo-600 text-white shadow-sm"
                    : "bg-slate-100 text-slate-600 hover:bg-slate-200"
                }`}
              >
                {f === "all" ? "All types" : TYPE_META[f].label}
              </button>
            ))}
          </div>
          <div className="mt-3 flex items-center gap-1.5">
            <span className="text-xs font-semibold text-slate-500">Difficulty:</span>
            {["all", "easy", "medium", "hard"].map((d) => (
              <button
                key={d}
                type="button"
                onClick={() => setDifficulty(d)}
                className={`rounded-full px-3 py-1 text-xs font-semibold capitalize transition-colors ${
                  difficulty === d
                    ? "bg-slate-900 text-white"
                    : "bg-slate-100 text-slate-600 hover:bg-slate-200"
                }`}
              >
                {d}
              </button>
            ))}
          </div>
        </CardContent>
      </Card>

      {loading ? (
        <div className="flex items-center justify-center py-20">
          <Spinner className="h-8 w-8" />
        </div>
      ) : error ? (
        <p className="text-sm text-rose-600">{error}</p>
      ) : questions.length === 0 ? (
        <Card>
          <CardContent className="py-12 text-center">
            <p className="text-slate-500">No questions match these filters.</p>
          </CardContent>
        </Card>
      ) : (
        grouped.map(([qtype, qs]) => (
          <section key={qtype}>
            <h2 className="mb-3 flex items-center gap-2 text-lg font-bold text-slate-800">
              <span>{TYPE_META[qtype]?.emoji}</span>
              {TYPE_META[qtype]?.label}
              <span className="text-sm font-medium text-slate-400">({qs.length})</span>
            </h2>
            <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
              {qs.map((q) => (
                <Link
                  key={q.id}
                  href={`/student/writing/${q.id}`}
                  className="group rounded-xl border border-slate-200 bg-white p-4 shadow-sm transition-all hover:-translate-y-0.5 hover:border-indigo-400 hover:shadow-md"
                >
                  <div className="flex items-start justify-between gap-2">
                    <p className="font-semibold text-slate-800 group-hover:text-indigo-700">
                      {q.title}
                    </p>
                    {q.difficulty && (
                      <Badge className={DIFFICULTY_STYLES[q.difficulty] ?? ""}>
                        {q.difficulty}
                      </Badge>
                    )}
                  </div>
                  <p className="mt-2 line-clamp-2 text-xs text-slate-500">
                    {q.prompt.split("\n")[0]}
                  </p>
                  <p className="mt-3 text-xs font-semibold text-indigo-600 group-hover:text-indigo-700">
                    Start practicing →
                  </p>
                </Link>
              ))}
            </div>
          </section>
        ))
      )}
    </div>
  );
}
