import Link from "next/link";

import { CreateRoomForm } from "@/components/teacher/create-room-form";
import { SignOutButton } from "@/components/sign-out-button";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { api } from "@/lib/api";
import { requireTeacher } from "@/lib/auth";

const STATUS_STYLES: Record<string, string> = {
  waiting: "bg-slate-100 text-slate-600",
  live: "bg-emerald-100 text-emerald-700",
  ended: "bg-amber-100 text-amber-700",
};

export const dynamic = "force-dynamic";

export default async function TeacherPage() {
  const { user, session } = await requireTeacher();
  let rooms: Awaited<ReturnType<typeof api.listRooms>> = [];
  try {
    rooms = await api.listRooms(session);
  } catch {
    rooms = [];
  }

  return (
    <main className="mx-auto max-w-4xl p-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">Teacher Dashboard</h1>
          <p className="text-sm text-slate-500">Welcome, {user.name}</p>
        </div>
        <SignOutButton />
      </div>

      <div className="mt-6 grid gap-6 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Create a room</CardTitle>
          </CardHeader>
          <CardContent>
            <CreateRoomForm session={session} />
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Your rooms</CardTitle>
          </CardHeader>
          <CardContent>
            {rooms.length === 0 ? (
              <p className="text-sm text-slate-500">
                No rooms yet. Create one to get a shareable room code.
              </p>
            ) : (
              <ul className="space-y-2">
                {rooms.map((room) => (
                  <li key={room.id}>
                    <Link
                      href={`/teacher/rooms/${room.id}`}
                      className="flex items-center justify-between rounded-lg border border-slate-200 p-3 transition-colors hover:border-emerald-500"
                    >
                      <div>
                        <p className="font-medium">{room.title}</p>
                        <p className="text-xs text-slate-500">
                          Code: <span className="font-mono font-semibold">{room.room_code}</span> · Part {room.part}
                        </p>
                      </div>
                      <Badge className={STATUS_STYLES[room.status] ?? ""}>
                        {room.status}
                      </Badge>
                    </Link>
                  </li>
                ))}
              </ul>
            )}
          </CardContent>
        </Card>
      </div>
    </main>
  );
}
