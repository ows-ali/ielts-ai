import Link from "next/link";

import { CreateRoomForm } from "@/components/teacher/create-room-form";
import { Navbar } from "@/components/navbar";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { api } from "@/lib/api";
import { requireTeacher } from "@/lib/auth";

const STATUS_STYLES: Record<string, string> = {
  waiting: "bg-slate-100 text-slate-600 border-slate-200",
  live: "bg-emerald-50 text-emerald-700 border-emerald-200",
  ended: "bg-amber-50 text-amber-700 border-amber-200",
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
    <div className="min-h-screen bg-slate-50/50">
      <Navbar userRole="teacher" userName={user.name} />

      <main className="mx-auto max-w-5xl px-4 py-8 sm:px-6">
        <div className="mb-6 rounded-2xl bg-gradient-to-r from-indigo-950 via-slate-900 to-indigo-900 p-6 text-white shadow-xl shadow-indigo-950/10">
          <div className="flex items-center justify-between">
            <div>
              <span className="rounded-full bg-indigo-500/20 px-3 py-1 text-xs font-semibold text-indigo-300 border border-indigo-500/30">
                TEACHER DASHBOARD
              </span>
              <h1 className="mt-2 text-2xl font-bold tracking-tight sm:text-3xl">
                Classroom Control Center
              </h1>
              <p className="mt-1 text-sm text-indigo-200/80">
                Create new speaking rooms, manage active turns, and review student performance reports.
              </p>
            </div>
          </div>
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
    </div>
  );
}
