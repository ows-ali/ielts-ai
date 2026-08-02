# Frontend Architecture

## Tech Stack
- **Framework**: Next.js 15.5 (App Router, React 19)
- **Styling**: Tailwind CSS 4
- **Auth**: @supabase/ssr (SSR cookies + client-side session)
- **Testing**: Vitest + happy-dom + React Testing Library
- **Language": TypeScript (strict mode)

## Project Structure
frontend/
+-- app/                    # App Router pages (server components by default)
¦   +-- layout.tsx          # Root layout, fonts, metadata
¦   +-- page.tsx            # Landing page
¦   +-- login/page.tsx      # Email/password sign in
¦   +-- register/page.tsx   # Sign up
¦   +-- teacher/
¦   ¦   +-- page.tsx        # Teacher dashboard (rooms list + create)
¦   ¦   +-- rooms/[roomId]/page.tsx  # Teacher room screen
¦   +-- student/
¦   ¦   +-- page.tsx        # Student dashboard (join room)
¦   ¦   +-- room/[roomId]/page.tsx   # Student speaking session
¦   ¦   +-- report/page.tsx  # Student progress report
¦   +-- globals.css         # Tailwind imports
+-- components/
¦   +-- teacher/
¦   ¦   +-- room-view.tsx       # Main teacher room screen
¦   ¦   +-- create-room-form.tsx
¦   +-- student/
¦   ¦   +-- speaking-session.tsx  # Student turn + recording
¦   ¦   +-- audio-recorder.tsx    # MediaRecorder wrapper
¦   ¦   +-- join-room-form.tsx
¦   +-- ui/                    # Shadcn-style primitives (Button, Card, Input, Badge, Spinner)
¦   +-- sign-out-button.tsx
+-- lib/
¦   +-- api.ts                 # Typed API client (fetch wrapper + ApiError)
¦   +-- auth.ts                # Server-side auth helpers (getSession, requireTeacher, requireStudent)
¦   +-- supabase/
¦   ¦   +-- client.ts          # Browser Supabase client
¦   ¦   +-- server.ts          # Server Supabase client (cookies)
¦   +-- use-unauthorized.ts    # 401 handler hook (useUnauthorizedRedirect)
¦   +-- types.ts               # Shared TypeScript interfaces
¦   +-- utils.ts               # cn() className helper
+-- middleware.ts              # Supabase SSR session refresh
+-- vitest.config.ts           # Test config (happy-dom, @ alias)

## Component Tree
app/layout
+-- app/page (landing)
+-- app/login/page
+-- app/register/page
+-- app/teacher/page (server)
¦   +-- CreateRoomForm (client)
+-- app/teacher/rooms/[roomId]/page (server)
¦   +-- TeacherRoomView (client)
¦       +-- SignOutButton
¦       +-- SignOutButton ? useUnauthorizedRedirect
¦       +-- realtime subscription
+-- app/student/page (server)
¦   +-- JoinRoomForm (client)
+-- app/student/room/[roomId]/page (server)
¦   +-- StudentSpeakingSession (client)
¦       +-- AudioRecorder (client)
¦       +-- SignOutButton
¦       +-- realtime subscription
+-- app/student/report/page (server)
¦   +-- StudentReport (server-rendered)
+-- middleware (edge)

## State Management Patterns

### Server Components (Default)
- Data fetching via lib/api.ts + lib/auth.ts helpers
- requireTeacher() / requireStudent() for route protection
- Direct Supabase queries via createClient() (server)

### Client Components (use client)
- Local UI state: useState, useRef
- Realtime: useEffect + Supabase channels
- Forms: controlled inputs + useRouter for navigation
- Auth errors: useUnauthorizedRedirect() hook

### Realtime Pattern
useEffect(() => {
  const supabase = createClient();
  const channel = supabase
    .channel(room-)
    .on(postgres_changes, { event: *, schema: public, table: rooms, filter: id=eq. }, refresh)
    .on(postgres_changes, { event: *, schema: public, table: participants, filter: room_id=eq. }, refresh)
    .subscribe();
  return () => supabase.removeChannel(channel);
}, [roomId]);

## Auth Flow

### Server Components
const { user, session } = await requireTeacher(); // or requireStudent()
const rooms = await api.listRooms(session);

### Client Components
const handleUnauthorized = useUnauthorizedRedirect();
const supabase = createClient();
const { data } = await supabase.auth.signInWithPassword({ email, password });
const res = await fetch(/api/auth/me, { headers: { Authorization: Bearer  } });

### 401 Handling
- useUnauthorizedRedirect() hook in lib/use-unauthorized.ts
- On ApiError.status === 401: supabase.auth.signOut() ? router.replace(/login) ? router.refresh()
- Wired into: room-view.tsx, speaking-session.tsx, join-room-form.tsx, create-room-form.tsx, login/page.tsx

## API Client (lib/api.ts)

class ApiError extends Error { status: number }
async function request(path, session, init?): Promise
const api = {
  me, createRoom, listRooms, getRoom, joinRoom, participants,
  setRoomStatus, startRoom, endRoom, turn, getQuestion,
  submitAnswer, studentReport, classReport
}

- Attaches Authorization: Bearer <token> when session present
- Throws ApiError with status + message from backend detail
- Base URL: NEXT_PUBLIC_API_URL (default http://localhost:8000)

## Testing

### Stack
- Vitest 4 + happy-dom (no jsdom ESM issues on Node 20.17)
- @testing-library/react 16 (React 19 compatible)
- @testing-library/jest-dom + @testing-library/user-event

### Config (vitest.config.ts)
plugins: [react()],
test: {
  environment: happy-dom,
  setupFiles: [./vitest.setup.ts],
  include: [__tests__/**/*.test.{ts,tsx}],
  exclude: [node_modules, .next],
}

### Setup (vitest.setup.ts)
import @testing-library/jest-dom/vitest;
import { cleanup } from @testing-library/react;
import { afterEach, vi } from vitest;
afterEach(() => { cleanup(); vi.restoreAllMocks(); vi.unstubAllGlobals(); vi.unstubAllEnvs(); });

### Mock Patterns
const mocks = vi.hoisted(() => ({ api: { joinRoom: vi.fn() } }));
vi.mock(@/lib/api, () => ({ api: mocks.api }));
vi.mock(next/navigation, () => ({ useRouter: () => mockRouter }));

### Test Files (38 tests)
- __tests__/lib/api.test.ts — API client behavior
- __tests__/components/audio-recorder.test.tsx — MediaRecorder mocking
- __tests__/components/join-room-form.test.tsx — Form submission + 401 redirect
- __tests__/components/create-room-form.test.tsx — Form submission + 401 redirect
- __tests__/components/room-view.test.tsx — Realtime, 401 redirect, no polling
- __tests__/app/login.test.tsx — Login flow + 401 sign-out

### Run Commands
npm test           # vitest run
npm run lint       # eslint
npx tsc --noEmit   # typecheck (via next build internally)

## Key Conventions

1. Server components by default — only add use client when needed (hooks, event handlers, realtime)
2. Typed API errors — ApiError with status + message
3. 401 = sign out + redirect — never silently swallow
4. Realtime over polling — no setInterval
5. Test mocks with vi.hoisted — avoids hoisting issues
6. Server components for data fetching — client only for interactivity
