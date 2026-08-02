"use client";

import Link from "next/link";
import { SignOutButton } from "@/components/sign-out-button";

interface NavbarProps {
  userRole?: "teacher" | "student" | null;
  userName?: string | null;
}

export function Navbar({ userRole, userName }: NavbarProps) {
  const homeHref = userRole === "teacher" ? "/teacher" : userRole === "student" ? "/student" : "/login";

  return (
    <header className="sticky top-0 z-50 w-full border-b border-slate-200/80 bg-white/80 backdrop-blur-md transition-all">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3 sm:px-6">
        {/* Stylish Fancy IELTS Logo */}
        <Link href={homeHref} className="group flex items-center gap-2 transition-transform hover:scale-[1.02]">
          <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-tr from-indigo-600 via-violet-600 to-emerald-500 shadow-md shadow-indigo-500/20 group-hover:shadow-lg group-hover:shadow-indigo-500/30">
            <span className="font-extrabold text-white tracking-tighter text-lg">i</span>
          </div>
          <div className="flex flex-col">
            <div className="flex items-center gap-1.5">
              <span className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-800 bg-clip-text font-black text-xl tracking-tight text-transparent font-sans">
                IELTS
              </span>
              <span className="rounded-full bg-indigo-100 px-2 py-0.5 text-[10px] font-bold text-indigo-700 uppercase tracking-widest border border-indigo-200">
                AI CLASSROOM
              </span>
            </div>
          </div>
        </Link>

        {/* Navigation Actions */}
        <div className="flex items-center gap-3">
          {userRole === "student" && (
            <nav className="flex items-center gap-1 sm:gap-2 mr-2">
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
            <nav className="flex items-center gap-1 sm:gap-2 mr-2">
              <Link
                href="/teacher"
                className="rounded-lg px-3 py-1.5 text-sm font-semibold text-slate-600 transition-colors hover:bg-slate-100 hover:text-indigo-600"
              >
                Dashboard Home
              </Link>
            </nav>
          )}

          {userName && (
            <div className="hidden sm:flex items-center gap-2 rounded-full border border-slate-200 bg-slate-50/80 px-3 py-1 text-xs font-medium text-slate-700">
              <span className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse" />
              <span>{userName}</span>
            </div>
          )}

          <SignOutButton />
        </div>
      </div>
    </header>
  );
}
