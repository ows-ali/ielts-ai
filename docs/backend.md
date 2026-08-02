# Backend Architecture

## Tech Stack
- **Framework**: FastAPI (Python 3.12)
- **Database/ORM**: Supabase (PostgreSQL) via async client
- **Auth**: Supabase GoTrue (JWT verification via /auth/v1/user)
- **AI**: Google Gemini (gemini-3.5-flash for eval + STT)
- **Server**: uvicorn
- **Language**: Python 3.12

## Project Structure
backend/
+-- app/
¦   +-- main.py                 # FastAPI app + CORS
¦   +-- core/
¦   ¦   +-- config.py           # Pydantic Settings (env vars)
¦   ¦   +-- security.py         # Auth: get_current_user, require_teacher
¦   +-- services/
¦   ¦   +-- supabase_client.py  # Async Supabase client (service role)
¦   ¦   +-- db.py               # All DB queries (rooms, participants, evals)
¦   ¦   +-- gemini.py           # Gemini evaluation + STT
¦   ¦   +-- rag.py              # RAG (not used in MVP)
¦   ¦   +-- check.py            # Health/readiness checks
¦   +-- api/
¦   ¦   +-- routes/
¦   ¦   ¦   +-- auth.py         # GET /api/auth/me
¦   ¦   ¦   +-- rooms.py        # Room CRUD + status + turn
¦   ¦   ¦   +-- speaking.py     # POST /answers (Gemini eval)
¦   ¦   ¦   +-- reports.py      # GET /students/me/report, GET /rooms/{id}/report
¦   ¦   +-- __init__.py
¦   +-- schemas/
¦   ¦   +-- auth.py             # UserOut
¦   ¦   +-- rooms.py            # RoomOut, ParticipantOut, TurnState
¦   ¦   +-- speaking.py         # AnswerSubmit, EvaluationOut
¦   ¦   +-- reports.py          # StudentAttempt, StudentReportOut, ClassReportOut
¦   +-- __init__.py
+-- scripts/
¦   +-- test_flow.py            # Full authorized e2e (12 steps, self-cleaning)
¦   +-- create_dummy_users.py   # Creates 4 verified users
¦   +-- seed_criteria.py        # (unused)
+-- requirements.txt
+-- .env                        # Local env vars
+-- .env.example                # Template

## Auth Verification

### Token Validation (app/core/security.py)
async function _verify_token_with_auth_server(token):
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(
            f"{settings.supabase_url}/auth/v1/user",
            headers={"apikey": settings.supabase_anon_key, "Authorization": "Bearer ${token}"}
        )
    if resp.status_code == 200:
        return resp.json()
    raise HTTPException(401, "Invalid token")

- Calls Supabase /auth/v1/user with apikey (anon) + Authorization: Bearer <token>
- Supabase validates ES256 JWT, returns user object or 401
- Backend extracts role from user_metadata or app_metadata (default: student)

### Dependencies
async function get_current_user(request) -> CurrentUser
function require_teacher(user: CurrentUser = Depends(get_current_user)) -> CurrentUser
- get_current_user: extracts Bearer token, validates, returns CurrentUser
- require_teacher: 403 if role != teacher

## Database Queries (app/services/db.py)

All queries use async Supabase client with service role key.

### Key Functions
| Function | Purpose |
|----------|---------|
| upsert_user(user) | Create/update user profile in public.users |
| get_user(user_id) | Fetch user by ID |
| create_room(room) | Insert room |
| get_room(room_id) | Fetch room by ID |
| get_room_by_code(code) | Lookup room by code |
| list_rooms_for_teacher(teacher_id) | Teacher has rooms (dashboard) |
| add_participant(payload) | Student joins room |
| get_participant(room_id, student_id) | Check if already joined |
| list_participants(room_id) | All participants with user names |
| update_participant_status(room_id, student_id, status) | waiting/speaking/completed |
| get_question(id) / get_next_question(part, exclude_ids) | Question retrieval |
| insert_answer(payload) | Store student audio_url + transcript |
| insert_evaluation(payload) | Store Gemini scores + feedback |
| list_evaluations_for_student(student_id) | Student report (with answers + rooms) |
| list_evaluations_for_room(room_id) | Teacher class report (all evaluations in room) |

### Query Patterns
- All inserts/upserts use .execute() (no .select().single() chaining — postgrest-py 2.11 limitation)
- .maybe_single().execute() returns None on zero rows (not APIResponse)
- RLS handled by Supabase; service role bypasses RLS for admin operations

## Gemini Integration (app/services/gemini.py)

### Models
- **Evaluation + STT**: gemini-3.5-flash (free tier: 60 RPM, 1M tokens/day)
- **Embeddings**: gemini-embedding-2 (768-dim, not used in MVP)

### Functions
async function evaluate_speaking(question, transcript, audio_url) -> dict:
    # Returns: fluency, grammar, vocabulary, pronunciation, overall_band, feedback[]

async function transcribe_audio(audio_bytes, mime_type) -> str:
    # Returns transcript text

### Error Handling
- 429 (quota) ? retry with backoff or fallback
- 404 (model not found) ? fallback to working model
- Network timeout ? 10s default

## API Routes

### Auth (/api/auth)
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | /api/auth/me | Bearer | Current user profile (upserts to users table) |

### Rooms (/api/rooms)
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | /api/rooms | Bearer (teacher) | Create room |
| GET | /api/rooms | Bearer | List teacher has rooms |
| GET | /api/rooms/{id} | Bearer | Get room |
| POST | /api/rooms/join | Bearer (student) | Join by code |
| GET | /api/rooms/{id}/participants | Bearer | List participants |
| POST | /api/rooms/{id}/status | Bearer (teacher) | Update status |
| POST | /api/rooms/{id}/start | Bearer (teacher) | Start session (assign turn) |
| POST | /api/rooms/{id}/end | Bearer (teacher) | End session |
| GET | /api/rooms/{id}/turn | Bearer | Current turn state |
| GET | /api/rooms/{id}/report | Bearer (teacher) | Class report |

### Speaking (/api/rooms/{room_id}/answers)
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | /api/rooms/{room_id}/answers | Bearer (student) | Submit answer + get Gemini eval |

### Reports
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | /api/students/me/report | Bearer (student) | Student has attempts |
| GET | /api/rooms/{room_id}/report | Bearer (teacher) | Class report |

## Storage (Audio)

### Bucket: audio
- **Upload**: Student records ? blob ? supabase.storage.from(audio).upload(path, blob) ? getPublicUrl(path) ? audio_url in answers table
- **RLS Policies**:
  - authenticated can upload audio: INSERT on storage.objects where bucket_id = audio
  - authenticated can read audio: SELECT on storage.objects where bucket_id = audio

## Realtime

### Tables Published
alter publication supabase_realtime add table public.rooms, public.participants;

### Frontend Subscriptions
- Teacher: room-{id} ? rooms + participants changes ? refresh()
- Student: student-room-{id} ? rooms + participants changes ? refresh()

## Key Files

| Area | File |
|------|------|
| App entry | app/main.py |
| Config | app/core/config.py |
| Auth | app/core/security.py |
| Supabase client | app/services/supabase_client.py |
| DB queries | app/services/db.py |
| Gemini | app/services/gemini.py |
| Auth routes | app/api/routes/auth.py |
| Room routes | app/api/routes/rooms.py |
| Speaking routes | app/api/routes/speaking.py |
| Report routes | app/api/routes/reports.py |
| E2E test | scripts/test_flow.py |
| Dummy users | scripts/create_dummy_users.py |
