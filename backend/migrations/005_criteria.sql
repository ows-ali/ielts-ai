-- 005_criteria.sql
-- RAG knowledge base: IELTS Band Descriptors (speaking) stored with embeddings.

create extension if not exists vector;

create table if not exists public.ielts_criteria (
    id bigint generated always as identity primary key,
    part int not null check (part in (1, 2, 3)),
    criterion text not null check (criterion in ('fluency', 'grammar', 'vocabulary', 'pronunciation')),
    band text not null,
    content text not null,
    embedding vector(768)
);

alter table public.ielts_criteria enable row level security;

drop policy if exists "criteria readable by authenticated" on public.ielts_criteria;
create policy "criteria readable by authenticated" on public.ielts_criteria
    for select using (auth.role() = 'authenticated');

-- Vector search function (used by the FastAPI RAG service).
create or replace function public.match_criteria(
    query_embedding vector(768),
    match_count int default 4
)
returns table (
    id bigint,
    part int,
    criterion text,
    band text,
    content text,
    similarity float
)
language plpgsql
as $$
begin
    return query
    select c.id, c.part, c.criterion, c.band, c.content,
           1 - (c.embedding <=> query_embedding) as similarity
    from public.ielts_criteria c
    order by c.embedding <=> query_embedding
    limit match_count;
end;
$$;

grant execute on function public.match_criteria(vector, int) to authenticated, service_role;
