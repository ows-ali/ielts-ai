"use client";

import type { ReactNode } from "react";

const PALETTE = [
  "#6366f1",
  "#10b981",
  "#f59e0b",
  "#ef4444",
  "#8b5cf6",
  "#06b6d4",
];

function fmt(value: number | string): string {
  if (typeof value === "number") {
    if (Number.isInteger(value)) return String(value);
    return value.toFixed(1);
  }
  return String(value);
}

function LineChart({ data }: { data: Record<string, unknown> }) {
  const xAxis = (data.x_axis as (number | string)[]) || [];
  const series = (data.series as { name: string; data: (number | string)[] }[]) || [];
  const unit = (data.unit as string) || "";

  const allValues = series.flatMap((s) => s.data.map(Number));
  const max = Math.max(...allValues, 1) * 1.1;
  const min = Math.min(...allValues, 0);

  const width = 640;
  const height = 260;
  const padL = 50;
  const padR = 16;
  const padT = 16;
  const padB = 34;

  const x = (i: number) => padL + (i * (width - padL - padR)) / Math.max(xAxis.length - 1, 1);
  const y = (v: number) => padT + (height - padT - padB) * (1 - (v - min) / (max - min || 1));

  return (
    <div>
      <svg viewBox={`0 0 ${width} ${height}`} className="w-full" role="img" aria-label="Line chart">
        {Array.from({ length: 5 }).map((_, i) => {
          const gy = padT + (i * (height - padT - padB)) / 4;
          const gv = min + ((max - min) * (4 - i)) / 4;
          return (
            <g key={i}>
              <line x1={padL} y1={gy} x2={width - padR} y2={gy} stroke="#e2e8f0" strokeWidth={1} />
              <text x={padL - 6} y={gy + 4} textAnchor="end" fontSize={10} fill="#94a3b8">
                {Math.round(gv)}
              </text>
            </g>
          );
        })}
        {series.map((s, si) => {
          const pts = s.data.map((v, i) => `${x(i)},${y(Number(v))}`);
          return (
            <g key={si}>
              <polyline
                points={pts.join(" ")}
                fill="none"
                stroke={PALETTE[si % PALETTE.length]}
                strokeWidth={2.5}
                strokeLinejoin="round"
              />
              {s.data.map((v, i) => (
                <circle key={i} cx={x(i)} cy={y(Number(v))} r={3.5} fill={PALETTE[si % PALETTE.length]} />
              ))}
            </g>
          );
        })}
        {xAxis.map((t, i) => (
          <text key={i} x={x(i)} y={height - 10} textAnchor="middle" fontSize={10} fill="#64748b">
            {fmt(t)}
          </text>
        ))}
      </svg>
      <div className="mt-2 flex flex-wrap items-center justify-center gap-4">
        {series.map((s, si) => (
          <span key={si} className="flex items-center gap-1.5 text-xs font-medium text-slate-600">
            <span className="h-2 w-2 rounded-full" style={{ background: PALETTE[si % PALETTE.length] }} />
            {s.name}
          </span>
        ))}
        {unit && <span className="text-[11px] text-slate-400">({unit})</span>}
      </div>
    </div>
  );
}

