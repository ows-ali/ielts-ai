import { notFound } from "next/navigation";

import { TeacherRoomView } from "@/components/teacher/room-view";
import { api } from "@/lib/api";
import { requireTeacher } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function TeacherRoomPage({
  params,
}: {
  params: Promise<{ roomId: string }>;
}) {
  const { roomId } = await params;
  const { user, session } = await requireTeacher();
  let room;
  try {
    room = await api.getRoom(session, roomId);
  } catch {
    notFound();
  }
  if (room.teacher_id !== user.id) {
    notFound();
  }
  const participants = await api.participants(session, roomId);

  return <TeacherRoomView session={session} room={room} initialParticipants={participants} userName={user.name} />;
}
