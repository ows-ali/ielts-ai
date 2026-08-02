import { notFound } from "next/navigation";

import { StudentSpeakingSession } from "@/components/student/speaking-session";
import { api } from "@/lib/api";
import { requireStudent } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function StudentRoomPage({
  params,
}: {
  params: Promise<{ roomId: string }>;
}) {
  const { roomId } = await params;
  const { user, session } = await requireStudent();
  try {
    await api.getRoom(session, roomId);
  } catch {
    notFound();
  }

  return (
    <StudentSpeakingSession session={session} roomId={roomId} userId={user.id} />
  );
}
