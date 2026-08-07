# IELTS AI Speaking Classroom

Collaborative AI-powered IELTS practice. Teachers run live speaking
rooms; students join with a code, answer IELTS questions by voice, get AI
feedback, and teachers see a class report. Students can also practise
**Writing Task 1** and **Writing Task 2** independently and receive manual
feedback from teachers.

Built from `PRD.md`.

## Features

- **Live speaking rooms**: teachers create Part 1/2/3 rooms, students join
  with a code and answer by voice; Gemini transcribes and evaluates against
  the IELTS band descriptors.
- **Class reports**: teachers see live progress and a summary of common
  weaknesses; students see their history and audio playback.
- **Writing practice** (not room-bound):
  - **Task 1**: 26 curated questions across all 7 Task 1 types (line, bar, pie,
    table, map, process, multiple charts).
  - **Task 2**: 24 essay questions across all 6 essay types (opinion,
    discussion, advantages & disadvantages, problem & solution,
    positive/negative development, two-part questions).
  - 3 model answers per question at Band 5, 7 and 9, each with criterion
    sub-scores, a "why this band" explanation and improvement tips.
  - Untimed, individual practice with a word counter (150-word target for
    Task 1, 250-word target for Task 2) and draft autosave.
  - Multiple teachers can leave feedback on any submission; students see all
    feedback and an overall band.

## Architecture

```
Next.js 15 (frontend)  ──▶  FastAPI (backend)  ──▶  Supabase (Postgres, Auth, Realtime, Storage)
                                        │
                                        ▼
                               Gemini API (2.5 Pro eval / 2.5 Flash STT) + pgvector RAG
```

The writing module uses the same Supabase + FastAPI stack. Writing question
diagrams live in `frontend/public/writing-images/` and are served by Next.js
(no storage bucket needed).

## Prerequisites

- Node.js 20+
- Python 3.12+
- A Supabase project (free tier)
- A Google Gemini API key (your Gemini Pro / Google AI Studio account)

## 1. Supabase setup

1. Create a project at https://supabase.com.
2. In **SQL Editor**, run the migrations in order:
   - `backend/migrations/001_users.sql`
   - `backend/migrations/002_rooms_participants.sql`
   - `backend/migrations/003_questions.sql`
   - `backend/migrations/004_answers_evaluations.sql`
   - `backend/migrations/005_criteria.sql`
   - `backend/supabase/migrations/20260805_writing_tables.sql` (writing module)
   - `backend/supabase/migrations/20260807_writing_part2.sql` (Task 2 support)
3. Create a **public** storage bucket named `audio` (Storage → New bucket,
   uncheck "restrict file uploads"). Audio recordings live here.
4. Enable Realtime on the `rooms` and `participants` tables if you want live
   turn updates (the UI also polls as a fallback).
5. For **password reset**, add the reset page to Auth → URL Configuration →
   Redirect URLs: `http://localhost:3000/reset-password` (dev) and
   `https://<your-vercel-domain>/reset-password` (prod). Emails are sent via
   the Supabase email provider (Auth → Providers → Email enabled; already
   required for signup confirmation).

> Writing question diagrams are committed under `frontend/public/writing-images/`
> and served directly by the frontend — no bucket upload required.

## 2. Seed the RAG knowledge base

The IELTS band descriptors are stored with vector embeddings for retrieval.

```bash
cd backend
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt     # Windows
cp .env.example .env                              # fill in the values
.venv\Scripts\python -m scripts.seed_criteria
.venv\Scripts\python -m scripts.seed_writing        # 26 Task 1 + 24 Task 2 questions (150 samples)
```

### Backend env vars (`.env`)

| Variable | Description |
|---|---|
| `SUPABASE_URL` | Project URL (Settings → API) |
| `SUPABASE_SERVICE_ROLE_KEY` | Service role key (Settings → API) |
| `SUPABASE_ANON_KEY` | Anon/publishable key — used to verify access tokens against the Auth server |
| `GEMINI_API_KEY` | Google AI Studio API key |
| `CORS_ORIGINS` | Comma-separated frontend origins allowed by CORS |

> Note: the backend verifies Supabase access tokens via the Auth server
> (`/auth/v1/user`), so the JWT secret / JWT Signing Keys are not needed.

## 3. Run the backend

```bash
cd backend
.venv\Scripts\python -m uvicorn app.main:app --reload --port 8000
# API docs at http://localhost:8000/docs
```

## 4. Run the frontend

```bash
cd frontend
cp .env.example .env.local                        # fill in the values
npm install
npm run dev                                       # http://localhost:3000
```

### Frontend env vars (`.env.local`)

| Variable | Description |
|---|---|
| `NEXT_PUBLIC_SUPABASE_URL` | Supabase project URL |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Supabase anon key |
| `NEXT_PUBLIC_API_URL` | Backend base URL, e.g. `http://localhost:8000` |

## Using the app

1. **Register** as a teacher or student (email + password).
2. **Forgot your password?** Use the **Forgot password?** link on the sign-in
   page — you'll get an email with a link to set a new password on the
   `/reset-password` page.
3. **Teacher**: create a room, choose Part 1/2/3, share the room code →
   start the session when students join.
4. **Student**: enter the room code, wait for your turn, record your answer.
5. The AI transcribes (Gemini Flash), evaluates against the IELTS band
   descriptors (Gemini Pro + RAG), and returns a band score with feedback.
6. **Teacher** sees live progress and a class report with average band and
   common problems. **Students** see their history in *My progress*.

### Writing practice

1. **Student**: open **Writing → Task 1 Practice** or **Task 2 Practice**, filter
   by type or difficulty, and pick any question.
2. Read the prompt, study the diagram/chart (Task 1) or essay question (Task 2),
   and write your answer with the built-in editor (150-word target for Task 1,
   250-word target for Task 2, draft autosave).
3. Compare your work with the Band 5 / 7 / 9 sample answers and their
   "why this band" explanations.
4. Submit for review; any teacher can score it on the 4 IELTS criteria and
   leave feedback. Students see all feedback and the average overall band.
5. **Teacher**: open **Writing → Task 1** or **Task 2** review to review pending
   submissions and grade them.

## Deployment

- **Frontend**: Vercel (set the env vars above). Vercel **Web Analytics** and
  **Speed Insights** are enabled via `@vercel/analytics` and
  `@vercel/speed-insights`; they activate automatically on Vercel
  deployments and no env vars are required.
- **Backend**: Render / Railway (set env vars; `uvicorn app.main:app`).
- **Database**: Supabase Cloud (already hosted).

All free tiers are sufficient for the MVP. No paid tools are required.
