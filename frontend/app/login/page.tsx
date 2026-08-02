"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input, Label } from "@/components/ui/input";
import { createClient } from "@/lib/supabase/client";

export default function LoginPage() {
  const router = useRouter();
  const supabase = createClient();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });
    setLoading(false);
    if (error) {
      setError(error.message);
      return;
    }
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
      return;
    }
    const me = await res.json();
    router.replace(me.role === "teacher" ? "/teacher" : "/student");
    router.refresh();
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-4 sm:p-6 bg-slate-900 text-slate-100 relative overflow-hidden">
      {/* Background Ambient Glows */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-gradient-to-tr from-indigo-600/20 via-violet-600/20 to-emerald-500/10 rounded-full blur-3xl pointer-events-none" />

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
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="you@example.com"
                  className="bg-slate-900/90 border-slate-800 text-slate-100 placeholder:text-slate-500 focus:border-indigo-500 focus:ring-indigo-500/20"
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
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  className="bg-slate-900/90 border-slate-800 text-slate-100 placeholder:text-slate-500 focus:border-indigo-500 focus:ring-indigo-500/20"
                />
              </div>
              {error && (
                <div className="rounded-lg bg-rose-500/10 border border-rose-500/30 p-3 text-xs font-medium text-rose-400">
                  {error}
                </div>
              )}
              <Button
                type="submit"
                className="w-full bg-gradient-to-r from-indigo-600 via-violet-600 to-indigo-600 hover:from-indigo-500 hover:to-violet-500 text-white font-semibold shadow-lg shadow-indigo-600/30 transition-all duration-200"
                disabled={loading}
              >
                {loading ? "Signing in..." : "Sign in"}
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

        {/* Demo Users Hint */}
        <div className="rounded-xl border border-slate-800/80 bg-slate-950/40 p-4 text-xs text-slate-400 space-y-2 backdrop-blur-md">
          <p className="font-semibold text-slate-300 uppercase tracking-wider">Quick Demo Accounts:</p>
          <div className="grid grid-cols-2 gap-2 text-[11px]">
            <div>
              <span className="font-medium text-indigo-400">Teacher:</span> teacher1@example.com
            </div>
            <div>
              <span className="font-medium text-emerald-400">Student:</span> student1@example.com
            </div>
          </div>
          <p className="text-[10px] text-slate-500">Password for demo accounts: <code className="text-slate-300">DummyPass123!</code></p>
        </div>
      </div>
    </main>
  );
}
