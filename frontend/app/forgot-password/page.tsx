"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input, Label } from "@/components/ui/input";
import { createClient } from "@/lib/supabase/client";

export default function ForgotPasswordPage() {
  const router = useRouter();
  const supabase = createClient();
  const [email, setEmail] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [sent, setSent] = useState(false);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    const redirectTo = `${window.location.origin}/reset-password`;
    const { error } = await supabase.auth.resetPasswordForEmail(email, {
      redirectTo,
    });
    setLoading(false);
    if (error) {
      setError(error.message);
      return;
    }
    setSent(true);
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-4 sm:p-6 bg-slate-900 text-slate-100 relative overflow-hidden">
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-gradient-to-tr from-indigo-600/20 via-violet-600/20 to-emerald-500/10 rounded-full blur-3xl pointer-events-none" />

      <div className="w-full max-w-md space-y-6 relative z-10">
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
              Forgot your password?
            </CardTitle>
          </CardHeader>
          <CardContent className="pt-6">
            {sent ? (
              <div className="space-y-4 text-center">
                <div className="rounded-lg border border-emerald-500/30 bg-emerald-500/10 p-4 text-sm font-medium text-emerald-300">
                  If an account exists for that email, we&apos;ve sent you a
                  password reset link. Check your inbox (and spam folder).
                </div>
                <Button
                  variant="secondary"
                  className="w-full"
                  onClick={() => router.replace("/login")}
                >
                  Back to sign in
                </Button>
              </div>
            ) : (
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
                {error && (
                  <div className="rounded-lg bg-rose-500/10 border border-rose-500/30 p-3 text-xs font-medium text-rose-400">
                    {error}
                  </div>
                )}
                <Button
                  type="submit"
                  className="w-full bg-gradient-to-r from-indigo-600 via-violet-600 to-indigo-600 hover:from-indigo-500 hover:to-violet-500 text-white font-semibold shadow-lg shadow-indigo-600/30 transition-all duration-200 disabled:opacity-75"
                  disabled={loading}
                >
                  {loading ? "Sending link..." : "Send reset link"}
                </Button>
              </form>
            )}
            {!sent && (
              <p className="mt-6 text-center text-xs text-slate-400">
                Remembered your password?{" "}
                <a href="/login" className="font-semibold text-indigo-400 hover:text-indigo-300 hover:underline">
                  Sign in
                </a>
              </p>
            )}
          </CardContent>
        </Card>
      </div>
    </main>
  );
}
