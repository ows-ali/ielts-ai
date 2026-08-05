import Link from "next/link";

import { WritingHistory } from "@/components/writing/writing-history";
import { Navbar } from "@/components/navbar";
import { Button } from "@/components/ui/button";
import { requireStudent } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function StudentWritingHistoryPage() {
  const { user, session } = await requireStudent();

  return (
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole="student" userName={user.name} />
      <main className="mx-auto max-w-4xl px-4 py-8 sm:px-6">
        <div className="mb-6 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl">
              My Writing Submissions
            </h1>
            <p className="text-sm text-slate-500">
              Review your answers and read feedback from your teachers.
            </p>
          </div>
          <div className="flex gap-2">
            <Link href="/student/writing">
              <Button variant="secondary">← Back to practice</Button>
            </Link>
          </div>
        </div>

        <WritingHistory session={session} />
      </main>
    </div>
  );
}
