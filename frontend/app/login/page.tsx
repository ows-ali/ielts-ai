"use client";

import { useRouter } from "next/navigation";
import Link from "next/link";
import { useState } from "react";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input, Label } from "@/components/ui/input";
import { createClient } from "@/lib/supabase/client";

const DEMO_ACCOUNTS = [
  { role: "Student 1", email: "student1@example.com", pass: "DummyPass123!", color: "emerald" },
  { role: "Student 2", email: "student2@example.com", pass: "DummyPass123!", color: "emerald" },
];

export default function LoginPage() {
  const router = useRouter();
  const supabase = createClient();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [loadingMessage, setLoadingMessage] = useState("");
  const [copiedKey, setCopiedKey] = useState<string | null>(null);

  const copyToClipboard = async (text: string, key: string) => {
    try {
      await navigator.clipboard.writeText(text);
      setCopiedKey(key);
      setTimeout(() => setCopiedKey(null), 1800);
    } catch {
      /* ignore clipboard errors */
    }
  };

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    setLoadingMessage("Signing in...");
    try {
      const { data, error } = await supabase.auth.signInWithPassword({
        email,
        password,
      });
      if (error) {
        setError(error.message);
        setLoading(false);
        setLoadingMessage("");
        return;
      }
      setLoadingMessage("Verifying profile...");
      const res = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/api/auth/me`,
        {
          headers: { Authorization: `Bearer ${data.session.access_token}` },
          cache: "no-store",
        }
      );
      if (!res.ok) {
        if (res.status === 401) {
          await supabase.auth.signOut();
        }
        let detail = "Failed to load your profile.";
        try {
          const body = await res.json();
          detail = typeof body.detail === "string" ? body.detail : detail;
        } catch {
          /* ignore */
        }
        setError(detail);
        setLoading(false);
        setLoadingMessage("");
        return;
      }
      const me = await res.json();
      setLoadingMessage(me.role === "teacher" ? "Redirecting to Teacher Dashboard..." : "Redirecting to Student Dashboard...");
      router.replace(me.role === "teacher" ? "/teacher" : "/student");
      router.refresh();
    } catch (err) {
      setError(err instanceof Error ? err.message : "An unexpected error occurred.");
      setLoading(false);
      setLoadingMessage("");
    }
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-4 sm:p-6 bg-slate-900 text-slate-100 relative overflow-hidden">
      {/* Background Ambient Glows */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-gradient-to-tr from-indigo-600/20 via-violet-600/20 to-emerald-500/10 rounded-full blur-3xl pointer-events-none" />

      <Link
        href="/"
        className="absolute left-4 top-4 sm:left-6 sm:top-6 z-10 inline-flex items-center gap-1.5 rounded-lg border border-slate-700 bg-slate-800/60 px-3 py-1.5 text-xs font-semibold text-slate-300 backdrop-blur-md transition-colors hover:bg-slate-700 hover:text-white"
      >
        ← Back to home
      </Link>

      <div className="w-full max-w-md space-y-6 relative z-10">
        {/* Fancy Logo Branding */}
        <div className="flex flex-col items-center justify-center text-center space-y-3">
          <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-tr from-indigo-600 via-violet-600 to-emerald-500 shadow-xl shadow-indigo-500/30 ring-1 ring-white/20">
            <span className="font-black text-white text-3xl tracking-tighter">i</span>
          </div>
          <div>
            <div className="flex items-center justify-center gap-2">
              <h1 className="text-3xl font-black tracking-tight text-white font-sans">
                IELTS
              </h1>
              <span className="rounded-full bg-indigo-500/20 px-2.5 py-0.5 text-xs font-bold text-indigo-300 border border-indigo-500/30 uppercase tracking-widest">
                AI CLASSROOM
              </span>
            </div>
            <p className="mt-1.5 text-sm text-slate-400">
              Real-time speaking practice with instant AI evaluation
            </p>
          </div>
        </div>

        <Card className="border-slate-800 bg-slate-950/80 backdrop-blur-xl shadow-2xl shadow-black/50 text-slate-100">
          <CardHeader className="space-y-1 text-center border-b border-slate-800/80 pb-4">
            <CardTitle className="text-xl font-bold text-slate-100">
              Sign in to your account
            </CardTitle>
          </CardHeader>
          <CardContent className="pt-6">
            <form onSubmit={onSubmit} className="space-y-4">
              <div className="space-y-1.5">
                <Label htmlFor="email" className="text-xs font-semibold text-slate-300 uppercase tracking-wider">
                  Email
                </Label>
                <Input
                  id="email"
                  type="email"
                  required
                  disabled={loading}
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="you@example.com"
                  className="bg-slate-900/90 border-slate-800 text-slate-100 placeholder:text-slate-500 focus:border-indigo-500 focus:ring-indigo-500/20 disabled:opacity-50"
                />
              </div>
              <div className="space-y-1.5">
                <Label htmlFor="password" className="text-xs font-semibold text-slate-300 uppercase tracking-wider">
                  Password
                </Label>
                <Input
                  id="password"
                  type="password"
                  required
                  disabled={loading}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  className="bg-slate-900/90 border-slate-800 text-slate-100 placeholder:text-slate-500 focus:border-indigo-500 focus:ring-indigo-500/20 disabled:opacity-50"
                />
                <div className="flex justify-end">
                  <a
                    href="/forgot-password"
                    className="text-xs font-semibold text-indigo-400 hover:text-indigo-300 hover:underline"
                  >
                    Forgot password?
                  </a>
                </div>
              </div>
              {error && (
                <div className="rounded-lg bg-rose-500/10 border border-rose-500/30 p-3 text-xs font-medium text-rose-400">
                  {error}
                </div>
              )}
              {loading && (
                <div className="flex items-center gap-3 rounded-lg bg-indigo-500/15 border border-indigo-500/30 p-3 text-xs font-medium text-indigo-200 animate-pulse">
                  <svg className="animate-spin h-4 w-4 shrink-0 text-indigo-400" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                  </svg>
                  <span>{loadingMessage || "Signing in... Please wait"}</span>
                </div>
              )}
              <Button
                type="submit"
                className="w-full bg-gradient-to-r from-indigo-600 via-violet-600 to-indigo-600 hover:from-indigo-500 hover:to-violet-500 text-white font-semibold shadow-lg shadow-indigo-600/30 transition-all duration-200 disabled:opacity-75"
                disabled={loading}
              >
                {loading ? (
                  <span className="flex items-center justify-center gap-2">
                    <svg className="animate-spin h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                    </svg>
                    <span>{loadingMessage || "Signing in..."}</span>
                  </span>
                ) : (
                  "Sign in"
                )}
              </Button>
            </form>
            <p className="mt-6 text-center text-xs text-slate-400">
              Need an account?{" "}
              <a href="/register" className="font-semibold text-indigo-400 hover:text-indigo-300 hover:underline">
                Register here
              </a>
            </p>
          </CardContent>
        </Card>

        {/* Demo Users Section */}
        <div className="rounded-xl border border-slate-800/80 bg-slate-950/60 p-4 text-xs text-slate-400 space-y-3 backdrop-blur-md">
          <div className="flex items-center justify-between">
            <span className="font-semibold text-slate-200 uppercase tracking-wider text-[11px]">
              Quick Demo Accounts
            </span>
            <span className="text-[10px] text-slate-500">1-Click Copy & Fill</span>
          </div>

          <div className="grid gap-2">
            {DEMO_ACCOUNTS.map((acc) => {
              const emailKey = `email-${acc.email}`;
              const passKey = `pass-${acc.email}`;
              const isTeacher = acc.color === "indigo";
              return (
                <div
                  key={acc.email}
                  className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 rounded-lg border border-slate-800/60 bg-slate-900/60 p-2.5 transition-colors hover:border-slate-700/80"
                >
                  <div className="space-y-0.5 min-w-0">
                    <div className="flex items-center gap-2">
                      <span
                        className={`inline-block rounded px-1.5 py-0.5 text-[9px] font-bold uppercase tracking-wider ${
                          isTeacher
                            ? "bg-indigo-500/20 text-indigo-300 border border-indigo-500/30"
                            : "bg-emerald-500/20 text-emerald-300 border border-emerald-500/30"
                        }`}
                      >
                        {acc.role}
                      </span>
                      <span className="truncate text-[12px] font-medium text-slate-200">
                        {acc.email}
                      </span>
                    </div>
                    <div className="text-[10px] text-slate-400 flex items-center gap-1">
                      <span>Pass:</span>
                      <code className="text-slate-300 bg-slate-950/80 px-1 py-0.2 rounded font-mono">
                        {acc.pass}
                      </code>
                    </div>
                  </div>

                  <div className="flex items-center gap-1.5 shrink-0 pt-1 sm:pt-0">
                    {/* Copy Email Button */}
                    <button
                      type="button"
                      onClick={() => copyToClipboard(acc.email, emailKey)}
                      title="Copy Email"
                      className="flex items-center gap-1 rounded bg-slate-800/80 px-2 py-1 text-[10px] font-semibold text-slate-300 hover:bg-slate-700 hover:text-white transition-colors"
                    >
                      {copiedKey === emailKey ? (
                        <span className="text-emerald-400 font-bold">Copied ✓</span>
                      ) : (
                        <>
                          <svg className="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                          </svg>
                          <span>Email</span>
                        </>
                      )}
                    </button>

                    {/* Copy Password Button */}
                    <button
                      type="button"
                      onClick={() => copyToClipboard(acc.pass, passKey)}
                      title="Copy Password"
                      className="flex items-center gap-1 rounded bg-slate-800/80 px-2 py-1 text-[10px] font-semibold text-slate-300 hover:bg-slate-700 hover:text-white transition-colors"
                    >
                      {copiedKey === passKey ? (
                        <span className="text-emerald-400 font-bold">Copied ✓</span>
                      ) : (
                        <>
                          <svg className="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 0121 9z" />
                          </svg>
                          <span>Pass</span>
                        </>
                      )}
                    </button>

                    {/* Autofill Button */}
                    <button
                      type="button"
                      onClick={() => {
                        setEmail(acc.email);
                        setPassword(acc.pass);
                      }}
                      title="Autofill credentials into sign in form"
                      className="flex items-center gap-1 rounded bg-indigo-600/30 border border-indigo-500/40 px-2 py-1 text-[10px] font-bold text-indigo-300 hover:bg-indigo-600 hover:text-white transition-colors"
                    >
                      ⚡ Fill
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </main>
  );
}
