-- 001_users.sql
-- users table synced from auth.users via trigger.

create table if not exists public.users (
    id uuid primary key references auth.users (id) on delete cascade,
    name text,
    email text,
    role text not null default 'student' check (role in ('teacher', 'student')),
    created_at timestamptz not null default now()
);

-- Keep users synced when a new auth user is created.
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
    insert into public.users (id, email, name, role)
    values (
        new.id,
        new.email,
        coalesce(new.raw_user_meta_data ->> 'name', new.email),
        coalesce(new.raw_user_meta_data ->> 'role', 'student')
    )
    on conflict (id) do update set
        email = excluded.email,
        name = excluded.name,
        role = excluded.role;
    return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
    after insert on auth.users
    for each row execute procedure public.handle_new_user();

-- RLS: users can read/update their own row; anon/authenticated minimal.
alter table public.users enable row level security;

drop policy if exists "users can read own" on public.users;
create policy "users can read own" on public.users
    for select using (auth.uid() = id);

drop policy if exists "users can update own" on public.users;
create policy "users can update own" on public.users
    for update using (auth.uid() = id) with check (auth.uid() = id);
