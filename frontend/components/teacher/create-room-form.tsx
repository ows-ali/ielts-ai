"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

import { Button } from "@/components/ui/button";
import { Input, Label } from "@/components/ui/input";
import { api } from "@/lib/api";
import type { Session } from "@supabase/supabase-js";

export function CreateRoomForm({ session }: { session: Session }) {
  const router = useRouter();
  const [title, setTitle] = useState("");
  const [part, setPart] = useState(1);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const room = await api.createRoom(session, title || "Speaking Practice", part);
      router.push(`/teacher/rooms/${room.id}`);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to create room");
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={onSubmit} className="space-y-4">
      <div>
        <Label htmlFor="title">Room title</Label>
        <Input
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Speaking Practice"
        />
      </div>
      <div>
        <Label htmlFor="part">IELTS Speaking Part</Label>
        <select
          id="part"
          value={part}
          onChange={(e) => setPart(Number(e.target.value))}
          className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm text-slate-900 focus:border-emerald-500 focus:outline-none focus:ring-2 focus:ring-emerald-500/30"
        >
          <option value={1}>Part 1</option>
          <option value={2}>Part 2</option>
          <option value={3}>Part 3</option>
        </select>
      </div>
      {error && <p className="text-sm text-rose-600">{error}</p>}
      <Button type="submit" className="w-full" disabled={loading}>
        {loading ? "Creating..." : "Create room"}
      </Button>
    </form>
  );
}
