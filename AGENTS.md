# IELTS AI Speaking Classroom — Agent Guide

## Stack
- **Frontend**: Next.js 15.5 (App Router, React 19), Tailwind CSS 4, @supabase/ssr, Vitest + happy-dom + RTL
- **Backend**: FastAPI, Supabase (async client), Google Gemini (`gemini-3.5-flash`), uvicorn
- **Database/Auth/Storage/Realtime**: Supabase (PostgreSQL + GoTrue + Storage + Realtime)
- **Language**: TypeScript (frontend), Python 3.12 (backend)

## Key Commands
```bash
# Frontend
cd frontend
npm run dev          # Dev server (webpack)
npm run build        # Production build (turbopack)
npm run lint         # ESLint
npm test             # Vitest (38 tests)

# Backend
cd backend
uvicorn app.main:app --reload  # Dev server :8000
python -m scripts.test_flow    # Full authorized e2e (12 steps)

# Supabase SQL (run in dashboard)
alter publication supabase_realtime add table public.rooms, public.participants;
```

## Environment Variables
| Variable | Frontend | Backend | Description |
|----------|----------|---------|-------------|
| `NEXT_PUBLIC_SUPABASE_URL` | ✅ | | Supabase project URL |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | ✅ | | Supabase anon key |
| `NEXT_PUBLIC_API_URL` | ✅ | | Backend URL (default: http://localhost:8000) |
| `SUPABASE_URL` | | ✅ | Supabase project URL |
| `SUPABASE_SERVICE_ROLE_KEY` | | ✅ | Supabase service role key |
| `SUPABASE_ANON_KEY` | | ✅ | Supabase anon key (for token verification) |
| `GEMINI_API_KEY` | | ✅ | Google AI Studio API key |
| `GEMINI_EVAL_MODEL` | | ✅ | `gemini-3.5-flash` (eval + STT) |
| `GROQ_API_KEY` | | ✅ | Optional: Groq Cloud API key (`whisper-large-v3-turbo` STT fallback) |

## Current Status (2026-08-02)
- ✅ Frontend tests: 38/38 passing, lint clean, typecheck clean
- ✅ Backend e2e: 12/12 passing (real Supabase + Gemini)
- ✅ 401 handling: `useUnauthorizedRedirect` hook + 5 components + 4 tests
- ✅ Polling removed (realtime-only updates)
- ✅ Dummy users: teacher1/2, student1/2 (password: DummyPass123!)
- ✅ Servers stopped (ports 3000/8000 free)
- ✅ Teacher home button added to room header navigation
- ✅ Student reports with audio playback controls added
- ✅ Complete system documentation created (`api.md`, `testing.md`, `deployment.md`, `project-state.md`)

## Conventions
- **Frontend tests**: `vitest` + happy-dom + RTL; mocks via `vi.hoisted` + `vi.mock`; `useUnauthorizedRedirect` for 401s
- **Backend tests**: `scripts/test_flow.py` (real Supabase + Gemini, self-cleaning)
- **Supabase**: RLS on `storage.objects` (audio bucket), realtime on `rooms` + `participants`
- **Auth**: SSR cookies → FastAPI Bearer token → Supabase `/auth/v1/user` verification (ES256)
- **Gemini**: `gemini-3.5-flash` for eval + STT (free tier); `gemini-embedding-2` @ 768d

## Quick Links
- Supabase Dashboard: https://supabase.com/dashboard/project/yulczbyfhdsyvbjjqmah
- Frontend: `http://localhost:3000` (dev)
- Backend: `http://localhost:8000` (dev), `/api/health`