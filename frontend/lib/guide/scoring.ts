import type { GuideTopic } from "./types";

export const scoringTopic: GuideTopic = {
  id: "scoring",
  label: "How Scoring Works",
  emoji: "🎯",
  description:
    "IELTS is scored on a 9-band scale. Your overall band is the average of the four skills — Listening, Reading, Writing and Speaking — rounded to the nearest half band. Each skill uses its own criteria.",
  structure: [
    {
      title: "The 9-band scale",
      body: [
        "Scores run from Band 0 (did not attempt) to Band 9 (expert user), with half bands such as 6.5 in between.",
      ],
      bullets: [
        "Band 9 — Expert user",
        "Band 8 — Very good user",
        "Band 7 — Good user",
        "Band 6 — Competent user",
        "Band 5 — Modest user",
        "Band 4 — Limited user",
      ],
    },
    {
      title: "Overall score = average of the four skills",
      body: [
        "Overall band = (Listening + Reading + Writing + Speaking) ÷ 4, rounded to the nearest half band.",
      ],
    },
    {
      title: "Writing score composition",
      body: [
        "Task 2 counts twice as much as Task 1: Writing band = (Task 1 + 2 × Task 2) ÷ 3.",
      ],
    },
    {
      title: "Sub-scores are equally weighted",
      body: [
        "Within each skill, every criterion is worth 25% of that skill's band.",
      ],
    },
  ],
  process: [
    {
      title: "Know your target",
      body: [
        "Most universities require 6.0–7.5 overall with a minimum in each skill. Write down your target per skill.",
      ],
    },
    {
      title: "Get an accurate baseline",
      body: [
        "Take a full practice test under timed conditions to find your true starting band before studying.",
      ],
    },
    {
      title: "Close your weakest criterion",
      body: [
        "Improving the lowest sub-score moves your overall band fastest. Focus there, not on your strengths.",
      ],
    },
    {
      title: "Practice under test conditions",
      body: [
        "Time every attempt, answer without notes, and record speaking answers. Then review every mistake.",
      ],
    },
    {
      title: "Reassess every 2–3 weeks",
      body: [
        "Re-take a full timed mock to confirm progress before you book the real exam.",
      ],
    },
  ],
  scoring: [
    {
      title: "Listening & Reading — right answers",
      body: [
        "Each has 40 questions. Your raw score maps to a band: roughly 23 correct = Band 6.0, 30 = Band 7.0, 35 = Band 8.0.",
      ],
    },
    {
      title: "Writing criteria",
      body: [
        "Task Achievement / Task Response, Coherence & Cohesion, Lexical Resource, Grammatical Range & Accuracy.",
      ],
    },
    {
      title: "Speaking criteria",
      body: [
        "Fluency & Coherence, Lexical Resource, Grammatical Range & Accuracy, Pronunciation.",
      ],
    },
    {
      title: "Half bands & rounding",
      body: [
        "An average of 6.75 rounds up to 7.0, while 6.25 rounds down to 6.0. A fraction of a band can matter — so polish counts.",
      ],
    },
  ],
  bandAdvice: {
    5: {
      do: [
        "Get an accurate baseline with a full timed mock test",
        "Learn the test format cold — structure, timing and question types",
        "Build everyday vocabulary and core grammar for each skill",
        "Set a realistic target with a deadline",
      ],
      dont: [
        "Don't study all skills equally if one is much weaker — prioritise",
        "Don't do only untimed practice; timing is half the battle",
        "Don't skip reviewing mistakes — the review is where you improve",
        "Don't book the real test before you can hit your target in a mock",
      ],
      tip: "At Band 5, spend about 70% of your time on timed practice tests and mistake review, and 30% on studying technique.",
    },
    6: {
      do: [
        "Fix repeated error patterns — articles, tenses, cohesion — systematically",
        "Expand vocabulary by topic: health, technology, education, environment",
        "Practise every question type, not just your favourites",
        "Score your own mocks against the official band descriptors",
      ],
      dont: [
        "Don't keep making the same mistakes in new tests — log them",
        "Don't memorise answers; memorise techniques and vocabulary",
        "Don't ignore sub-scores — target the lowest criterion in each skill",
        "Don't compare yourself to Band 9 speakers; compare to Band 7 descriptors",
      ],
      tip: "Keep a mistake log: every error you find in practice, note the pattern and re-test it in your next session. Logged mistakes get fixed.",
    },
    7: {
      do: [
        "Target the exact sub-scores that hold your average down",
        "Practise exam strategies: skimming, key-word matching, section time budgets",
        "Refine less common vocabulary and complex grammar in context",
        "Take full mocks under real conditions: timed and uninterrupted",
      ],
      dont: [
        "Don't neglect one skill while chasing an overall average",
        "Don't practise without feedback — self-assessment has a ceiling",
        "Don't let your strongest skill carry the average",
        "Don't book the test without a recent timed mock at target band",
      ],
      tip: "At Band 7, precision matters: score your mocks against the official descriptors and fix the sub-scores between your current band and 8.",
    },
    8: {
      do: [
        "Polish the highest-level nuances: idiom, intonation, essay depth",
        "Calibrate to the exact Band 8 descriptors across all four criteria",
        "Simulate full tests, including the paper-and-pencil or screen setup you'll use",
        "Manage exam-day fatigue and time pressure deliberately",
      ],
      dont: [
        "Don't chase Band 9 vocabulary at the cost of natural control",
        "Don't ignore your weakest skill — a 7.5 cap lowers the average",
        "Don't let overconfidence skip mock testing before the real exam",
        "Don't cram in the final week — consolidate what you already know",
      ],
      tip: "At Band 8, consistency and stamina are the goal: run full timed mocks, score yourself honestly, and fix the last uneven sub-scores.",
    },
  },
};
