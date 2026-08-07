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

### Writing Practice (Task 1 & Task 2)

All writing endpoints require a valid Supabase Bearer token. Students can read
questions/samples and submit answers; teachers additionally list all
submissions and create/delete feedback.

Both task types share the same tables, distinguished by a `part` column
(`1` = Task 1, `2` = Task 2). List endpoints accept an optional `part` query
param (default `1`); pass `part=2` for essays. Task 1 question types are
`line|bar|pie|table|map|process|multi`; Task 2 types are
`opinion|discussion|advantages|problem_solution|positive_negative|double_question`.

#### `GET /api/writing/questions`
- **Description**: Lists writing questions, optionally filtered by `type`,
  `difficulty` (`easy|medium|hard`) and `part` (`1|2`, default `1`) via query
  params. When `part` is omitted/`1` only Task 1 types are returned; `part=2`
  returns only essay types.
- **Response `200 OK`**:
  ```json
  [
    {
      "id": "question-uuid",
      "type": "map",
      "title": "Island Before and After Tourist Development",
      "prompt": "The two maps below show an island...",
      "data_description": { "type": "map", "maps": ["Before", "After"], "before": [], "after": [] },
      "image_url": "writing-images/island-before-after.png",
      "difficulty": "easy",
      "part": 1
    }
  ]
  ```

#### `GET /api/writing/questions/{question_id}`
- **Description**: Gets a question with its three model samples (Band 5/7/9).
- **Response `200 OK`**: `WritingQuestionDetail` = question fields (incl. `part`)
  plus `samples: [WritingSampleOut]` (each with `band`, `answer_text`, the four
  criterion sub-scores, `explanation`, `improvement_tips`).
- **Error `404`**: Question not found.

#### `GET /api/writing/questions/{question_id}/samples`
- **Description**: Lists only the model samples for a question.
- **Response `200 OK`**: Array of `WritingSampleOut`.

#### `POST /api/writing/submissions`
- **Description**: Creates a submission (student). Stores the answer, the
  server-computed `word_count`, and the `part` (from the request body or the
  question, defaulting to `1`).
- **Request Body**:
  ```json
  {
    "question_id": "question-uuid",
    "answer_text": "The maps illustrate the transformation of the island... (at least 20 chars)",
    "part": 1
  }
  ```
- **Response `201 Created`**: `WritingSubmissionOut` with empty `feedback`.
- **Error `422`**: Answer shorter than 20 characters. **Error `404`**:
  Question not found.

#### `GET /api/writing/submissions/me`
- **Description**: Lists the current student's submissions, each with its
  feedback list and the average `overall_band` across feedback. Accepts an
  optional `part` query param to filter to one task.
- **Response `200 OK`**: Array of `WritingSubmissionOut` (each includes `part`).

#### `GET /api/writing/submissions`
- **Description**: Lists all submissions (teacher only). Students' answers are
  visible to every teacher; feedback is nested per submission. Accepts an
  optional `part` query param to filter to one task.
- **Response `200 OK`**: Array of `WritingSubmissionOut` (each includes `part`).

#### `GET /api/writing/submissions/{submission_id}`
- **Description**: Gets one submission including the full question prompt/data
  and all feedback. Allowed for the owning student or any teacher.
- **Response `200 OK`**: `WritingSubmissionDetailOut`.
- **Error `403`**: Not the owner and not a teacher. **Error `404`**: Not found.

#### `POST /api/writing/feedback`
- **Description**: Creates teacher feedback on a submission (teacher only).
  The server computes `overall_band` as the average of the four criteria.
- **Request Body**:
  ```json
  {
    "submission_id": "submission-uuid",
    "task_achievement": 6,
    "coherence_cohesion": 5,
    "lexical_resource": 6,
    "grammatical_range": 5,
    "overall_comment": "Good structure but needs more linking words."
  }
  ```
- **Response `200 OK`**: `WritingFeedbackOut` including `overall_band` and
  `teacher_name`.
- **Error `422`**: A criterion score is outside the 4–9 range. **Error `404`**:
  Submission not found.

#### `DELETE /api/writing/feedback/{feedback_id}`
- **Description**: Deletes a feedback entry (teacher only).
- **Response `204 No Content`**.

---

## Supabase Realtime Channels

| Channel Pattern | Table Subscribed | Target Audience | Triggered Events |
|-----------------|------------------|-----------------|------------------|
| `room-{room_id}` | `rooms`, `participants` | Teacher Component | Status updates, student join/leave/completion |
| `student-room-{room_id}` | `rooms`, `participants` | Student Component | Turn transition, room completion |
