-- 003_questions.sql
-- IELTS question bank (seeded). Add more via the admin or INSERT statements.

create table if not exists public.questions (
    id uuid primary key default gen_random_uuid(),
    part int not null check (part in (1, 2, 3)),
    topic text,
    question text not null,
    difficulty text not null default 'medium' check (difficulty in ('easy', 'medium', 'hard')),
    created_at timestamptz not null default now()
);

alter table public.questions enable row level security;

drop policy if exists "anyone can read questions" on public.questions;
create policy "anyone can read questions" on public.questions
    for select using (true);

insert into public.questions (part, topic, question, difficulty) values
    (1, 'Work', 'What do you do for a living?', 'easy'),
    (1, 'Home', 'Can you describe the place where you live?', 'easy'),
    (1, 'Hobbies', 'What do you like to do in your free time?', 'easy'),
    (1, 'Food', 'What kind of food do you enjoy eating?', 'easy'),
    (1, 'Travel', 'Do you like travelling? Why or why not?', 'easy'),
    (1, 'Technology', 'How often do you use your mobile phone?', 'easy'),
    (1, 'Education', 'What subject did you enjoy most at school?', 'medium'),
    (1, 'Friends', 'How important are friends to you?', 'medium'),
    (1, 'Weather', 'What is the weather like in your country?', 'medium'),
    (1, 'Reading', 'Do you prefer reading books or watching films?', 'medium'),
    (1, 'Music', 'What kind of music do you listen to?', 'medium'),
    (1, 'Sport', 'Do you play any sports?', 'easy'),
    (1, 'Family', 'How much time do you spend with your family?', 'medium'),
    (1, 'Shopping', 'Do you enjoy going shopping?', 'easy'),
    (1, 'Daily Routine', 'What does a typical day look like for you?', 'medium'),
    (2, 'Travel', 'Describe a memorable journey you have made.', 'medium'),
    (2, 'People', 'Describe a person who has influenced you.', 'medium'),
    (2, 'Places', 'Describe a place you would like to visit.', 'medium'),
    (2, 'Objects', 'Describe an object that is important to you.', 'medium'),
    (2, 'Events', 'Describe a celebration or festival you enjoyed.', 'medium'),
    (2, 'Skills', 'Describe a skill you would like to learn.', 'medium'),
    (2, 'Books', 'Describe a book you have recently read.', 'medium'),
    (2, 'Food', 'Describe a traditional meal from your country.', 'hard'),
    (2, 'Activities', 'Describe an activity you do to relax.', 'medium'),
    (2, 'Homes', 'Describe a house or apartment you remember well.', 'medium'),
    (2, 'Jobs', 'Describe a job you would like to do in the future.', 'medium'),
    (2, 'Animals', 'Describe an animal you are fond of.', 'medium'),
    (2, 'Films', 'Describe a film you enjoyed watching.', 'medium'),
    (2, 'Gifts', 'Describe a gift you have received.', 'medium'),
    (2, 'Achievements', 'Describe an achievement you are proud of.', 'hard'),
    (3, 'Education', 'Why do you think education is important for society?', 'hard'),
    (3, 'Technology', 'Has technology improved the quality of life?', 'hard'),
    (3, 'Environment', 'What should governments do to protect the environment?', 'hard'),
    (3, 'Work', 'Do you think the concept of retirement will change in the future?', 'hard'),
    (3, 'Health', 'Why are many people suffering from lifestyle diseases today?', 'hard'),
    (3, 'Cities', 'What are the advantages of living in large cities?', 'hard'),
    (3, 'Globalization', 'Does globalization harm local cultures?', 'hard'),
    (3, 'Media', 'How has social media changed the way we communicate?', 'hard'),
    (3, 'Family', 'Has the role of the family changed in modern society?', 'hard'),
    (3, 'Travel', 'Is tourism beneficial or harmful to local communities?', 'hard'),
    (3, 'Money', 'Is money the most important measure of success?', 'hard'),
    (3, 'Youth', 'What challenges do young people face today?', 'medium'),
    (3, 'Learning', 'How can people learn a foreign language effectively?', 'medium'),
    (3, 'Food', 'Should governments tax unhealthy food?', 'hard'),
    (3, 'Privacy', 'Is privacy still possible in the digital age?', 'hard');
