# IELTS AI Speaking Classroom

Collaborative AI-powered IELTS speaking practice. Teachers run live speaking
rooms; students join with a code, answer IELTS questions by voice, get AI
feedback, and teachers see a class report.

Built from `PRD.md`.

## Architecture

```
Next.js 15 (frontend)  ──▶  FastAPI (backend)  ──▶  Supabase (Postgres, Auth, Realtime, Storage)
                                        │
                                        ▼
                               Gemini API (2.5 Pro eval / 2.5 Flash STT) + pgvector RAG
```

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
3. Create a **public** storage bucket named `audio` (Storage → New bucket,
   uncheck "restrict file uploads"). Audio recordings live here.
4. Enable Realtime on the `rooms` and `participants` tables if you want live
   turn updates (the UI also polls as a fallback).

## 2. Seed the RAG knowledge base

The IELTS band descriptors are stored with vector embeddings for retrieval.

```bash
cd backend
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt     # Windows
cp .env.example .env                              # fill in the values
.venv\Scripts\python -m scripts.seed_criteria
```

### Backend env vars (`.env`)

| Variable | Description |
|---|---|
| `SUPABASE_URL` | Project URL (Settings → API) |
| `SUPABASE_SERVICE_ROLE_KEY` | Service role key (Settings → API) |
| `SUPABASE_JWT_SECRET` | JWT Secret (Settings → API) — used to verify auth tokens |
| `SUPABASE_ANON_KEY` | Anon/publishable key |
| `GEMINI_API_KEY` | Google AI Studio API key |
| `FRONTEND_URL` | `http://localhost:3000` for local dev |

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
2. **Teacher**: create a room, choose Part 1/2/3, share the room code →
   start the session when students join.
3. **Student**: enter the room code, wait for your turn, record your answer.
4. The AI transcribes (Gemini Flash), evaluates against the IELTS band
   descriptors (Gemini Pro + RAG), and returns a band score with feedback.
5. **Teacher** sees live progress and a class report with average band and
   common problems. **Students** see their history in *My progress*.

## Deployment

- **Frontend**: Vercel (set the env vars above).
- **Backend**: Render / Railway (set env vars; `uvicorn app.main:app`).
- **Database**: Supabase Cloud (already hosted).

All free tiers are sufficient for the MVP. No paid tools are required.
