"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { SignOutButton } from "@/components/sign-out-button";
import { createClient } from "@/lib/supabase/client";

interface NavbarProps {
  userRole?: "teacher" | "student" | null;
  userName?: string | null;
}

export function Navbar({ userRole, userName }: NavbarProps) {
  const [displayName, setDisplayName] = useState<string | null>(userName || null);

  useEffect(() => {
    if (userName) {
      setDisplayName(userName);
      return;
    }
    const supabase = createClient();
    if (typeof supabase.auth?.getUser === "function") {
      supabase.auth.getUser().then(({ data }) => {
        if (data?.user) {
          const name = data.user.user_metadata?.name || data.user.email?.split("@")[0];
          if (name) setDisplayName(name);
        }
      }).catch(() => {});
    }
  }, [userName]);

  const homeHref = userRole === "teacher" ? "/teacher" : userRole === "student" ? "/student" : "/login";

  return (
    <header className="sticky top-0 z-50 w-full border-b border-slate-200/80 bg-white/90 backdrop-blur-md transition-all">
      <div className="mx-auto max-w-6xl px-4 py-2.5 sm:px-6">
        <div className="flex items-center justify-between gap-2">
          {/* Stylish Fancy IELTS Logo */}
          <Link href={homeHref} className="group flex items-center gap-2 transition-transform hover:scale-[1.02] shrink-0">
            <div className="flex h-8 w-8 sm:h-9 sm:w-9 items-center justify-center rounded-xl bg-gradient-to-tr from-indigo-600 via-violet-600 to-emerald-500 shadow-md shadow-indigo-500/20 group-hover:shadow-lg group-hover:shadow-indigo-500/30">
              <span className="font-extrabold text-white tracking-tighter text-base sm:text-lg">i</span>
            </div>
            <div className="flex items-center gap-1.5">
              <span className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-800 bg-clip-text font-black text-lg sm:text-xl tracking-tight text-transparent font-sans">
                IELTS
              </span>
              <span className="hidden sm:inline-block rounded-full bg-indigo-100 px-2 py-0.5 text-[10px] font-bold text-indigo-700 uppercase tracking-widest border border-indigo-200">
                AI CLASSROOM
              </span>
            </div>
          </Link>

          {/* Desktop Navigation Links */}
          <div className="hidden md:flex items-center gap-1">
            {userRole === "student" && (
              <nav className="flex items-center gap-1">
                <Link
                  href="/student"
                  className="rounded-lg px-3 py-1.5 text-sm font-semibold text-slate-600 transition-colors hover:bg-slate-100 hover:text-indigo-600"
                >
                  Home
                </Link>
                <Link
                  href="/student/report"
                  className="rounded-lg px-3 py-1.5 text-sm font-semibold text-slate-600 transition-colors hover:bg-slate-100 hover:text-indigo-600"
                >
                  Progress Report
                </Link>
              </nav>
            )}

            {userRole === "teacher" && (
              <nav className="flex items-center gap-1">
                <Link
                  href="/teacher"
                  className="rounded-lg px-3 py-1.5 text-sm font-semibold text-slate-600 transition-colors hover:bg-slate-100 hover:text-indigo-600"
                >
                  Dashboard Home
                </Link>
              </nav>
            )}
          </div>

          {/* User Badge & Sign Out */}
          <div className="flex items-center gap-2 shrink-0">
            {displayName && (
              <div className="flex items-center gap-1.5 rounded-full border border-slate-200 bg-slate-50/90 px-2.5 py-1 text-xs font-semibold text-slate-700 shadow-sm">
                <span className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse shrink-0" />
                <span className="max-w-[90px] sm:max-w-[150px] truncate">{displayName}</span>
              </div>
            )}
            <SignOutButton className="text-xs px-2.5 py-1 h-8" />
          </div>
        </div>

        {/* Mobile Navigation Bar */}
        {userRole && (
          <div className="mt-2 pt-2 border-t border-slate-100 md:hidden flex items-center justify-center gap-2">
            {userRole === "student" && (
              <>
                <Link
                  href="/student"
                  className="rounded-full bg-slate-100/80 px-3.5 py-1 text-xs font-bold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
                >
                  Home
                </Link>
                <Link
                  href="/student/report"
                  className="rounded-full bg-slate-100/80 px-3.5 py-1 text-xs font-bold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
                >
                  Progress Report
                </Link>
              </>
            )}
            {userRole === "teacher" && (
              <Link
                href="/teacher"
                className="rounded-full bg-slate-100/80 px-3.5 py-1 text-xs font-bold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
              >
                Dashboard Home
              </Link>
            )}
          </div>
        )}
      </div>
    </header>
  );
}