function BarChart({ data }: { data: Record<string, unknown> }) {
  const categories = (data.categories as string[]) || [];
  const series = (data.series as { name: string; data: (number | string)[] }[]) || [];
  const unit = (data.unit as string) || "";

  const allValues = series.flatMap((s) => s.data.map(Number));
  const max = Math.max(...allValues, 1) * 1.1;

  const width = 640;
  const height = 260;
  const padL = 46;
  const padR = 16;
  const padT = 16;
  const padB = 34;

  const groupW = (width - padL - padR) / categories.length;
  const barW = Math.min((groupW * 0.8) / Math.max(series.length, 1), 56);
  const y = (v: number) => padT + (height - padT - padB) * (1 - v / max);

  return (
    <div>
      <svg viewBox={`0 0 ${width} ${height}`} className="w-full" role="img" aria-label="Bar chart">
        {Array.from({ length: 5 }).map((_, i) => {
          const gy = padT + (i * (height - padT - padB)) / 4;
          const gv = (max * (4 - i)) / 4;
          return (
            <g key={i}>
              <line x1={padL} y1={gy} x2={width - padR} y2={gy} stroke="#e2e8f0" strokeWidth={1} />
              <text x={padL - 6} y={gy + 4} textAnchor="end" fontSize={10} fill="#94a3b8">
                {Math.round(gv)}
              </text>
            </g>
          );
        })}
        {categories.map((cat, ci) => {
          const cx = padL + ci * groupW + groupW / 2;
          return (
            <g key={cat}>
              {series.map((s, si) => {
                const bx = cx - (series.length * barW) / 2 + si * barW;
                const v = Number(s.data[ci]);
                return (
                  <rect
                    key={si}
                    x={bx}
                    y={y(v)}
                    width={barW - 3}
                    height={height - padT - padB - y(v) + padT}
                    fill={PALETTE[si % PALETTE.length]}
                    rx={3}
                  />
                );
              })}
              <text x={cx} y={height - 10} textAnchor="middle" fontSize={10} fill="#64748b">
                {cat}
              </text>
            </g>
          );
        })}
      </svg>
      <div className="mt-2 flex flex-wrap items-center justify-center gap-4">
        {series.map((s, si) => (
          <span key={si} className="flex items-center gap-1.5 text-xs font-medium text-slate-600">
            <span className="h-2 w-2 rounded-full" style={{ background: PALETTE[si % PALETTE.length] }} />
            {s.name}
          </span>
        ))}
        {unit && <span className="text-[11px] text-slate-400">({unit})</span>}
      </div>
    </div>
  );
}

