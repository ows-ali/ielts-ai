-- 002_rooms_participants.sql

create table if not exists public.rooms (
    id uuid primary key default gen_random_uuid(),
    room_code text not null unique,
    title text not null,
    part int not null default 1 check (part in (1, 2, 3)),
    teacher_id uuid not null references public.users (id) on delete cascade,
    status text not null default 'waiting' check (status in ('waiting', 'live', 'ended')),
    current_student_id uuid references public.users (id) on delete set null,
    created_at timestamptz not null default now()
);

create index if not exists idx_rooms_teacher on public.rooms (teacher_id);
create index if not exists idx_rooms_code on public.rooms (room_code);

create table if not exists public.participants (
    id uuid primary key default gen_random_uuid(),
    room_id uuid not null references public.rooms (id) on delete cascade,
    student_id uuid not null references public.users (id) on delete cascade,
    status text not null default 'waiting' check (status in ('waiting', 'speaking', 'completed')),
    joined_at timestamptz not null default now(),
    unique (room_id, student_id)
);

create index if not exists idx_participants_room on public.participants (room_id);

-- RLS: teachers own their rooms; participants see rooms they joined.
alter table public.rooms enable row level security;
alter table public.participants enable row level security;

drop policy if exists "teachers manage own rooms" on public.rooms;
create policy "teachers manage own rooms" on public.rooms
    for all using (auth.uid() = teacher_id) with check (auth.uid() = teacher_id);

drop policy if exists "students read joined rooms" on public.rooms;
create policy "students read joined rooms" on public.rooms
    for select using (
        exists (
            select 1 from public.participants p
            where p.room_id = public.rooms.id and p.student_id = auth.uid()
        )
    );

drop policy if exists "teachers manage participants" on public.participants;
create policy "teachers manage participants" on public.participants
    for all using (
        exists (select 1 from public.rooms r where r.id = public.participants.room_id and r.teacher_id = auth.uid())
    );

drop policy if exists "students read own participants rows" on public.participants;
create policy "students read own participants rows" on public.participants
    for select using (student_id = auth.uid());
