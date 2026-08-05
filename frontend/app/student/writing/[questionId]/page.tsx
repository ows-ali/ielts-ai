import { notFound } from "next/navigation";

import { WritingPractice } from "@/components/writing/writing-practice";
import { api } from "@/lib/api";
import { requireStudent } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function StudentWritingQuestionPage({
  params,
}: {
  params: Promise<{ questionId: string }>;
}) {
  const { questionId } = await params;
  const { user, session } = await requireStudent();
  let question;
  try {
    question = await api.writingQuestion(session, questionId);
  } catch {
    notFound();
  }

  return <WritingPractice session={session} question={question} userName={user.name} />;
}
