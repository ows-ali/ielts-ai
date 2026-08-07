import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";

import ForgotPasswordPage from "@/app/forgot-password/page";

const mocks = vi.hoisted(() => ({
  router: { replace: vi.fn(), refresh: vi.fn() },
  resetPasswordForEmail: vi.fn(),
}));

vi.mock("next/navigation", () => ({
  useRouter: () => mocks.router,
}));

vi.mock("@/lib/supabase/client", () => ({
  createClient: () => ({
    auth: {
      resetPasswordForEmail: mocks.resetPasswordForEmail,
    },
  }),
}));

describe("ForgotPasswordPage", () => {
  beforeEach(() => {
    mocks.router.replace.mockReset();
    mocks.resetPasswordForEmail.mockReset();
  });

  it("renders the forgot-password form", () => {
    render(<ForgotPasswordPage />);
    expect(screen.getByLabelText("Email")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Send reset link" })).toBeInTheDocument();
  });

  it("sends a reset link with the current origin as redirect target", async () => {
    mocks.resetPasswordForEmail.mockResolvedValue({ error: null });
    Object.defineProperty(window, "location", {
      writable: true,
      value: { origin: "http://localhost:3000" },
    });

    const user = userEvent.setup();
    render(<ForgotPasswordPage />);
    await user.type(screen.getByLabelText("Email"), "teacher1@example.com");
    await user.click(screen.getByRole("button", { name: "Send reset link" }));

    await waitFor(() =>
      expect(mocks.resetPasswordForEmail).toHaveBeenCalledWith(
        "teacher1@example.com",
        { redirectTo: "http://localhost:3000/reset-password" }
      )
    );
    expect(
      await screen.findByText(/we've sent you a password reset link/i)
    ).toBeInTheDocument();
  });

  it("shows an error when sending the link fails", async () => {
    mocks.resetPasswordForEmail.mockResolvedValue({
      error: { message: "Email provider is not configured" },
    });

    const user = userEvent.setup();
    render(<ForgotPasswordPage />);
    await user.type(screen.getByLabelText("Email"), "x@example.com");
    await user.click(screen.getByRole("button", { name: "Send reset link" }));

    expect(
      await screen.findByText("Email provider is not configured")
    ).toBeInTheDocument();
    expect(mocks.router.replace).not.toHaveBeenCalled();
  });
});
