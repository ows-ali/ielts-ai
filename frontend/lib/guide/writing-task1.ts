import type { GuideTopic } from "./types";

export const writingTask1Topic: GuideTopic = {
  id: "writing-task1",
  label: "Writing Task 1",
  emoji: "📊",
  description:
    "Write at least 150 words in 20 minutes. You must describe visual data — a graph, chart, table, map or process — objectively, without giving opinions.",
  structure: [
    {
      title: "Word & time limits",
      body: [
        "At least 150 words in 20 minutes. Under-length answers lose Task Achievement marks; there is no penalty for a few extra words.",
      ],
    },
    {
      title: "The data types",
      body: ["Line graphs, bar charts, pie charts, tables, maps/diagrams and process flows."],
    },
    {
      title: "The four-paragraph shape",
      body: [
        "Introduction (paraphrase the prompt) → Overview (the key trends, no numbers) → Details 1 → Details 2.",
        "The overview is the most important paragraph — missing it caps your Task Achievement score.",
      ],
    },
    {
      title: "No conclusion, no opinion",
      body: [
        "Unlike Task 2, you summarise the data. Never write 'I think' or recommend actions.",
      ],
    },
  ],
  process: [
    {
      title: "2–3 min — Analyse",
      body: [
        "What are the axes, units and time period? What is the biggest change? What is similar or different between series?",
      ],
    },
    {
      title: "2–3 min — Plan",
      body: [
        "Choose 2–3 key trends for the overview, then split the remaining details into two paragraphs with a clear theme each.",
      ],
    },
    {
      title: "12–13 min — Write",
      body: [
        "Write the introduction (paraphrase), then the overview, then two detail paragraphs with figures and comparisons.",
      ],
    },
    {
      title: "2–3 min — Check",
      body: [
        "Word count, verb tenses, articles and prepositions. Make sure every paragraph has one clear topic.",
      ],
    },
  ],
  scoring: [
    {
      title: "Task Achievement (25%)",
      body: [
        "Accurate data, a clear overview, all main features covered and no invented figures.",
      ],
    },
    {
      title: "Coherence & Cohesion (25%)",
      body: [
        "Logical organisation, clear paragraphing, and linking words that don't feel mechanical.",
      ],
    },
    {
      title: "Lexical Resource (25%)",
      body: [
        "Precise trend vocabulary — rose sharply, fluctuated, remained stable — and synonyms for increase and decrease.",
      ],
    },
    {
      title: "Grammatical Range & Accuracy (25%)",
      body: [
        "Complex sentences, correct comparisons, and accurate tense use for the time period in the data.",
      ],
    },
  ],
  bandAdvice: {
    5: {
      do: [
        "Always include an overview paragraph — the single biggest mark gain at Band 5",
        "Paraphrase the question in your own words in sentence one",
        "Describe the most obvious trend first",
        "Use basic trend language: increase, decrease, stay the same",
      ],
      dont: [
        "Don't write opinions or recommendations — 'this is bad for society' is a Band 5 killer",
        "Don't report every single number; select the main features",
        "Don't invent data the chart doesn't show",
        "Don't forget to compare series or years when the data shows them",
      ],
      tip: "Add a clear two-sentence overview right after the introduction, then organise the details into two separate paragraphs with one topic idea each.",
    },
    6: {
      do: [
        "Cover all main features with accurate figures",
        "Organise data into a logical sequence with clear paragraphing",
        "Use a mix of linking words that feel natural",
        "Use less common vocabulary for trends and change",
      ],
      dont: [
        "Don't start every sentence with 'The chart shows' — vary your openings",
        "Don't mix tenses across time periods; use past tense for past years",
        "Don't omit comparisons when two groups move differently",
        "Don't write a conclusion paragraph with an opinion",
      ],
      tip: "Rehearse a bank of trend vocabulary (rise, climb, plunge, plateau, dip) and always compare at least two data sets before you finish.",
    },
    7: {
      do: [
        "Give a well-developed overview of all key trends, then organised detail",
        "Use cohesive devices flexibly without over-linking: however, by contrast, meanwhile",
        "Show a wide range of vocabulary with precise data language",
        "Use complex structures: passive voice, comparatives, subordinate clauses",
      ],
      dont: [
        "Don't mechanically link every sentence — good cohesion is subtle",
        "Don't use vague words when precise ones exist ('went up' → 'surged')",
        "Don't quote numbers without saying what the movement implies",
        "Don't let small grammar slips — articles, plurals — accumulate",
      ],
      tip: "Interpret, don't transcribe: for every figure you quote, say what the movement implies, and vary your sentence subjects across each paragraph.",
    },
    8: {
      do: [
        "Address every requirement fully with a flawless overview",
        "Manage cohesion skilfully — paragraphs flow without visible linking phrases",
        "Use a wide, precise and natural range of vocabulary",
        "Write mostly error-free sentences with flexible structures",
      ],
      dont: [
        "Don't overdo the data — select what's significant and ignore the noise",
        "Don't use repeated 'the graph shows that…' openings",
        "Don't confuse similar figures; accuracy matters more than coverage",
        "Don't rush the final check — one misplaced tense can cost half a band",
      ],
      tip: "At Band 8, precision and restraint win: choose the 3–4 most significant features, describe them with varied structures, and leave time to proofread.",
    },
  },
};
