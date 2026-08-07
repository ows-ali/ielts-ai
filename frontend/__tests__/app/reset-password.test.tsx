import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";

import ResetPasswordPage from "@/app/reset-password/page";

const mocks = vi.hoisted(() => ({
  router: { replace: vi.fn(), refresh: vi.fn() },
  onAuthStateChange: vi.fn(),
  getSession: vi.fn(),
  updateUser: vi.fn(),
  signOut: vi.fn(),
  authEventCallback: {
    current: undefined as ((event: string) => void) | undefined,
  },
}));

vi.mock("next/navigation", () => ({
  useRouter: () => mocks.router,
}));

vi.mock("@/lib/supabase/client", () => ({
  createClient: () => ({
    auth: {
      onAuthStateChange: mocks.onAuthStateChange,
      getSession: mocks.getSession,
      updateUser: mocks.updateUser,
      signOut: mocks.signOut,
    },
  }),
}));

function mockAuthState() {
  mocks.onAuthStateChange.mockImplementation((callback: (event: string) => void) => {
    mocks.authEventCallback.current = callback;
    return { data: { subscription: { unsubscribe: vi.fn() } } };
  });
}

function fireEvent(event: string) {
  mocks.authEventCallback.current?.(event);
}

describe("ResetPasswordPage", () => {
  beforeEach(() => {
    mocks.router.replace.mockReset();
    mocks.router.refresh.mockReset();
    mocks.onAuthStateChange.mockReset();
    mocks.getSession.mockReset();
    mocks.updateUser.mockReset();
    mocks.signOut.mockReset();
    mocks.authEventCallback.current = undefined;
  });

  it("shows an invalid/expired message when there is no recovery session", async () => {
    mockAuthState();
    mocks.getSession.mockResolvedValue({ data: { session: null } });

    render(<ResetPasswordPage />);

    expect(
      await screen.findByText(/reset link is invalid or has expired/i)
    ).toBeInTheDocument();
  });

  it("shows the password form when a recovery session exists", async () => {
    mockAuthState();
    mocks.getSession.mockResolvedValue({ data: { session: { user: {} } } });

    render(<ResetPasswordPage />);

    expect(await screen.findByLabelText("New password")).toBeInTheDocument();
    expect(screen.getByLabelText("Confirm password")).toBeInTheDocument();
  });

  it("shows the password form on a PASSWORD_RECOVERY event", async () => {
    mockAuthState();
    mocks.getSession.mockResolvedValue({ data: { session: null } });

    render(<ResetPasswordPage />);
    await screen.findByText(/reset link is invalid or has expired/i);

    fireEvent("PASSWORD_RECOVERY");

    expect(await screen.findByLabelText("New password")).toBeInTheDocument();
  });

  it("shows an error when passwords do not match", async () => {
    mockAuthState();
    mocks.getSession.mockResolvedValue({ data: { session: { user: {} } } });

    const user = userEvent.setup();
    render(<ResetPasswordPage />);
    await user.type(await screen.findByLabelText("New password"), "NewPassword123");
    await user.type(screen.getByLabelText("Confirm password"), "Different123");
    await user.click(screen.getByRole("button", { name: "Set new password" }));

    expect(await screen.findByText("Passwords do not match.")).toBeInTheDocument();
    expect(mocks.updateUser).not.toHaveBeenCalled();
  });

  it("updates the password, signs out, and redirects to /login on success", async () => {
    mockAuthState();
    mocks.getSession.mockResolvedValue({ data: { session: { user: {} } } });
    mocks.updateUser.mockResolvedValue({ error: null });
    mocks.signOut.mockResolvedValue({ error: null });

    const user = userEvent.setup();
    render(<ResetPasswordPage />);
    await user.type(await screen.findByLabelText("New password"), "NewPassword123");
    await user.type(screen.getByLabelText("Confirm password"), "NewPassword123");
    await user.click(screen.getByRole("button", { name: "Set new password" }));

    await waitFor(() =>
      expect(mocks.updateUser).toHaveBeenCalledWith({ password: "NewPassword123" })
    );
    await waitFor(() => expect(mocks.signOut).toHaveBeenCalledTimes(1));
    await waitFor(() =>
      expect(mocks.router.replace).toHaveBeenCalledWith("/login")
    );
    expect(mocks.router.refresh).toHaveBeenCalled();
  });

  it("shows an error when updating the password fails", async () => {
    mockAuthState();
    mocks.getSession.mockResolvedValue({ data: { session: { user: {} } } });
    mocks.updateUser.mockResolvedValue({ error: { message: "Password too weak" } });

    const user = userEvent.setup();
    render(<ResetPasswordPage />);
    await user.type(await screen.findByLabelText("New password"), "NewPassword123");
    await user.type(screen.getByLabelText("Confirm password"), "NewPassword123");
    await user.click(screen.getByRole("button", { name: "Set new password" }));

    expect(await screen.findByText("Password too weak")).toBeInTheDocument();
    expect(mocks.signOut).not.toHaveBeenCalled();
    expect(mocks.router.replace).not.toHaveBeenCalled();
  });
});
