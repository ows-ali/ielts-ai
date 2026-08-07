import type { GuideTopic } from "./types";

export const speakingTopic: GuideTopic = {
  id: "speaking",
  label: "Speaking",
  emoji: "🎙️",
  description:
    "The Speaking test takes 11–14 minutes as a one-to-one interview with an examiner and is recorded. You are scored on fluency, vocabulary, grammar and pronunciation across three parts.",
  structure: [
    {
      title: "Part 1 — Interview (4–5 minutes)",
      body: [
        "The examiner asks short questions about familiar topics: your home, work or studies, hobbies, family and daily life.",
        "Purpose: warm you up and check your everyday, personal language.",
      ],
      bullets: [
        "Identity check, then 3 topic areas with 2–3 questions each",
        "Answers should be developed, not one or two words",
        "No card or notes — just conversation",
      ],
    },
    {
      title: "Part 2 — Long turn (3–4 minutes)",
      body: [
        "You receive a cue card with a topic and prompts. You have 1 minute to prepare and may take notes.",
        "You then speak for 1–2 minutes, followed by 1–2 questions from the examiner.",
      ],
      bullets: [
        "1 minute preparation time with a pen and paper",
        "Speak for 1–2 minutes without interruption",
        "Use your notes to structure: what, when, who, why",
      ],
    },
    {
      title: "Part 3 — Discussion (4–5 minutes)",
      body: [
        "The examiner asks abstract questions linked to your Part 2 topic — about society, trends, causes and effects.",
        "Purpose: test your ability to discuss ideas in depth, not just personal experience.",
      ],
      bullets: [
        "Two-way discussion — give opinions, reasons and examples",
        "Questions are more abstract than Part 1",
        "No card or notes",
      ],
    },
  ],
  process: [
    {
      title: "Listen to the full question",
      body: [
        "Don't interrupt or start answering halfway. If you don't catch something, it's fine to ask for repetition — it does not cost marks.",
      ],
    },
    {
      title: "Extend every answer",
      body: [
        "One-word answers cap you around Band 5–6. For each answer add a reason, an example or a contrast.",
      ],
      bullets: [
        "Answer + reason: 'I like running because it clears my head'",
        "Answer + example: 'For example, I train three times a week'",
        "Answer + contrast: 'Unlike most people, I prefer mornings'",
      ],
    },
    {
      title: "Structure your long turn",
      body: [
        "Give an opening sentence that states the main idea, describe the 'what', add detail (who, when, why), and close with a concluding comment.",
      ],
    },
    {
      title: "In Part 3, argue both sides",
      body: [
        "Give a clear position, support it with a reason and example, then acknowledge the other side before restating your view. This is where Band 7+ answers are won.",
      ],
    },
  ],
  scoring: [
    {
      title: "Fluency & Coherence (25%)",
      body: [
        "Speak at a natural pace without long pauses, link ideas logically, and structure your answers.",
      ],
    },
    {
      title: "Lexical Resource (25%)",
      body: [
        "Show a range of vocabulary, use less common words, and paraphrase when you don't have the exact word.",
      ],
    },
    {
      title: "Grammatical Range & Accuracy (25%)",
      body: [
        "Use a mix of simple and complex sentence forms with a good level of accuracy.",
      ],
    },
    {
      title: "Pronunciation (25%)",
      body: [
        "Be clear and easy to understand, with natural stress and intonation. Accent is irrelevant — clarity is what counts.",
      ],
    },
  ],
  bandAdvice: {
    5: {
      do: [
        "Answer every question — silence or 'I don't know' scores nothing",
        "Pause briefly to collect your thoughts instead of filling with 'um' and 'like'",
        "Use simple linking words: firstly, because, so, but",
        "Learn common topic vocabulary for daily life: home, work, hobbies, food",
      ],
      dont: [
        "Don't memorise long rehearsed answers — examiners spot them quickly",
        "Don't give one-word answers like 'Yes' or 'No'",
        "Don't abandon complex sentences because you fear making mistakes",
        "Don't rush — a steady pace with pauses beats a nervous blur",
      ],
      tip: "Focus on fluency first: practise speaking for 30–45 seconds on everyday topics without stopping, even if you make small grammar mistakes.",
    },
    6: {
      do: [
        "Speak at length on familiar topics with only short hesitation",
        "Introduce less common vocabulary and paraphrase when you forget a word",
        "Use a mix of simple and complex sentence forms",
        "Answer Part 3 questions with a clear opinion plus a reason",
      ],
      dont: [
        "Don't overuse the same words — good, bad, very, nice",
        "Don't abandon an idea mid-sentence; talk around it with examples",
        "Don't over-correct yourself in the middle of every answer",
        "Don't ignore the follow-up questions after your long turn",
      ],
      tip: "Broaden your vocabulary for Part 3 topics (education, technology, environment) and aim to give an opinion plus two supporting reasons for every answer.",
    },
    7: {
      do: [
        "Speak fluently, pausing only to search for ideas, not for words or grammar",
        "Use less common and idiomatic vocabulary where it feels natural",
        "Use complex structures flexibly: conditionals, relative clauses, reported speech",
        "Keep pronunciation clear with natural stress and intonation",
      ],
      dont: [
        "Don't force idioms into every answer — unnatural fits hurt more than they help",
        "Don't use memorised phrases that don't answer the question",
        "Don't let nerves speed you up; keep a measured pace",
        "Don't give a one-sided answer in Part 3 — acknowledge the other view",
      ],
      tip: "Work on Part 3 depth: make a claim, justify it with an example, concede a counterpoint, then restate your position.",
    },
    8: {
      do: [
        "Speak effortlessly, covering any topic with minimal hesitation",
        "Use a wide vocabulary with idiomatic phrasing and precise word choice",
        "Maintain full grammatical control, switching structures flexibly",
        "Sound natural with clear pronunciation, stress and intonation",
      ],
      dont: [
        "Don't rehearse — respond to the actual question every time",
        "Don't over-elaborate until the examiner needs to move you on",
        "Don't let a rare pronunciation slip compound — self-correct cleanly",
        "Don't ignore Part 3 nuance: compare, evaluate and qualify your views",
      ],
      tip: "Polish the last 5%: record yourself answering, then fix hesitations and unnatural intonation. Aim for measured, precise and engaging delivery.",
    },
  },
};
