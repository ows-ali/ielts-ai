import Link from "next/link";

import { LeaderboardPreview } from "@/components/landing/leaderboard-preview";
import { api } from "@/lib/api";
import { getUserOrNull } from "@/lib/auth";
import type { Community } from "@/lib/types";

export const dynamic = "force-dynamic";

const EMPTY_COMMUNITY: Community = { week: [], all: [], improvers: [], activity: [] };

const FEATURES = [
  {
    emoji: "🎙️",
    title: "Live Speaking Rooms",
    desc: "Teachers run Part 1–3 practice rooms. Join with a code and answer by voice.",
  },
  {
    emoji: "🤖",
    title: "Instant AI Evaluation",
    desc: "Gemini transcribes your answer and scores fluency, grammar, vocabulary and pronunciation.",
  },
  {
    emoji: "✍️",
    title: "Writing Task 1 & 2",
    desc: "Practise charts, maps, processes and essays with model Band 5/7/9 answers and teacher feedback.",
  },
  {
    emoji: "🏅",
    title: "Achievement Badges",
    desc: "Earn badges for speaking milestones, band scores, feedback and writing coverage.",
  },
  {
    emoji: "🏆",
    title: "Community Leaderboards",
    desc: "Compete on the weekly board, chase all-time greats, and follow the improvers.",
  },
  {
    emoji: "👥",
    title: "Public Profiles",
    desc: "See classmates' badges and progress, and share your own achievements.",
  },
];

