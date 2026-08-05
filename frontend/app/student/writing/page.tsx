import Link from "next/link";

import { WritingDashboard } from "@/components/writing/student-dashboard";
import { Navbar } from "@/components/navbar";
import { requireStudent } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function StudentWritingPage() {
  const { user, session } = await requireStudent();

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole="student" userName={user.name} />
      <main className="mx-auto max-w-5xl px-4 py-8 sm:px-6">
        <div className="mb-6 rounded-2xl bg-gradient-to-r from-indigo-950 via-slate-900 to-indigo-900 p-6 text-white shadow-xl shadow-indigo-950/10">
          <div className="flex items-center justify-between">
            <div>
              <span className="rounded-full bg-indigo-500/20 px-3 py-1 text-xs font-semibold text-indigo-300 border border-indigo-500/30">
                WRITING TASK 1 PRACTICE
              </span>
              <h1 className="mt-2 text-2xl font-bold tracking-tight sm:text-3xl">
                Academic Writing, Part 1
              </h1>
              <p className="mt-1 text-sm text-indigo-200/80">
                Practice any question type as many times as you like. Read model answers for Band
                5, 7 and 9, and get feedback from your teachers.
              </p>
            </div>
            <Link
              href="/student/writing/history"
              className="shrink-0 rounded-lg bg-white/10 px-3.5 py-2 text-sm font-semibold text-white backdrop-blur-md border border-white/15 transition-colors hover:bg-white/20"
            >
              My submissions →
            </Link>
          </div>
        </div>

        <WritingDashboard session={session} />
      </main>
    </div>
  );
}
