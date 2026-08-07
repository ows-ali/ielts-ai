import type { Session } from "@supabase/supabase-js";

import type {
  BadgeSummary,
  ClassReport,
  Community,
  Evaluation,
  Participant,
  PublicProfile,
  Question,
  Room,
  RoomScoresOut,
  StudentReport,
  TurnState,
  User,
  WritingFeedback,
  WritingQuestion,
  WritingQuestionDetail,
  WritingSample,
  WritingSubmission,
  WritingSubmissionDetail,
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

  writingQuestions: (
    s: Session | null,
    params?: { type?: string; difficulty?: string; part?: number }
  ) => {
    const qs = new URLSearchParams();
    if (params?.type) qs.set("type", params.type);
    if (params?.difficulty) qs.set("difficulty", params.difficulty);
    if (params?.part) qs.set("part", String(params.part));
    const q = qs.toString();
    return request<WritingQuestion[]>(`/api/writing/questions${q ? `?${q}` : ""}`, s);
  },

  writingQuestion: (s: Session | null, id: string) =>
    request<WritingQuestionDetail>(`/api/writing/questions/${id}`, s),

  writingSamples: (s: Session | null, id: string) =>
    request<WritingSample[]>(`/api/writing/questions/${id}/samples`, s).catch(
      () => []
    ),

  submitWriting: (s: Session | null, questionId: string, answerText: string, part?: number) =>
    request<WritingSubmission>("/api/writing/submissions", s, {
      method: "POST",
      body: JSON.stringify({
        question_id: questionId,
        answer_text: answerText,
        ...(part ? { part } : {}),
      }),
    }),

  myWritingSubmissions: (s: Session | null, part?: number) => {
    const qs = new URLSearchParams();
    if (part) qs.set("part", String(part));
    const q = qs.toString();
    return request<WritingSubmission[]>(`/api/writing/submissions/me${q ? `?${q}` : ""}`, s);
  },

  allWritingSubmissions: (s: Session | null, part?: number) => {
    const qs = new URLSearchParams();
    if (part) qs.set("part", String(part));
    const q = qs.toString();
    return request<WritingSubmission[]>(`/api/writing/submissions${q ? `?${q}` : ""}`, s);
  },

  writingSubmission: (s: Session | null, id: string) =>
    request<WritingSubmissionDetail>(`/api/writing/submissions/${id}`, s),

  giveWritingFeedback: (
    s: Session | null,
    submissionId: string,
    scores: {
      task_achievement: number;
      coherence_cohesion: number;
      lexical_resource: number;
      grammatical_range: number;
      overall_comment?: string | null;
    }
  ) =>
    request<WritingFeedback>("/api/writing/feedback", s, {
      method: "POST",
      body: JSON.stringify({ submission_id: submissionId, ...scores }),
    }),

  myBadges: (s: Session | null) => request<BadgeSummary>("/api/me/badges", s),

  publicProfile: (s: Session | null, userId: string) =>
    request<PublicProfile>(`/api/users/${userId}/profile`, s),

  community: (s: Session | null) => request<Community>("/api/community", s),
};
