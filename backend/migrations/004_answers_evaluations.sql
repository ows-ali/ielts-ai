-- 004_answers_evaluations.sql

create table if not exists public.answers (
    id uuid primary key default gen_random_uuid(),
    room_id uuid not null references public.rooms (id) on delete cascade,
    student_id uuid not null references public.users (id) on delete cascade,
    question_id uuid not null references public.questions (id) on delete cascade,
    audio_url text,
    transcript text,
    created_at timestamptz not null default now()
);

create index if not exists idx_answers_room on public.answers (room_id);
create index if not exists idx_answers_student on public.answers (student_id);

create table if not exists public.evaluations (
    id uuid primary key default gen_random_uuid(),
    answer_id uuid not null references public.answers (id) on delete cascade,
    student_id uuid not null references public.users (id) on delete cascade,
    fluency numeric(3,1) not null,
    grammar numeric(3,1) not null,
    vocabulary numeric(3,1) not null,
    pronunciation numeric(3,1) not null,
    overall_band numeric(3,1) not null,
    feedback jsonb not null default '[]',
    created_at timestamptz not null default now()
);

create index if not exists idx_evals_student on public.evaluations (student_id);
create index if not exists idx_evals_answer on public.evaluations (answer_id);

-- RLS: the service role handles all writes. Users may read their own data.
alter table public.answers enable row level security;
alter table public.evaluations enable row level security;

drop policy if exists "answers read own" on public.answers;
create policy "answers read own" on public.answers
    for select using (
        student_id = auth.uid()
        or exists (select 1 from public.rooms r where r.id = public.answers.room_id and r.teacher_id = auth.uid())
    );

drop policy if exists "evaluations read own" on public.evaluations;
create policy "evaluations read own" on public.evaluations
    for select using (
        student_id = auth.uid()
        or exists (
            select 1
            from public.answers a
            join public.rooms r on r.id = a.room_id
            where a.id = public.evaluations.answer_id and r.teacher_id = auth.uid()
        )
    );

-- Added here (after questions table exists) so the FK resolves.
alter table public.rooms
    add column if not exists current_question_id uuid
    references public.questions (id) on delete set null;
