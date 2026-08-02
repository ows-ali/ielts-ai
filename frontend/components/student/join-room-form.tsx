"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import type { Session } from "@supabase/supabase-js";

import { Button } from "@/components/ui/button";
import { Input, Label } from "@/components/ui/input";
import { api } from "@/lib/api";
import { useUnauthorizedRedirect } from "@/lib/use-unauthorized";

export function JoinRoomForm({ session }: { session: Session }) {
  const router = useRouter();
  const handleUnauthorized = useUnauthorizedRedirect();
  const [code, setCode] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const room = await api.joinRoom(session, code);
      router.push(`/student/room/${room.id}`);
    } catch (err) {
      await handleUnauthorized(err);
      setError(err instanceof Error ? err.message : "Failed to join room");
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={onSubmit} className="space-y-4">
      <div>
        <Label htmlFor="code">Room code</Label>
        <Input
          id="code"
          value={code}
          onChange={(e) => setCode(e.target.value.toUpperCase())}
          placeholder="e.g. IELTS8291"
          className="font-mono text-lg tracking-widest"
          required
        />
      </div>
      {error && <p className="text-sm text-rose-600">{error}</p>}
      <Button type="submit" className="w-full" disabled={loading}>
        {loading ? "Joining..." : "Join room"}
      </Button>
    </form>
  );
}
