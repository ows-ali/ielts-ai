"use client";

import { BandAdviceBlock } from "@/components/guide/band-advice";
import type { BandInfo, GuideSection, GuideTopic } from "@/lib/guide";

function SectionList({ heading, sections }: { heading: string; sections: GuideSection[] }) {
  return (
    <section>
      <h3 className="text-xs font-bold uppercase tracking-wide text-slate-500">{heading}</h3>
      <div className="mt-2 space-y-2">
        {sections.map((s) => (
          <div key={s.title} className="rounded-lg border border-slate-200 bg-white p-3.5">
            <p className="text-sm font-semibold text-slate-800">{s.title}</p>
            {s.body.map((p, i) => (
              <p key={i} className="mt-1 text-sm leading-relaxed text-slate-600">
                {p}
              </p>
            ))}
            {s.bullets && (
              <ul className="mt-1.5 space-y-1">
                {s.bullets.map((b, i) => (
                  <li key={i} className="flex gap-1.5 text-sm leading-relaxed text-slate-600">
                    <span className="shrink-0 text-indigo-500" aria-hidden>
                      •
                    </span>
                    <span>{b}</span>
                  </li>
                ))}
              </ul>
            )}
          </div>
        ))}
      </div>
    </section>
  );
}

function ProcessSteps({ sections }: { sections: GuideSection[] }) {
  return (
    <section>
      <h3 className="text-xs font-bold uppercase tracking-wide text-slate-500">
        How to attempt it
      </h3>
      <div className="mt-2 space-y-2">
        {sections.map((s, i) => (
          <div key={s.title} className="flex gap-3 rounded-lg border border-slate-200 bg-white p-3.5">
            <span className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-indigo-100 text-xs font-bold text-indigo-700">
              {i + 1}
            </span>
            <div className="min-w-0 flex-1">
              <p className="text-sm font-semibold text-slate-800">{s.title}</p>
              {s.body.map((p, j) => (
                <p key={j} className="mt-1 text-sm leading-relaxed text-slate-600">
                  {p}
                </p>
              ))}
              {s.bullets && (
                <ul className="mt-1.5 space-y-1">
                  {s.bullets.map((b, k) => (
                    <li key={k} className="flex gap-1.5 text-sm leading-relaxed text-slate-600">
                      <span className="shrink-0 text-indigo-500" aria-hidden>
                        •
                      </span>
                      <span>{b}</span>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export function GuideTopicView({
  topic,
  bandInfo,
  skillLabel,
}: {
  topic: GuideTopic;
  bandInfo: BandInfo;
  skillLabel: string;
}) {
  return (
    <div className="space-y-6">
      <div className="rounded-lg bg-indigo-50/70 p-4">
        <p className="text-sm leading-relaxed text-indigo-950">{topic.description}</p>
      </div>

      <SectionList heading="Structure & requirements" sections={topic.structure} />
      <ProcessSteps sections={topic.process} />
      <SectionList heading="How it's scored" sections={topic.scoring} />

      <BandAdviceBlock
        advice={topic.bandAdvice}
        currentBand={bandInfo.band}
        hasData={bandInfo.hasData}
        skillLabel={skillLabel}
      />
    </div>
  );
}
