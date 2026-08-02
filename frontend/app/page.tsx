import { redirect } from "next/navigation";

import { getSession } from "@/lib/auth";
import { api } from "@/lib/api";

export const dynamic = "force-dynamic";

export default async function Home() {
  const session = await getSession();
  if (!session) {
    redirect("/login");
  }
  try {
    const user = await api.me(session);
    redirect(user.role === "teacher" ? "/teacher" : "/student");
  } catch {
    redirect("/login");
  }
}
