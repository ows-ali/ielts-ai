import { redirect } from "next/navigation";

import { requireStudent } from "@/lib/auth";

export const dynamic = "force-dynamic";

export default async function MyProfileRedirectPage() {
  const { user } = await requireStudent();
  redirect(`/profile/${user.id}`);
}
