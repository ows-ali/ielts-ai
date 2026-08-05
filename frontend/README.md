# Frontend — IELTS AI Speaking Classroom

Next.js 15 (App Router, React 19) frontend for the IELTS AI Speaking
Classroom. Talks to the FastAPI backend and Supabase for auth, realtime and
storage.

## Getting Started

Copy the example env file and fill in the values (Supabase project URL + anon
key, backend API URL):

```bash
cp .env.example .env.local
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start the dev server (webpack) |
| `npm run build` | Production build (turbopack) |
| `npm run start` | Serve a production build |
| `npm run lint` | ESLint |
| `npm test` | Vitest test suite |

## Structure

- `app/` — App Router pages (`/student/*`, `/teacher/*`, auth).
- `components/` — Shared UI and feature components (`writing/` holds the
  Writing Task 1 module).
- `lib/` — Supabase client, API client and shared types.
- `public/writing-images/` — Static Writing Task 1 diagrams served at
  `/writing-images/...`.

## Analytics

Web Analytics (`@vercel/analytics`) and Speed Insights
(`@vercel/speed-insights`) are mounted in `app/layout.tsx` and activate
automatically on Vercel deployments.

See the [root README](../README.md) for full setup and deployment docs.
