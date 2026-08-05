import { notFound } from "next/navigation";

import { WritingSubmissionView } from "@/components/writing/writing-submission-view";
import { api } from "@/lib/api";
import { requireStudent } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function StudentWritingSubmissionPage({
  params,
}: {
  params: Promise<{ submissionId: string }>;
}) {
  const { submissionId } = await params;
  const { user, session } = await requireStudent();
  let submission;
  try {
    submission = await api.writingSubmission(session, submissionId);
  } catch {
    notFound();
  }

  return <WritingSubmissionView submission={submission} userName={user.name} />;
}
