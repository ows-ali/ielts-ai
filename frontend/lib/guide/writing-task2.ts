import type { GuideTopic } from "./types";

export const writingTask2Topic: GuideTopic = {
  id: "writing-task2",
  label: "Writing Task 2",
  emoji: "✍️",
  description:
    "Write at least 250 words in 40 minutes in response to a point of view, argument or problem. Your job is to present and support a position — not to describe.",
  structure: [
    {
      title: "Word & time limits",
      body: [
        "At least 250 words in 40 minutes. Plan for roughly 5 minutes of that total.",
      ],
    },
    {
      title: "The question types",
      body: [
        "Opinion (agree/disagree), discussion (both views), advantages/disadvantages, problems/solutions, and double question.",
      ],
    },
    {
      title: "The 4–5 paragraph shape",
      body: [
        "Introduction (paraphrase + clear position) → two body paragraphs (one idea each, fully developed) → conclusion (restate position).",
      ],
    },
    {
      title: "Length balance",
      body: [
        "Task 2 is 2/3 of your Writing score; Task 1 is 1/3. Spend your effort on strong body paragraphs, not a long introduction.",
      ],
    },
  ],
  process: [
    {
      title: "2 min — Read & underline",
      body: [
        "Identify the question type and underline the key words. Answer the whole question — every part of it.",
      ],
    },
    {
      title: "3 min — Plan",
      body: [
        "Choose two body ideas. For each: a claim, a reason, and a specific example.",
      ],
    },
    {
      title: "30 min — Write",
      body: [
        "Write the introduction with your position, then body 1, body 2 and the conclusion. Keep examples concrete, not generic.",
      ],
    },
    {
      title: "5 min — Check",
      body: [
        "Did you answer the question? Check word count, grammar, linking and punctuation.",
      ],
    },
  ],
  scoring: [
    {
      title: "Task Response (25%)",
      body: [
        "A full answer to all parts of the question, a clear position throughout, and well-developed ideas.",
      ],
    },
    {
      title: "Coherence & Cohesion (25%)",
      body: [
        "Logical flow between and inside paragraphs, with effective use of cohesive devices.",
      ],
    },
    {
      title: "Lexical Resource (25%)",
      body: [
        "A wide range of vocabulary, precise and natural word choice, and correct collocations.",
      ],
    },
    {
      title: "Grammatical Range & Accuracy (25%)",
      body: [
        "A variety of sentence structures with a high proportion of error-free sentences.",
      ],
    },
  ],
  bandAdvice: {
    5: {
      do: [
        "Take a clear position early and keep it consistent",
        "Write at least 250 words — under-length answers are capped around Band 5",
        "Give every paragraph one main idea with an example",
        "Use basic linking words correctly: however, therefore, for example",
      ],
      dont: [
        "Don't write about the general topic — answer the exact question asked",
        "Don't memorise essay templates — examiners penalise them",
        "Don't leave ideas unsupported: 'technology is bad' with no reason",
        "Don't introduce new ideas in the conclusion",
      ],
      tip: "Before writing, plan two body ideas and, for each, write claim → reason → concrete example. That structure alone lifts most Band 5 essays.",
    },
    6: {
      do: [
        "Address all parts of the question with a relevant position",
        "Develop ideas with reasons and examples, not repetition",
        "Use paragraphing and cohesive devices that don't feel forced",
        "Mix simple and complex sentences with generally accurate grammar",
      ],
      dont: [
        "Don't repeat the same idea in different words to hit the word count",
        "Don't use vague examples like 'in my country…' without specifics",
        "Don't leave your conclusion unclear or contradicting your body",
        "Don't overuse signposting: firstly… secondly… thirdly",
      ],
      tip: "Strengthen every body paragraph with a specific, named example — companies, studies, countries — and check each paragraph advances your position.",
    },
    7: {
      do: [
        "Present a clear position throughout, fully addressing the question",
        "Extend and support ideas with relevant, well-developed examples",
        "Use a range of cohesive devices effectively and naturally",
        "Show a good range of vocabulary and complex sentence structures",
      ],
      dont: [
        "Don't include irrelevant or half-developed examples",
        "Don't use formal words you can't control — errors then show",
        "Don't write unbalanced essays: huge introduction, thin body",
        "Don't chase fancy vocabulary while ignoring grammar accuracy",
      ],
      tip: "Write one strong, specific example per body paragraph and vary your sentence openings — most Band 7 gaps come from template-like essays.",
    },
    8: {
      do: [
        "Cover all requirements fully with a well-developed, precise position",
        "Argue with relevance, depth and skilful cohesion",
        "Use a wide, natural vocabulary with idiomatic precision",
        "Maintain control of grammar, with only occasional minor slips",
      ],
      dont: [
        "Don't sacrifice clarity for clever vocabulary",
        "Don't present both sides without a clear recommendation in opinion essays",
        "Don't add an example that doesn't strengthen the argument",
        "Don't skip the final proofread — polish is part of Band 8",
      ],
      tip: "Edit ruthlessly: cut every sentence that doesn't serve the argument, tighten the conclusion to a single confident position, and proofread twice.",
    },
  },
};
