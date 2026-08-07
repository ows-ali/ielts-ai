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
  const [writingOpen, setWritingOpen] = useState(false);

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

  const writingHref =
    userRole === "teacher" ? "/teacher/writing" : userRole === "student" ? "/student/writing" : null;

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
                {writingHref && (
                  <div className="relative">
                    <button
                      type="button"
                      onClick={() => setWritingOpen((o) => !o)}
                      className="flex items-center gap-1 rounded-lg px-3 py-1.5 text-sm font-semibold text-slate-600 transition-colors hover:bg-slate-100 hover:text-indigo-600"
                    >
                      Writing
                      <svg className="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor">
                        <path fillRule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clipRule="evenodd" />
                      </svg>
                    </button>
                    {writingOpen && (
                      <>
                        <div className="fixed inset-0 z-40" onClick={() => setWritingOpen(false)} />
                        <div className="absolute right-0 z-50 mt-1 w-56 rounded-xl border border-slate-200 bg-white p-1.5 shadow-xl">
                          <Link
                            href={writingHref}
                            onClick={() => setWritingOpen(false)}
                            className="block rounded-lg px-3 py-2 text-sm font-semibold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600"
                          >
                            Writing Task 1 Practice
                          </Link>
                          <Link
                            href="/student/writing/part2"
                            onClick={() => setWritingOpen(false)}
                            className="block rounded-lg px-3 py-2 text-sm font-semibold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600"
                          >
                            Writing Task 2 Practice
                          </Link>
                        </div>
                      </>
                    )}
                  </div>
                )}
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
                {writingHref && (
                  <div className="relative">
                    <button
                      type="button"
                      onClick={() => setWritingOpen((o) => !o)}
                      className="flex items-center gap-1 rounded-lg px-3 py-1.5 text-sm font-semibold text-slate-600 transition-colors hover:bg-slate-100 hover:text-indigo-600"
                    >
                      Writing
                      <svg className="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor">
                        <path fillRule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clipRule="evenodd" />
                      </svg>
                    </button>
                    {writingOpen && (
                      <>
                        <div className="fixed inset-0 z-40" onClick={() => setWritingOpen(false)} />
                        <div className="absolute right-0 z-50 mt-1 w-56 rounded-xl border border-slate-200 bg-white p-1.5 shadow-xl">
                          <Link
                            href={writingHref}
                            onClick={() => setWritingOpen(false)}
                            className="block rounded-lg px-3 py-2 text-sm font-semibold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600"
                          >
                            Writing Task 1 Review
                          </Link>
                          <Link
                            href="/teacher/writing/part2"
                            onClick={() => setWritingOpen(false)}
                            className="block rounded-lg px-3 py-2 text-sm font-semibold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600"
                          >
                            Writing Task 2 Review
                          </Link>
                        </div>
                      </>
                    )}
                  </div>
                )}
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
                {writingHref && (
                  <>
                    <Link
                      href={writingHref}
                      className="rounded-full bg-slate-100/80 px-3.5 py-1 text-xs font-bold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
                    >
                      Writing 1
                    </Link>
                    <Link
                      href="/student/writing/part2"
                      className="rounded-full bg-slate-100/80 px-3.5 py-1 text-xs font-bold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
                    >
                      Writing 2
                    </Link>
                  </>
                )}
                <Link
                  href="/student/report"
                  className="rounded-full bg-slate-100/80 px-3.5 py-1 text-xs font-bold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
                >
                  Progress Report
                </Link>
              </>
            )}
            {userRole === "teacher" && (
              <>
                <Link
                  href="/teacher"
                  className="rounded-full bg-slate-100/80 px-3.5 py-1 text-xs font-bold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
                >
                  Dashboard Home
                </Link>
                {writingHref && (
                  <>
                    <Link
                      href={writingHref}
                      className="rounded-full bg-slate-100/80 px-3.5 py-1 text-xs font-bold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
                    >
                      Writing 1
                    </Link>
                    <Link
                      href="/teacher/writing/part2"
                      className="rounded-full bg-slate-100/80 px-3.5 py-1 text-xs font-bold text-slate-700 hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
                    >
                      Writing 2
                    </Link>
                  </>
                )}
              </>
            )}
          </div>
        )}
      </div>
    </header>
  );
}
