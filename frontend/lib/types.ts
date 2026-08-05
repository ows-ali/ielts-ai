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
  room_id?: string | null;
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
  audio_url?: string | null;
  transcript?: string | null;
  question?: string | null;
  fluency?: number | null;
  grammar?: number | null;
  vocabulary?: number | null;
  pronunciation?: number | null;
  feedback?: string[] | null;
}

export interface ClassReport {
  room_id: string;
  room_code: string;
  participants: ParticipantScore[];
  average_band: number | null;
  common_problems: string[];
}

export interface RoomScoresOut {
  room_id: string;
  room_code: string;
  participants: ParticipantScore[];
}

export type WritingQuestionType =
  | "line"
  | "bar"
  | "pie"
  | "table"
  | "map"
  | "process"
  | "multi";

export interface WritingQuestion {
  id: string;
  type: WritingQuestionType;
  title: string;
  prompt: string;
  data_description?: Record<string, unknown> | null;
  image_url?: string | null;
  difficulty?: string | null;
}

export interface WritingSample {
  id: string;
  band: number;
  answer_text: string;
  task_achievement: number;
  coherence_cohesion: number;
  lexical_resource: number;
  grammatical_range: number;
  explanation: string;
  improvement_tips: string[];
}

export interface WritingQuestionDetail extends WritingQuestion {
  samples: WritingSample[];
}

export interface WritingFeedback {
  id: string;
  submission_id: string;
  teacher_id: string;
  teacher_name?: string | null;
  task_achievement: number;
  coherence_cohesion: number;
  lexical_resource: number;
  grammatical_range: number;
  overall_band: number;
  overall_comment?: string | null;
  created_at?: string | null;
}

export interface WritingSubmission {
  id: string;
  question_id: string;
  question_title?: string | null;
  question_type?: string | null;
  answer_text: string;
  word_count?: number | null;
  created_at?: string | null;
  feedback: WritingFeedback[];
  overall_band?: number | null;
}

export interface WritingSubmissionDetail extends WritingSubmission {
  question_prompt?: string | null;
  question_data?: Record<string, unknown> | null;
  question_image_url?: string | null;
  question_difficulty?: string | null;
}
