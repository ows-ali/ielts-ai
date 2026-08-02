import Link from "next/link";

import { JoinRoomForm } from "@/components/student/join-room-form";
import { SignOutButton } from "@/components/sign-out-button";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { requireStudent } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function StudentPage() {
  const { user, session } = await requireStudent();

  return (
    <main className="mx-auto max-w-2xl p-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">Student</h1>
          <p className="text-sm text-slate-500">Welcome, {user.name}</p>
        </div>
        <SignOutButton />
      </div>

      <div className="mt-6 grid gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Join a session</CardTitle>
          </CardHeader>
          <CardContent>
            <JoinRoomForm session={session} />
          </CardContent>
        </Card>

        <Card>
          <CardContent>
            <Link href="/student/report" className="inline-block w-full">
              <Button variant="secondary" className="w-full">
                View my progress report
              </Button>
            </Link>
          </CardContent>
        </Card>
      </div>
    </main>
  );
}
