# API Specification & Contracts

## Overview
The IELTS AI Speaking Classroom backend is a RESTful FastAPI service communicating with Supabase PostgreSQL and Google Gemini AI. All authenticated routes expect a Supabase JWT in the `Authorization` header.

```http
Authorization: Bearer <SUPABASE_ACCESS_TOKEN>
```

---

## REST Endpoints Summary

### Authentication

#### `GET /api/auth/me`
- **Description**: Verifies the Bearer token and returns the current user profile.
- **Header**: `Authorization: Bearer <token>`
- **Response `200 OK`**:
  ```json
  {
    "id": "uuid-string",
    "email": "teacher1@example.com",
    "name": "Teacher One",
    "role": "teacher"
  }
  ```
- **Error `401 Unauthorized`**: Returned when the token is missing, expired, or invalid.

---

### Rooms & Management

#### `POST /api/rooms`
- **Description**: Creates a new practice room (Teacher only).
- **Request Body**:
  ```json
  {
    "title": "Evening Part 1 Speaking",
    "part": 1
  }
  ```
- **Response `200 OK`**:
  ```json
  {
    "id": "room-uuid",
    "room_code": "AB12CD",
    "title": "Evening Part 1 Speaking",
    "part": 1,
    "teacher_id": "teacher-uuid",
    "status": "waiting",
    "created_at": "2026-08-02T20:00:00Z"
  }
  ```

#### `GET /api/rooms`
- **Description**: Lists all rooms created by the current authenticated teacher.
- **Response `200 OK`**: Array of `Room` objects.

#### `GET /api/rooms/{id}`
- **Description**: Gets details of a specific room.
- **Response `200 OK`**: `Room` object.

#### `POST /api/rooms/join`
- **Description**: Student joins a room using a room code.
- **Request Body**:
  ```json
  {
    "room_code": "AB12CD"
  }
  ```
- **Response `200 OK`**: `Room` object.

#### `GET /api/rooms/{id}/participants`
- **Description**: Fetches all students currently registered in a room.
- **Response `200 OK`**:
  ```json
  [
    {
      "id": "participant-uuid",
      "room_id": "room-uuid",
      "student_id": "student-uuid",
      "student_name": "Student One",
      "status": "waiting",
      "joined_at": "2026-08-02T20:05:00Z"
    }
  ]
  ```

#### `POST /api/rooms/{id}/status`
- **Description**: Updates the room status (`waiting` | `live` | `ended`).
- **Request Body**:
  ```json
  {
    "status": "live"
  }
  ```

#### `POST /api/rooms/{id}/start`
- **Description**: Starts the room practice session and selects the first student turn.
- **Response `200 OK`**: `TurnState` object.

#### `POST /api/rooms/{id}/end`
- **Description**: Ends the room session and updates status to `ended`.
- **Response `200 OK`**: `Room` object.

#### `GET /api/rooms/{id}/turn`
- **Description**: Fetches current turn state, current speaking student, and question prompt.
- **Response `200 OK`**:
  ```json
  {
    "room_id": "room-uuid",
    "current_student_id": "student-uuid",
    "current_student_name": "Student One",
    "question_id": "question-uuid",
    "question": {
      "id": "question-uuid",
      "part": 1,
      "topic": "Hobbies",
      "question": "What do you like to do in your spare time?",
      "difficulty": "medium"
    },
    "status": "live"
  }
  ```

---

### Student Answers & Evaluations

#### `POST /api/rooms/{id}/answers`
- **Description**: Submits audio URL for the current turn, triggers Gemini evaluation and transcript generation.
- **Request Body**:
  ```json
  {
    "room_id": "room-uuid",
    "question_id": "question-uuid",
    "audio_url": "https://<supabase-url>/storage/v1/object/public/audio/room-uuid/student-uuid.webm",
    "transcript": "In my spare time I enjoy reading books and playing tennis."
  }
  ```
- **Response `200 OK`**:
  ```json
  {
    "id": "evaluation-uuid",
    "answer_id": "answer-uuid",
    "fluency": 7.5,
    "grammar": 7.0,
    "vocabulary": 8.0,
    "pronunciation": 7.5,
    "overall_band": 7.5,
    "feedback": [
      "Use more complex conjunctions when expanding on hobbies.",
      "Good lexical range regarding sports terminology."
    ]
  }
  ```

---

### Reports

#### `GET /api/students/me/report`
- **Description**: Retrieves performance history and past attempt scores for the logged-in student.
- **Response `200 OK`**:
  ```json
  {
    "student_id": "student-uuid",
    "attempts": [
      {
        "id": "eval-uuid",
        "room_code": "AB12CD",
        "title": "Evening Part 1 Speaking",
        "question": "What do you like to do in your spare time?",
        "audio_url": "https://<supabase-url>/storage/v1/object/public/audio/room-uuid/student-uuid.webm",
        "transcript": "In my spare time I enjoy reading books...",
        "fluency": 7.5,
        "grammar": 7.0,
        "vocabulary": 8.0,
        "pronunciation": 7.5,
        "overall_band": 7.5,
        "feedback": ["Use more complex conjunctions..."],
        "created_at": "2026-08-02T20:10:00Z"
      }
    ]
  }
  ```

#### `GET /api/rooms/{id}/report`
- **Description**: Room-wide summary report accessible by teachers and room participants.
- **Privacy Rules**:
  - **Teachers**: Receive full participant score objects containing overall band, criterion sub-scores (fluency, grammar, vocabulary, pronunciation), question prompt, transcript, feedback tips, and `audio_url`.
  - **Students**: Receive overall `band` scores for all classmates (class leaderboard), but `audio_url`, `transcript`, and `feedback` are strictly `null` for other students (populated ONLY for the student's own entry).
- **Response `200 OK` (Teacher View Example)**:
  ```json
  {
    "room_id": "room-uuid",
    "room_code": "AB12CD",
    "participants": [
      {
        "student_id": "student-uuid",
        "student_name": "Student One",
        "status": "completed",
        "band": 7.5,
        "audio_url": "https://<supabase-url>/storage/v1/object/public/audio/room-uuid/student-uuid.webm",
        "transcript": "In my spare time I enjoy reading books...",
        "question": "What do you like to do in your spare time?",
        "fluency": 7.5,
        "grammar": 7.0,
        "vocabulary": 8.0,
        "pronunciation": 7.5,
        "feedback": ["Use more complex conjunctions..."]
      }
    ],
    "average_band": 7.5,
    "common_problems": [
      "Frequent hesitations when forming conditional sentences.",
      "Inconsistent word stress on multi-syllable vocabulary."
    ]
  }
  ```

---

## Supabase Realtime Channels

| Channel Pattern | Table Subscribed | Target Audience | Triggered Events |
|-----------------|------------------|-----------------|------------------|
| `room-{room_id}` | `rooms`, `participants` | Teacher Component | Status updates, student join/leave/completion |
| `student-room-{room_id}` | `rooms`, `participants` | Student Component | Turn transition, room completion |