export default async function LandingPage() {
  const { session, user } = await getUserOrNull();

  let community: Community = EMPTY_COMMUNITY;
  try {
    community = await api.community(session);
  } catch {
    community = EMPTY_COMMUNITY;
  }

  const dashboardHref = user?.role === "teacher" ? "/teacher" : "/student";

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      {/* Top navigation */}
      <header className="sticky top-0 z-50 border-b border-slate-800/80 bg-slate-950/90 backdrop-blur-md">
        <div className="mx-auto flex max-w-6xl items-center justify-between gap-2 px-4 py-3 sm:px-6">
          <Link href="/" className="flex items-center gap-2">
            <div className="flex h-8 w-8 items-center justify-center rounded-xl bg-gradient-to-tr from-indigo-600 via-violet-600 to-emerald-500 shadow-md shadow-indigo-500/20">
              <span className="font-extrabold text-white">i</span>
            </div>
            <span className="bg-gradient-to-r from-slate-100 via-indigo-100 to-slate-200 bg-clip-text font-black text-lg tracking-tight text-transparent">
              IELTS AI Classroom
            </span>
          </Link>
          <div className="flex items-center gap-2">
            {user ? (
              <Link
                href={dashboardHref}
                className="rounded-lg bg-gradient-to-r from-indigo-600 via-violet-600 to-indigo-600 px-4 py-2 text-sm font-bold text-white shadow-lg shadow-indigo-600/30 transition-colors hover:from-indigo-500 hover:to-violet-500"
              >
                Open your dashboard
              </Link>
            ) : (
              <>
                <Link
                  href="/login"
                  className="rounded-lg border border-slate-700 px-4 py-2 text-sm font-semibold text-slate-200 hover:bg-slate-800"
                >
                  Sign in
                </Link>
                <Link
                  href="/register"
                  className="rounded-lg bg-gradient-to-r from-indigo-600 via-violet-600 to-indigo-600 px-4 py-2 text-sm font-bold text-white shadow-lg shadow-indigo-600/30 transition-colors hover:from-indigo-500 hover:to-violet-500"
                >
                  Sign up free
                </Link>
              </>
            )}
          </div>
        </div>
      </header>

      <main>
        {/* Hero */}
        <section className="relative overflow-hidden">
          <div className="pointer-events-none absolute left-1/2 top-1/3 h-[500px] w-[700px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-gradient-to-tr from-indigo-600/25 via-violet-600/20 to-emerald-500/10 blur-3xl" />
          <div className="relative mx-auto max-w-4xl px-4 py-20 text-center sm:px-6 sm:py-28">
            <span className="rounded-full border border-indigo-500/30 bg-indigo-500/20 px-3 py-1 text-xs font-bold uppercase tracking-widest text-indigo-300">
              AI-powered IELTS practice
            </span>
            <h1 className="mt-5 text-4xl font-black tracking-tight sm:text-6xl">
              Speak. Write.{" "}
              <span className="bg-gradient-to-r from-indigo-400 via-violet-400 to-emerald-400 bg-clip-text text-transparent">
                Improve.
              </span>
            </h1>
            <p className="mx-auto mt-5 max-w-2xl text-base text-slate-400 sm:text-lg">
              Real-time speaking rooms with instant AI band scoring, plus writing practice
              with model answers and teacher feedback. Earn badges, climb the community
              leaderboard, and share your progress.
            </p>
            <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
              {user ? (
                <Link
                  href={dashboardHref}
                  className="rounded-xl bg-gradient-to-r from-indigo-600 via-violet-600 to-indigo-600 px-6 py-3 text-base font-bold text-white shadow-xl shadow-indigo-600/30 transition-colors hover:from-indigo-500 hover:to-violet-500"
                >
                  Go to your dashboard →
                </Link>
              ) : (
                <>
                  <Link
                    href="/register"
                    className="rounded-xl bg-gradient-to-r from-indigo-600 via-violet-600 to-indigo-600 px-6 py-3 text-base font-bold text-white shadow-xl shadow-indigo-600/30 transition-colors hover:from-indigo-500 hover:to-violet-500"
                  >
                    Start practising free
                  </Link>
                  <Link
                    href="/login"
                    className="rounded-xl border border-slate-700 px-6 py-3 text-base font-semibold text-slate-200 hover:bg-slate-800"
                  >
                    Sign in
                  </Link>
                </>
              )}
            </div>
          </div>
        </section>

        {/* Features */}
        <section className="border-t border-slate-800/60 bg-slate-900/40">
          <div className="mx-auto max-w-6xl px-4 py-16 sm:px-6">
            <h2 className="text-center text-2xl font-bold sm:text-3xl">
              Everything you need to hit your target band
            </h2>
            <div className="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {FEATURES.map((f) => (
                <div
                  key={f.title}
                  className="rounded-2xl border border-slate-800 bg-slate-900/70 p-5 transition-colors hover:border-indigo-500/50"
                >
                  <div className="text-2xl" aria-hidden>
                    {f.emoji}
                  </div>
                  <h3 className="mt-3 font-bold text-slate-100">{f.title}</h3>
                  <p className="mt-1.5 text-sm text-slate-400">{f.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Leaderboard preview */}
        <section className="mx-auto max-w-6xl px-4 py-16 sm:px-6">
          <h2 className="text-2xl font-bold sm:text-3xl">See who&apos;s climbing</h2>
          <p className="mt-2 text-sm text-slate-400">
            The weekly board resets every Monday — everyone gets a fresh chance to top it.
          </p>
          <div className="mt-8">
            <LeaderboardPreview week={community.week} activity={community.activity} />
          </div>
        </section>

        {/* CTA */}
        <section className="border-t border-slate-800/60">
          <div className="mx-auto max-w-4xl px-4 py-16 text-center sm:px-6">
            <h2 className="text-2xl font-bold sm:text-3xl">Ready to start?</h2>
            <p className="mt-2 text-sm text-slate-400">
              Join a speaking session or begin your first writing task in minutes.
            </p>
            <div className="mt-6 flex flex-wrap items-center justify-center gap-3">
              <Link
                href={user ? dashboardHref : "/register"}
                className="rounded-xl bg-gradient-to-r from-indigo-600 via-violet-600 to-indigo-600 px-6 py-3 text-base font-bold text-white shadow-xl shadow-indigo-600/30 transition-colors hover:from-indigo-500 hover:to-violet-500"
              >
                {user ? "Open your dashboard" : "Create a free account"}
              </Link>
            </div>
          </div>
        </section>
      </main>

      <footer className="border-t border-slate-800/60 py-8 text-center text-xs text-slate-500">
        IELTS AI Classroom · AI-powered practice — not a guarantee of exam results.
      </footer>
    </div>
  );
}
