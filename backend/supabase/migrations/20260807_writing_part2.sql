-- Writing Task 2 Practice
-- Migration: 20260807_writing_part2.sql
-- Adds part support to the writing tables and extends the type constraint
-- to allow Task 2 essay question types.

-- 1. Add `part` column to writing_questions (1 = Task 1, 2 = Task 2)
ALTER TABLE writing_questions ADD COLUMN IF NOT EXISTS part INT NOT NULL DEFAULT 1 CHECK (part IN (1, 2));

-- 2. Add `part` column to writing_submissions
ALTER TABLE writing_submissions ADD COLUMN IF NOT EXISTS part INT NOT NULL DEFAULT 1 CHECK (part IN (1, 2));

-- 3. Extend the type CHECK constraint to allow Task 2 essay types
ALTER TABLE writing_questions DROP CONSTRAINT IF EXISTS writing_questions_type_check;
ALTER TABLE writing_questions ADD CONSTRAINT writing_questions_type_check CHECK (
    type IN ('line','bar','pie','table','map','process','multi',
             'opinion','discussion','advantages','problem_solution',
             'positive_negative','double_question')
);

-- 4. Indexes for part filtering
CREATE INDEX IF NOT EXISTS idx_writing_questions_part ON writing_questions(part);
CREATE INDEX IF NOT EXISTS idx_writing_submissions_part ON writing_submissions(part);
