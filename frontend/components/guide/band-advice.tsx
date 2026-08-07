"use client";

import { useState } from "react";

import { nextBandLabel } from "@/lib/guide";
import type { BandAdvice, BandLevel } from "@/lib/guide";

const BANDS: BandLevel[] = [5, 6, 7, 8];

export function BandAdviceBlock({
  advice,
  currentBand,
  hasData,
  skillLabel,
}: {
  advice: Record<BandLevel, BandAdvice>;
  currentBand: BandLevel;
  hasData: boolean;
  skillLabel: string;
}) {
  const [selected, setSelected] = useState<BandLevel>(currentBand);
  const a = advice[selected];
  const target = nextBandLabel(selected);

  return (
    <div className="rounded-xl border border-slate-200 bg-slate-50/50 p-4 sm:p-5">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <h4 className="text-sm font-bold uppercase tracking-wide text-slate-600">
          Band-specific advice
        </h4>
        <span className="rounded-full bg-indigo-50 px-2 py-0.5 text-xs font-semibold text-indigo-700 border border-indigo-100">
          {skillLabel}
        </span>
      </div>

      {hasData ? (
        <p className="mt-1.5 text-xs text-slate-500">
          Based on your current {skillLabel.toLowerCase()} band, this advice targets Band{" "}
          <span className="font-bold text-indigo-700">{currentBand}</span>. Switch bands below to
          see the journey to Band 8.
        </p>
      ) : (
        <p className="mt-1.5 text-xs text-slate-500">
          Complete an attempt to get personalised advice — showing Band 5 guidance for now.
        </p>
      )}

      <div className="mt-3 flex flex-wrap gap-1.5">
        {BANDS.map((b) => (
          <button
            key={b}
            type="button"
            onClick={() => setSelected(b)}
            aria-pressed={selected === b}
            className={`rounded-full px-3 py-1 text-xs font-bold transition-colors ${
              selected === b
                ? "bg-indigo-600 text-white shadow-sm"
                : "border border-slate-200 bg-white text-slate-600 hover:bg-slate-100"
            }`}
          >
            Band {b}
          </button>
        ))}
      </div>

      <div className="mt-4 grid gap-3 sm:grid-cols-2">
        <div className="rounded-lg border border-emerald-200 bg-emerald-50 p-3.5">
          <p className="text-xs font-bold uppercase tracking-wide text-emerald-700">Do</p>
          <ul className="mt-1.5 space-y-1.5">
            {a.do.map((item, i) => (
              <li key={i} className="flex gap-1.5 text-sm leading-relaxed text-emerald-900">
                <span className="shrink-0" aria-hidden>
                  ✓
                </span>
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>
        <div className="rounded-lg border border-rose-200 bg-rose-50 p-3.5">
          <p className="text-xs font-bold uppercase tracking-wide text-rose-700">Don&apos;t</p>
          <ul className="mt-1.5 space-y-1.5">
            {a.dont.map((item, i) => (
              <li key={i} className="flex gap-1.5 text-sm leading-relaxed text-rose-900">
                <span className="shrink-0" aria-hidden>
                  ✗
                </span>
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      <div className="mt-3 rounded-lg border border-amber-200 bg-amber-50 p-3.5">
        <p className="text-xs font-bold uppercase tracking-wide text-amber-700">
          To move to Band {target}
        </p>
        <p className="mt-1 text-sm leading-relaxed text-amber-900">{a.tip}</p>
      </div>
    </div>
  );
}
