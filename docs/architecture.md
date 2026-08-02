# Architecture Overview

## High-Level Data Flow

```
┌─────────────┐     SSR/CSR      ┌─────────────┐     REST      ┌─────────────┐
│   Browser   │ ◄──────────────► │  Next.js 15 │ ◄────────────► │   FastAPI   │
│  (React 19) │   SSR + CSR      │  (App Router)│   /api/*       │  (Python)   │
└─────────────┘                  └─────────────┘                └──────┬──────┘
                                                                       │
                        ┌──────────────────────────────────────────────┼──────────┐
                        ▼                                              ▼          ▼
                 ┌─────────────┐                               ┌─────────────┐ ┌─────────┐
                 │  Supabase   │                               │   Gemini    │ │ Storage │
                 │  (PostgreSQL)│                               │  (gemini-   │ │ (audio) │
                 │  + GoTrue   │                               │   3.5-flash)│ │         │
                 │  + Realtime │                               └─────────────┘ └─────────┘
                 └─────────────┘
```

## Supabase Schema

### Core Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| `users` | Teacher/Student profiles | `id`, `email`, `name`, `role` (teacher/student) |
| `rooms` | Speaking practice rooms | `id`, `room_code`, `title`, `part` (1-3), `teacher_id`, `status` (waiting/live/ended) |
| `participants` | Students in rooms | `id`, `room_id`, `student_id`, `student_name`, `status` (waiting/speaking/completed) |
| `questions` | IELTS Speaking prompts | `id`, `part`, `topic`, `question`, `difficulty` |
| `answers` | Student audio submissions | `id`, `room_id`, `student_id`, `question_id`, `audio_url`, `transcript`, `created_at` |
| `evaluations` | Gemini scoring | `id`, `answer_id`, `student_id`, `fluency`, `grammar`, `vocabulary`, `pronunciation`, `overall_band`, `feedback[]`, `created_at` |

### Relationships
- `rooms.teacher_id` → `users.id`
- `participants.room_id` → `rooms.id`, `participants.student_id` → `users.id`
- `answers.room_id` → `rooms.id`, `answers.student_id` → `users.id`, `answers.question_id` → `questions.id`
- `evaluations.answer_id` → `answers.id`, `evaluations.student_id` → `users.id`

## Realtime Subscriptions

| Channel | Filter | Purpose |
|---------|--------|---------|
| `room-{room_id}` | `rooms.id=eq.{room_id}` | Teacher: room status, participant changes |
| `room-{room_id}` | `participants.room_id=eq.{room_id}` | Teacher: student join/leave/status |
| `student-room-{room_id}` | `rooms.id=eq.{room_id}` | Student: turn changes, room status |
| `student-room-{room_id}` | `participants.room_id=eq.{room_id}` | Student: own status updates |

**Frontend**: `supabase.channel().on('postgres_changes', {...}, refresh).subscribe()`

**Cleanup**: `supabase.removeChannel(channel)` on unmount

## Auth Flow

```
1. User signs in (email/password) → Supabase GoTrue
2. Session stored in SSR cookies (@supabase/ssr)
3. Frontend server components: getSession() → cookies → Supabase
4. Client components: createClient() → browser session
5. API calls: Authorization: Bearer <access_token>
6. Backend: GET /auth/v1/user with apikey + Bearer token
7. Supabase validates JWT (ES256) → returns user or 401
8. Backend extracts role from user_metadata/app_metadata
```

**Token Lifetime**: ~1 hour (Supabase default). Expired tokens → 401 "Invalid token"

## Storage

| Bucket | Purpose | Access |
|--------|---------|--------|
| `audio` | Student recordings (webm/mp4) | Public read, authenticated write via RLS |

**RLS Policies**:
- `authenticated can upload audio`: `bucket_id='audio'` + `auth.role() = 'authenticated'` (INSERT)
- `authenticated can read audio`: `bucket_id='audio'` + `auth.role() = 'authenticated'` (SELECT)

**Upload Flow**: Student records → blob → `supabase.storage.from('audio').upload(path, blob)` → `getPublicUrl(path)` → `audio_url` stored in `answers` table

## Gemini Integration

| Task | Model | Prompt Strategy |
|------|-------|-----------------|
| Speaking evaluation | `gemini-3.5-flash` | Structured output (fluency, grammar, vocab, pronunciation, overall_band, feedback[]) |
| STT (speech-to-text) | `gemini-3.5-flash` | Audio file → transcript |
| Class problem summary | `gemini-3.5-flash` | Aggregated evaluations → common problems list |
| Embeddings | `gemini-embedding-2` (768d) | Not currently used (future: semantic search) |

**Free Tier Limits**: 60 RPM, 1M tokens/day. Quota exceeded → 429.

## Key Files

| Area | Files |
|------|-------|
| Supabase client (frontend) | `frontend/lib/supabase/client.ts`, `server.ts`, `middleware.ts` |
| Supabase client (backend) | `backend/app/services/supabase_client.py` |
| Auth (frontend) | `frontend/lib/auth.ts`, `middleware.ts` |
| Auth (backend) | `backend/app/core/security.py` |
| DB queries | `backend/app/services/db.py` |
| Realtime channels | `frontend/components/teacher/room-view.tsx`, `student/speaking-session.tsx` |
| Gemini | `backend/app/services/gemini.py`, `backend/app/api/routes/speaking.py` |
| Storage upload | `frontend/components/student/speaking-session.tsx` (handleRecorded) |