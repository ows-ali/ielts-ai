import type { Session } from "@supabase/supabase-js";

import type {
  ClassReport,
  Evaluation,
  Participant,
  Question,
  Room,
  RoomScoresOut,
  StudentReport,
  TurnState,
  User,
} from "@/lib/types";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export class ApiError extends Error {
  status: number;
  constructor(status: number, message: string) {
    super(message);
    this.status = status;
  }
}

async function request<T>(
  path: string,
  session: Session | null,
  init?: RequestInit
): Promise<T> {
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
  };
  if (session?.access_token) {
    headers.Authorization = `Bearer ${session.access_token}`;
  }
  const res = await fetch(`${API_BASE}${path}`, {
    ...init,
    headers: { ...headers, ...(init?.headers || {}) },
    cache: "no-store",
  });
  if (!res.ok) {
    let detail = res.statusText;
    try {
      const body = await res.json();
      detail = body.detail ?? detail;
    } catch {
      /* ignore */
    }
    throw new ApiError(res.status, typeof detail === "string" ? detail : JSON.stringify(detail));
  }
  return res.json() as Promise<T>;
}

export const api = {
  me: (s: Session | null) => request<User>("/api/auth/me", s),

  createRoom: (s: Session | null, title: string, part: number) =>
    request<Room>("/api/rooms", s, {
      method: "POST",
      body: JSON.stringify({ title, part }),
    }),

  listRooms: (s: Session | null) => request<Room[]>("/api/rooms", s),

  getRoom: (s: Session | null, id: string) =>
    request<Room>(`/api/rooms/${id}`, s),

  joinRoom: (s: Session | null, code: string) =>
    request<Room>("/api/rooms/join", s, {
      method: "POST",
      body: JSON.stringify({ room_code: code }),
    }),

  participants: (s: Session | null, id: string) =>
    request<Participant[]>(`/api/rooms/${id}/participants`, s),

  setRoomStatus: (s: Session | null, id: string, status: string) =>
    request<Room>(`/api/rooms/${id}/status`, s, {
      method: "POST",
      body: JSON.stringify({ status }),
    }),

  startRoom: (s: Session | null, id: string) =>
    request<TurnState>(`/api/rooms/${id}/start`, s, { method: "POST" }),

  endRoom: (s: Session | null, id: string) =>
    request<Room>(`/api/rooms/${id}/end`, s, { method: "POST" }),

  turn: (s: Session | null, id: string) =>
    request<TurnState>(`/api/rooms/${id}/turn`, s),

  getQuestion: (s: Session | null, id: string) =>
    request<Question>(`/api/rooms/${id}/turn`, s).then((t) => t.question),

  submitAnswer: (
    s: Session | null,
    roomId: string,
    questionId: string,
    audioUrl: string,
    transcript?: string
  ) =>
    request<Evaluation>(`/api/rooms/${roomId}/answers`, s, {
      method: "POST",
      body: JSON.stringify({ room_id: roomId, question_id: questionId, audio_url: audioUrl, transcript }),
    }),

  studentReport: (s: Session | null) =>
    request<StudentReport>("/api/students/me/report", s),

  classReport: (s: Session | null, roomId: string) =>
    request<ClassReport>(`/api/rooms/${roomId}/report`, s),

  roomScores: (s: Session | null, roomId: string) =>
    request<RoomScoresOut>(`/api/rooms/${roomId}/scores`, s),
};
