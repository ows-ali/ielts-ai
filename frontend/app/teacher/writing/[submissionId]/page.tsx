import { notFound } from "next/navigation";

import { TeacherWritingReview } from "@/components/writing/teacher-writing-review";
import { api } from "@/lib/api";
import { requireTeacher } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function TeacherWritingReviewPage({
  params,
}: {
  params: Promise<{ submissionId: string }>;
}) {
  const { submissionId } = await params;
  const { user, session } = await requireTeacher();
  let submission;
  try {
    submission = await api.writingSubmission(session, submissionId);
  } catch {
    notFound();
  }

  return (
    <TeacherWritingReview session={session} submission={submission} userName={user.name} />
  );
}
