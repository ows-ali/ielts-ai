import { redirect } from "next/navigation";

import { api } from "@/lib/api";
import { createClient } from "@/lib/supabase/server";
import type { User } from "@/lib/types";

export async function getSession() {
  const supabase = await createClient();
  const { data } = await supabase.auth.getSession();
  return data.session;
}

export async function getUserOrRedirect(): Promise<{ session: NonNullable<Awaited<ReturnType<typeof getSession>>>; user: User }> {
  const session = await getSession();
  if (!session) {
    redirect("/login");
  }
  let user: User;
  try {
    user = await api.me(session);
  } catch {
    redirect("/login");
  }
  return { session, user };
}

export async function getUserOrNull(): Promise<{
  session: Awaited<ReturnType<typeof getSession>>;
  user: User | null;
}> {
  const session = await getSession();
  if (!session) {
    return { session: null, user: null };
  }
  try {
    const user = await api.me(session);
    return { session, user };
  } catch {
    return { session: null, user: null };
  }
}

export async function requireTeacher() {
  const { user, session } = await getUserOrRedirect();
  if (user.role !== "teacher") {
    redirect("/student");
  }
  return { user, session };
}

export async function requireStudent() {
  const { user, session } = await getUserOrRedirect();
  if (user.role !== "student") {
    redirect("/teacher");
  }
  return { user, session };
}
