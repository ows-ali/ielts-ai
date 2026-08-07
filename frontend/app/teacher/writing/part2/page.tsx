import { TeacherWritingDashboard } from "@/components/writing/teacher-dashboard";
import { Navbar } from "@/components/navbar";
import { requireTeacher } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function TeacherWritingPart2Page() {
  const { user, session } = await requireTeacher();

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole="teacher" userName={user.name} />
      <main className="mx-auto max-w-5xl px-4 py-8 sm:px-6">
        <div className="mb-6 rounded-2xl bg-gradient-to-r from-indigo-950 via-slate-900 to-indigo-900 p-6 text-white shadow-xl shadow-indigo-950/10">
          <span className="rounded-full bg-indigo-500/20 px-3 py-1 text-xs font-semibold text-indigo-300 border border-indigo-500/30">
            WRITING TASK 2 REVIEW
          </span>
          <h1 className="mt-2 text-2xl font-bold tracking-tight sm:text-3xl">
            Student Essay Submissions
          </h1>
          <p className="mt-1 text-sm text-indigo-200/80">
            Review student essays and leave feedback using the IELTS 4-criteria rubric. Multiple
            teachers can comment on the same submission.
          </p>
        </div>

        <TeacherWritingDashboard session={session} part={2} />
      </main>
    </div>
  );
}
