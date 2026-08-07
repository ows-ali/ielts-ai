# Testing Guide & Strategy

## Overview
The IELTS AI Speaking Classroom uses a dual testing approach:
1. **Frontend**: Unit & Component tests with **Vitest**, **happy-dom**, and **React Testing Library (RTL)**.
2. **Backend**: End-to-End integration tests using an automated Python test runner script (`scripts/test_flow.py`) executing real requests against live Supabase and Gemini environments.

---

## Frontend Testing (Vitest)

### Stack & Setup
- **Framework**: Vitest (`vitest.config.mts`)
- **DOM Environment**: `happy-dom`
- **Setup File**: `frontend/vitest.setup.ts` (`@testing-library/jest-dom/vitest`)

### Key Test Files
```
frontend/__tests__/
├── app/
│   └── login.test.tsx           # Login form rendering & auth handler tests
├── components/
│   ├── audio-recorder.test.tsx  # MediaRecorder API mocking & recording flow
│   ├── create-room-form.test.tsx# Room creation form submission tests
│   ├── join-room-form.test.tsx  # Student room code entry tests
│   └── room-view.test.tsx       # Teacher live room view, realtime, and navigation
└── lib/
    └── api.test.ts              # API client methods & error handling tests
```

### Running Frontend Tests
```bash
cd frontend
npm test                # Run all tests once
npm run test:watch      # Watch mode for interactive development
```

### Mocking Patterns & Conventions
- **Supabase Mocks**: Mocks live inside `vi.hoisted()` blocks before module imports.
- **Unauthorized Handling**: Tests mock `useUnauthorizedRedirect` to catch 401 status errors.
- **Routing**: `next/navigation` (`useRouter`, `useSearchParams`, `notFound`) is mocked via `vi.mock("next/navigation", ...)` with standard router functions.

---

## Backend Testing (E2E Integration Flow)

### Strategy
Rather than using mocked HTTP endpoints, backend testing runs a sequential 12-step authorized e2e flow using `python -m scripts.test_flow`. This validates real database interactions, auth token decoding, RLS policies, audio upload paths, and Gemini scoring calls.

### Execution Command
```bash
cd backend
python -m scripts.test_flow
```

### E2E Flow Test Steps
1. **Supabase Connectivity**: Verifies connection to PostgreSQL database.
2. **Auth Verification**: Signs in dummy teacher (`teacher1@example.com`, password `TeacherSecure#2026`) and student (`student1@example.com`, password `DummyPass123!`).
3. **Room Creation**: Teacher creates a Part 1 speaking room (`POST /api/rooms`).
4. **Student Join**: Student joins room via code (`POST /api/rooms/join`).
5. **Participant Roster**: Verifies participant list (`GET /api/rooms/{id}/participants`).
6. **Start Room**: Teacher starts room (`POST /api/rooms/{id}/start`).
7. **Turn Verification**: Student checks turn state (`GET /api/rooms/{id}/turn`).
8. **Audio Upload**: Uploads sample test audio file to Supabase `audio` bucket.
9. **Submit Answer**: Student posts audio URL (`POST /api/rooms/{id}/answers`).
10. **Gemini Evaluation**: Asserts non-null evaluation scores (Fluency, Grammar, Vocab, Pronunciation, Overall Band).
11. **Student Report**: Fetches student report (`GET /api/students/me/report`) and checks attempt listing.
12. **End Room & Class Report**: Teacher ends session and validates class problem summary (`GET /api/rooms/{id}/report`).