function PieChart({ data }: { data: Record<string, unknown> }) {
  const slices = (data.slices as { label: string; value: number }[]) || [];
  const total = slices.reduce((sum, s) => sum + Number(s.value), 0);
  let angle = -90;

  const arc = (start: number, end: number, r: number) => {
    const large = end - start > 180 ? 1 : 0;
    const x1 = 100 + r * Math.cos((Math.PI * start) / 180);
    const y1 = 100 + r * Math.sin((Math.PI * start) / 180);
    const x2 = 100 + r * Math.cos((Math.PI * end) / 180);
    const y2 = 100 + r * Math.sin((Math.PI * end) / 180);
    return `M ${x1} ${y1} A ${r} ${r} 0 ${large} 1 ${x2} ${y2} L 100 100 Z`;
  };

  return (
    <div className="flex flex-col items-center gap-3 sm:flex-row">
      <svg viewBox="0 0 200 200" className="h-52 w-52 shrink-0" role="img" aria-label="Pie chart">
        {slices.map((s, si) => {
          const start = angle;
          const sweep = (Number(s.value) / total) * 360;
          const end = start + sweep;
          angle = end;
          return (
            <path
              key={si}
              d={arc(start, end, 90)}
              fill={PALETTE[si % PALETTE.length]}
              stroke="#fff"
              strokeWidth={1.5}
            />
          );
        })}
      </svg>
      <ul className="space-y-1.5">
        {slices.map((s, si) => (
          <li key={si} className="flex items-center gap-2 text-sm text-slate-700">
            <span className="h-2.5 w-2.5 rounded-sm" style={{ background: PALETTE[si % PALETTE.length] }} />
            <span className="font-medium">{s.label}</span>
            <span className="text-slate-500">{Number(s.value)}%</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

function DataTable({ data }: { data: Record<string, unknown> }) {
  const columns = (data.columns as string[]) || [];
  const rows = (data.rows as (string | number)[][]) || [];
  return (
    <div className="overflow-x-auto">
      <table className="w-full border-collapse text-sm">
        <thead>
          <tr>
            {columns.map((c, i) => (
              <th
                key={i}
                className="border border-slate-200 bg-slate-50 px-3 py-2 text-left font-semibold text-slate-700"
              >
                {c}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, ri) => (
            <tr key={ri} className={ri % 2 ? "bg-slate-50/50" : "bg-white"}>
              {row.map((cell, ci) => (
                <td key={ci} className="border border-slate-200 px-3 py-2 text-slate-700">
                  {ci === 0 ? <span className="font-medium">{cell}</span> : fmt(cell)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function MapDescription({ data }: { data: Record<string, unknown> }) {
  const maps = (data.maps as string[]) || [];
  const before = (data.before as string[]) || [];
  const after = (data.after as string[]) || [];

  return (
    <div className="grid gap-3 sm:grid-cols-2">
      {( [["Before", before, "#f1f5f9"], ["After", after, "#ecfdf5"]] as const ).map(([label, items, bg]) => (
        <div key={label} className="rounded-lg border border-slate-200 p-3" style={{ background: bg }}>
          <p className="mb-2 text-xs font-bold uppercase tracking-wide text-slate-500">{label}</p>
          <ul className="space-y-1.5">
            {items.map((item, i) => (
              <li key={i} className="flex gap-1.5 text-sm text-slate-700">
                <span className="mt-1.5 h-1 w-1 shrink-0 rounded-full bg-slate-400" />
                {item}
              </li>
            ))}
          </ul>
        </div>
      ))}
      {maps.length === 0 && (
        <div className="rounded-lg border border-amber-200 bg-amber-50 p-4 text-sm text-amber-700 sm:col-span-2">
          An image of the map(s) accompanies this question. Compare the two maps below if available.
        </div>
      )}
    </div>
  );
}

function ProcessDiagram({ data }: { data: Record<string, unknown> }) {
  const steps = (data.steps as string[]) || [];
  const title = (data.title as string) || "Process";
  return (
    <div className="space-y-2">
      <p className="text-xs font-bold uppercase tracking-wide text-slate-500">{title}</p>
      {steps.map((step, i) => (
        <div key={i} className="flex items-start gap-3 rounded-lg border border-slate-200 bg-white p-2.5">
          <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-indigo-600 text-xs font-bold text-white">
            {i + 1}
          </span>
          <p className="text-sm text-slate-700">{step}</p>
          {i < steps.length - 1 && (
            <span className="ml-auto shrink-0 text-slate-300">↓</span>
          )}
        </div>
      ))}
    </div>
  );
}

export function WritingVisual({ data, imageUrl }: { data?: Record<string, unknown> | null; imageUrl?: string | null }) {
  let content: ReactNode = null;

  if (data?.type === "line") content = <LineChart data={data} />;
  else if (data?.type === "bar") content = <BarChart data={data} />;
  else if (data?.type === "pie") content = <PieChart data={data} />;
  else if (data?.type === "table") content = <DataTable data={data} />;
  else if (data?.type === "map") content = <MapDescription data={data} />;
  else if (data?.type === "process") content = <ProcessDiagram data={data} />;
  else if (data?.type === "multi") {
    const charts = (data.charts as Record<string, unknown>[]) || [];
    content = (
      <div className="space-y-4">
        {charts.map((c, i) => (
          <div key={i} className="rounded-lg border border-slate-200 bg-slate-50/50 p-3">
            {typeof c.title === "string" && (
              <p className="mb-2 text-center text-xs font-bold uppercase tracking-wide text-slate-500">
                {c.title}
              </p>
            )}
            <WritingVisual data={c} />
          </div>
        ))}
      </div>
    );
  }

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
      {imageUrl ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={imageUrl}
          alt="Writing prompt visual"
          className="mx-auto max-h-96 w-auto rounded-lg"
        />
      ) : content ? (
        content
      ) : (
        <p className="text-sm text-slate-400">No visual data for this question.</p>
      )}
    </div>
  );
}
