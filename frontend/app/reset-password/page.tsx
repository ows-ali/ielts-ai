"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import type { AuthChangeEvent } from "@supabase/supabase-js";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input, Label } from "@/components/ui/input";
import { Spinner } from "@/components/ui/spinner";
import { createClient } from "@/lib/supabase/client";

export default function ResetPasswordPage() {
  const router = useRouter();
  const supabase = createClient();
  const [checking, setChecking] = useState(true);
  const [valid, setValid] = useState(false);
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    let mounted = true;
    const { data: { subscription } } = supabase.auth.onAuthStateChange(
      (event: AuthChangeEvent) => {
        if (event === "PASSWORD_RECOVERY") {
          if (mounted) setValid(true);
        }
      }
    );
    supabase.auth.getSession().then(({ data }) => {
      if (mounted) {
        if (data.session) setValid(true);
        setChecking(false);
      }
    });
    return () => {
      mounted = false;
      subscription.unsubscribe();
    };
  }, [supabase]);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    if (password.length < 8) {
      setError("Password must be at least 8 characters.");
      return;
    }
    if (password !== confirm) {
      setError("Passwords do not match.");
      return;
    }
    setLoading(true);
    const { error } = await supabase.auth.updateUser({ password });
    setLoading(false);
    if (error) {
      setError(error.message);
      return;
    }
    await supabase.auth.signOut();
    router.replace("/login");
    router.refresh();
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
              Reset your password
            </CardTitle>
          </CardHeader>
          <CardContent className="pt-6">
            {checking ? (
              <div className="flex items-center justify-center py-8">
                <Spinner className="h-8 w-8" />
              </div>
            ) : !valid ? (
              <div className="space-y-4 text-center">
                <div className="rounded-lg border border-amber-500/30 bg-amber-500/10 p-4 text-sm font-medium text-amber-300">
                  This password reset link is invalid or has expired. Request a
                  new link to continue.
                </div>
                <Button
                  variant="secondary"
                  className="w-full"
                  onClick={() => router.replace("/forgot-password")}
                >
                  Request a new link
                </Button>
              </div>
            ) : (
              <form onSubmit={onSubmit} className="space-y-4">
                <div className="space-y-1.5">
                  <Label htmlFor="password" className="text-xs font-semibold text-slate-300 uppercase tracking-wider">
                    New password
                  </Label>
                  <Input
                    id="password"
                    type="password"
                    required
                    minLength={8}
                    disabled={loading}
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="At least 8 characters"
                    className="bg-slate-900/90 border-slate-800 text-slate-100 placeholder:text-slate-500 focus:border-indigo-500 focus:ring-indigo-500/20 disabled:opacity-50"
                  />
                </div>
                <div className="space-y-1.5">
                  <Label htmlFor="confirm" className="text-xs font-semibold text-slate-300 uppercase tracking-wider">
                    Confirm password
                  </Label>
                  <Input
                    id="confirm"
                    type="password"
                    required
                    minLength={8}
                    disabled={loading}
                    value={confirm}
                    onChange={(e) => setConfirm(e.target.value)}
                    placeholder="Repeat your new password"
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
                  {loading ? "Saving..." : "Set new password"}
                </Button>
              </form>
            )}
          </CardContent>
        </Card>
      </div>
    </main>
  );
}
