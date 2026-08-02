"use client";

import { useCallback } from "react";
import { useRouter } from "next/navigation";

import { ApiError } from "@/lib/api";
import { createClient } from "@/lib/supabase/client";

export function useUnauthorizedRedirect() {
  const router = useRouter();
  return useCallback(
    async (err: unknown) => {
      if (err instanceof ApiError && err.status === 401) {
        const supabase = createClient();
        await supabase.auth.signOut();
        router.replace("/login");
        router.refresh();
      }
    },
    [router]
  );
}
