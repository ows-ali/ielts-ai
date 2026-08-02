Project: IELTS AI Speaking Classroom
Product Vision

A collaborative AI-powered IELTS speaking practice platform where teachers can run live speaking sessions with students.

Students join an AI room using a code, practice speaking turn-by-turn, receive AI feedback, and teachers get a complete class performance report.

The platform supports:

Teacher-led classroom sessions
Student self-practice
AI evaluation and feedback
MVP Goal

Build a working product where:

Teacher creates an IELTS practice room.
Students join using a room code.
AI manages speaking turns.
Students answer IELTS questions using their microphone.
AI evaluates answers.
Each student receives individual feedback.
Teacher receives class analytics.
User Roles
1. Teacher

Capabilities:

Register/login
Create practice rooms
Select IELTS section:
Speaking Part 1
Speaking Part 2
Speaking Part 3
View joined students
Start/stop session
Monitor student progress
View class report
2. Student

Capabilities:

Register/login
Join room using code
See current question
Record voice answer
Receive feedback
View personal progress history
Main User Flow
Teacher Flow
Login

↓

Create Room

↓

Select:
IELTS Speaking Part

↓

Generate Room Code

↓

Share code with students

↓

Students join

↓

Start session

↓

AI manages turns

↓

View results

↓

Download report
Student Flow
Login

↓

Enter room code

↓

Join session

↓

Wait for turn

↓

AI asks question

↓

Record answer

↓

Submit

↓

AI evaluates

↓

Receive feedback

Technical Architecture
                 Frontend
              Next.js + React

                    |
                    |

             Backend API

              FastAPI

                    |
        -------------------------

        |                       |

   PostgreSQL              AI Services

   Supabase                 Gemini/GPT

        |                       |

        |                  RAG System

        |                       |

        |             IELTS Knowledge Base

        |

   Analytics + Reports

Tech Stack
Frontend

Use:

Next.js 15
TypeScript
Tailwind CSS
Shadcn UI

Purpose:

Modern UI
Fast development
Easy deployment
Backend

Use:

Python FastAPI

Responsibilities:

Authentication
Room management
AI orchestration
Score generation
Database communication
Database

Use:

Supabase PostgreSQL

Tables:

users
rooms
participants
questions
answers
evaluations
progress
Database Design
Users
id

name

email

role
(teacher/student)

created_at
Rooms
id

room_code

teacher_id

status

created_at

Example:

IELTS8291
Room Participants
id

room_id

student_id

joined_at

status
IELTS Questions
id

part

topic

question

difficulty

Example:

Part 2

Topic:
Travel

Question:
Describe a memorable journey.
Speaking Answers
id

room_id

student_id

question_id

audio_url

transcript

created_at
Evaluations
id

answer_id

fluency_score

grammar_score

vocabulary_score

pronunciation_score

overall_band

feedback
AI Architecture
Components
1. Question Generator

NOT RAG.

Questions come from database.

Example:

get_question()
2. Speech Recognition

Input:

Student voice

Output:

Transcript

Options:

Whisper
Gemini speech API
3. IELTS Evaluation Agent

Input:

Transcript
IELTS criteria

Output:

{
fluency:7,
grammar:6.5,
vocabulary:7,
pronunciation:7,
overall:7,

feedback:
[
"Use more complex sentences",
"Reduce repetition"
]
}
RAG System

Purpose:

Provide IELTS scoring criteria.

NOT questions.

Knowledge base contains:

IELTS Band Descriptors

Speaking criteria

Fluency guidelines

Grammar guidelines

Vocabulary guidelines

Pronunciation guidelines

Flow:

Student Answer

↓

Retrieve relevant IELTS criteria

↓

LLM evaluates

↓

Generate score
Agent Tools

The AI agent has these tools:

Tool 1
get_next_question()

Gets IELTS question.

Tool 2
get_student_history()

Checks previous weaknesses.

Tool 3
retrieve_ielts_criteria()

RAG search.

Tool 4
save_evaluation()

Stores results.

Real-Time Room Logic

Use:

Supabase Realtime / WebSockets

Room state:

{
room_id:"IELTS123",

current_student:"Ali",

status:"waiting"
}

Flow:

Teacher starts session

↓

AI selects student

↓

Student answers

↓

Save result

↓

Next student

Teacher Dashboard

Display:

Live Session

Students:

Ali
Completed
Band 6.5


Sara
Completed
Band 7


Ahmed
Waiting

Class report:

Average Band:

6.7


Common Problems:

Grammar:
Past tense mistakes

Vocabulary:
Repeated adjectives

Fluency:
Long pauses
Student Dashboard

Show:

Latest Attempt

Overall:
6.5


Fluency:
7

Grammar:
6

Vocabulary:
7

Pronunciation:
7


Improve:

- Use linking words
- Give longer examples
- Avoid repetition
MVP Features (Build First)
Phase 1

Authentication

✓ Teacher login

✓ Student login

Phase 2

Rooms

✓ Create room

✓ Join room

✓ Participant list

Phase 3

Speaking

✓ Display question

✓ Record audio

✓ Upload audio

Phase 4

AI

✓ Speech-to-text

✓ IELTS evaluation

✓ Feedback generation

Phase 5

Reports

✓ Student report

✓ Teacher dashboard