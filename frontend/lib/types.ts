export type Role = "teacher" | "student";

export interface User {
  id: string;
  email: string | null;
  name: string | null;
  role: Role;
}

export interface Room {
  id: string;
  room_code: string;
  title: string;
  part: number;
  teacher_id: string;
  status: "waiting" | "live" | "ended";
  created_at?: string | null;
}

export interface Participant {
  id: string;
  room_id: string;
  student_id: string;
  student_name: string | null;
  status: "waiting" | "speaking" | "completed";
  joined_at?: string | null;
}

export interface Question {
  id: string;
  part: number;
  topic: string | null;
  question: string;
  difficulty?: string | null;
}

export interface TurnState {
  room_id: string;
  current_student_id: string | null;
  current_student_name: string | null;
  question_id: string | null;
  question: Question | null;
  status: "waiting" | "live" | "ended";
}

export interface Evaluation {
  id: string;
  answer_id: string;
  fluency: number;
  grammar: number;
  vocabulary: number;
  pronunciation: number;
  overall_band: number;
  feedback: string[];
}

export interface StudentAttempt {
  id: string;
  room_code?: string | null;
  title?: string | null;
  question: string;
  audio_url?: string | null;
  transcript?: string | null;
  fluency?: number | null;
  grammar?: number | null;
  vocabulary?: number | null;
  pronunciation?: number | null;
  overall_band?: number | null;
  feedback?: string[] | null;
  created_at?: string | null;
}

export interface StudentReport {
  student_id: string;
  attempts: StudentAttempt[];
}

export interface ParticipantScore {
  student_id: string;
  student_name: string | null;
  status: string;
  band: number | null;
}

export interface ClassReport {
  room_id: string;
  room_code: string;
  participants: ParticipantScore[];
  average_band: number | null;
  common_problems: string[];
}
