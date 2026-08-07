export type BandLevel = 5 | 6 | 7 | 8;

export type GuideTopicId = "speaking" | "writing-task1" | "writing-task2" | "scoring";

export interface BandAdvice {
  do: string[];
  dont: string[];
  tip: string;
}

export interface GuideSection {
  title: string;
  body: string[];
  bullets?: string[];
}

export interface GuideTopic {
  id: GuideTopicId;
  label: string;
  emoji: string;
  description: string;
  structure: GuideSection[];
  process: GuideSection[];
  scoring: GuideSection[];
  bandAdvice: Record<BandLevel, BandAdvice>;
}

export interface BandInfo {
  band: BandLevel;
  hasData: boolean;
}
