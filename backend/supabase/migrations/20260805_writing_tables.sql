-- Writing Task 1 Practice Tables
-- Migration: 20260805_writing_tables.sql

-- 1. Writing Questions Table
CREATE TABLE IF NOT EXISTS writing_questions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    type TEXT NOT NULL CHECK (type IN ('line','bar','pie','table','map','process','multi')),
    title TEXT NOT NULL,
    prompt TEXT NOT NULL,
    data_description JSONB,
    image_url TEXT,
    difficulty TEXT CHECK (difficulty IN ('easy','medium','hard')),
    created_at TIMESTAMPTZ DEFAULT now()
);

-- 2. Writing Samples (Model Answers with Band Analysis)
CREATE TABLE IF NOT EXISTS writing_samples (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    question_id UUID REFERENCES writing_questions(id) ON DELETE CASCADE,
    band INT NOT NULL CHECK (band BETWEEN 5 AND 9),
    answer_text TEXT NOT NULL,
    task_achievement INT CHECK (task_achievement BETWEEN 4 AND 9),
    coherence_cohesion INT CHECK (coherence_cohesion BETWEEN 4 AND 9),
    lexical_resource INT CHECK (lexical_resource BETWEEN 4 AND 9),
    grammatical_range INT CHECK (grammatical_range BETWEEN 4 AND 9),
    explanation TEXT NOT NULL,
    improvement_tips JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- 3. Writing Submissions (Student Practice Attempts)
CREATE TABLE IF NOT EXISTS writing_submissions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID REFERENCES users(id) ON DELETE CASCADE,
    question_id UUID REFERENCES writing_questions(id) ON DELETE CASCADE,
    answer_text TEXT NOT NULL,
    word_count INT GENERATED ALWAYS AS (LENGTH(answer_text) - LENGTH(REPLACE(answer_text, ' ', '')) + 1) STORED,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- 4. Writing Feedback (Teacher Feedback - Multiple per Submission)
CREATE TABLE IF NOT EXISTS writing_feedback (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    submission_id UUID REFERENCES writing_submissions(id) ON DELETE CASCADE,
    teacher_id UUID REFERENCES users(id) ON DELETE CASCADE,
    task_achievement INT CHECK (task_achievement BETWEEN 4 AND 9),
    coherence_cohesion INT CHECK (coherence_cohesion BETWEEN 4 AND 9),
    lexical_resource INT CHECK (lexical_resource BETWEEN 4 AND 9),
    grammatical_range INT CHECK (grammatical_range BETWEEN 4 AND 9),
    overall_band NUMERIC(2,1) GENERATED ALWAYS AS (
        (task_achievement + coherence_cohesion + lexical_resource + grammatical_range) / 4.0
    ) STORED,
    overall_comment TEXT,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- Indexes for Performance
CREATE INDEX IF NOT EXISTS idx_writing_questions_type ON writing_questions(type);
CREATE INDEX IF NOT EXISTS idx_writing_questions_difficulty ON writing_questions(difficulty);
CREATE INDEX IF NOT EXISTS idx_writing_samples_question_id ON writing_samples(question_id);
CREATE INDEX IF NOT EXISTS idx_writing_samples_band ON writing_samples(band);
CREATE INDEX IF NOT EXISTS idx_writing_submissions_student_id ON writing_submissions(student_id);
CREATE INDEX IF NOT EXISTS idx_writing_submissions_question_id ON writing_submissions(question_id);
CREATE INDEX IF NOT EXISTS idx_writing_feedback_submission_id ON writing_feedback(submission_id);
CREATE INDEX IF NOT EXISTS idx_writing_feedback_teacher_id ON writing_feedback(teacher_id);

-- Row Level Security
ALTER TABLE writing_questions ENABLE ROW LEVEL SECURITY;
ALTER TABLE writing_samples ENABLE ROW LEVEL SECURITY;
ALTER TABLE writing_submissions ENABLE ROW LEVEL SECURITY;
ALTER TABLE writing_feedback ENABLE ROW LEVEL SECURITY;

-- Policies for writing_questions (readable by all authenticated users)
CREATE POLICY "Questions readable by authenticated users" ON writing_questions
    FOR SELECT TO authenticated USING (true);

-- Policies for writing_samples (readable by all authenticated users)
CREATE POLICY "Samples readable by authenticated users" ON writing_samples
    FOR SELECT TO authenticated USING (true);

-- Policies for writing_submissions
-- Students can read their own submissions
CREATE POLICY "Students can read own submissions" ON writing_submissions
    FOR SELECT TO authenticated USING (student_id = auth.uid());

-- Students can insert their own submissions
CREATE POLICY "Students can insert own submissions" ON writing_submissions
    FOR INSERT TO authenticated WITH CHECK (student_id = auth.uid());

-- Students can update their own submissions (for drafts)
CREATE POLICY "Students can update own submissions" ON writing_submissions
    FOR UPDATE TO authenticated USING (student_id = auth.uid());

-- Teachers can read all submissions
CREATE POLICY "Teachers can read all submissions" ON writing_submissions
    FOR SELECT TO authenticated USING (
        EXISTS (
            SELECT 1 FROM users WHERE users.id = auth.uid() AND users.role = 'teacher'
        )
    );

-- Policies for writing_feedback
-- Teachers can insert feedback on any submission
CREATE POLICY "Teachers can insert feedback" ON writing_feedback
    FOR INSERT TO authenticated WITH CHECK (
        EXISTS (
            SELECT 1 FROM users WHERE users.id = auth.uid() AND users.role = 'teacher'
        )
    );

-- Teachers can read all feedback
CREATE POLICY "Teachers can read all feedback" ON writing_feedback
    FOR SELECT TO authenticated USING (
        EXISTS (
            SELECT 1 FROM users WHERE users.id = auth.uid() AND users.role = 'teacher'
        )
    );

-- Students can read feedback on their own submissions
CREATE POLICY "Students can read feedback on own submissions" ON writing_feedback
    FOR SELECT TO authenticated USING (
        EXISTS (
            SELECT 1 FROM writing_submissions ws
            WHERE ws.id = writing_feedback.submission_id
            AND ws.student_id = auth.uid()
        )
    );

-- Teachers can update their own feedback
CREATE POLICY "Teachers can update own feedback" ON writing_feedback
    FOR UPDATE TO authenticated USING (teacher_id = auth.uid());

-- Teachers can delete their own feedback
CREATE POLICY "Teachers can delete own feedback" ON writing_feedback
    FOR DELETE TO authenticated USING (teacher_id = auth.uid());

-- Grant permissions
GRANT SELECT ON writing_questions TO authenticated;
GRANT SELECT ON writing_samples TO authenticated;
GRANT SELECT, INSERT, UPDATE ON writing_submissions TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON writing_feedback TO authenticated;