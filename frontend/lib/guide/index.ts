import type { ProfileStats } from "@/lib/types";

import { scoringTopic } from "./scoring";
import { speakingTopic } from "./speaking";
import type { BandInfo, BandLevel, GuideTopic, GuideTopicId } from "./types";
import { writingTask1Topic } from "./writing-task1";
import { writingTask2Topic } from "./writing-task2";

export * from "./types";
export { scoringTopic } from "./scoring";
export { speakingTopic } from "./speaking";
export { writingTask1Topic } from "./writing-task1";
export { writingTask2Topic } from "./writing-task2";

export const guideTopics: GuideTopic[] = [
  speakingTopic,
  writingTask1Topic,
  writingTask2Topic,
  scoringTopic,
];

const BAND_MIN: BandLevel = 5;
const BAND_MAX: BandLevel = 8;

export function clampBand(value: number | null | undefined): BandLevel {
  if (value === null || value === undefined || Number.isNaN(value)) {
    return BAND_MIN;
  }
  const rounded = Math.round(value);
  if (rounded >= BAND_MAX) return BAND_MAX;
  if (rounded <= BAND_MIN) return BAND_MIN;
  return rounded as BandLevel;
}

export function nextBandLabel(band: BandLevel): string {
  return band >= BAND_MAX ? "9" : String(band + 1);
}

export function currentBandFor(topicId: GuideTopicId, stats: ProfileStats | null): BandInfo {
  if (!stats) {
    return { band: BAND_MIN, hasData: false };
  }
  if (topicId === "speaking") {
    return {
      band: clampBand(stats.avg_speaking_band),
      hasData: stats.total_speaking_attempts > 0,
    };
  }
  if (topicId === "writing-task1" || topicId === "writing-task2") {
    return {
      band: clampBand(stats.best_writing_band),
      hasData: stats.writing_submissions > 0,
    };
  }
  const any = stats.avg_speaking_band ?? stats.best_writing_band ?? null;
  return {
    band: clampBand(any),
    hasData: stats.total_speaking_attempts > 0 || stats.writing_submissions > 0,
  };
}
