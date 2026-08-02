import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";

import LoginPage from "@/app/login/page";

const mocks = vi.hoisted(() => ({
  router: { replace: vi.fn(), refresh: vi.fn() },
  signIn: vi.fn(),
  signOut: vi.fn(),
}));

vi.mock("next/navigation", () => ({
  useRouter: () => mocks.router,
}));

vi.mock("@/lib/supabase/client", () => ({
  createClient: () => ({
    auth: {
      signInWithPassword: mocks.signIn,
      signOut: mocks.signOut,
    },
  }),
}));

function mockMeResponse(ok: boolean, body: unknown, detail?: string, status?: number) {
  const fn = vi.fn().mockResolvedValue({
    ok,
    status: status ?? (ok ? 200 : 500),
    json: async () => (ok ? body : { detail }),
  });
  vi.stubGlobal("fetch", fn);
  return fn;
}

async function submitLogin(email: string, password: string) {
  const user = userEvent.setup();
  await user.type(screen.getByLabelText("Email"), email);
  await user.type(screen.getByLabelText("Password"), password);
  await user.click(screen.getByRole("button", { name: "Sign in" }));
}

describe("LoginPage", () => {
  beforeEach(() => {
    mocks.router.replace.mockReset();
    mocks.router.refresh.mockReset();
    mocks.signIn.mockReset();
    mocks.signOut.mockReset();
  });

  it("renders the sign-in form", () => {
    render(<LoginPage />);
    expect(screen.getByLabelText("Email")).toBeInTheDocument();
    expect(screen.getByLabelText("Password")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Sign in" })).toBeInTheDocument();
  });

  it("redirects a teacher to /teacher after profile load", async () => {
    mocks.signIn.mockResolvedValue({
      data: { session: { access_token: "tok" } },
      error: null,
    });
    const fetchMock = mockMeResponse(true, { role: "teacher" });

    render(<LoginPage />);
    await submitLogin("t@example.com", "pw");

    await waitFor(() => expect(mocks.signIn).toHaveBeenCalledWith({
      email: "t@example.com",
      password: "pw",
    }));
    await waitFor(() => expect(fetchMock).toHaveBeenCalled());
    await waitFor(() =>
      expect(mocks.router.replace).toHaveBeenCalledWith("/teacher")
    );
    expect(mocks.router.refresh).toHaveBeenCalled();
  });

  it("redirects a student to /student", async () => {
    mocks.signIn.mockResolvedValue({
      data: { session: { access_token: "tok" } },
      error: null,
    });
    mockMeResponse(true, { role: "student" });

    render(<LoginPage />);
    await submitLogin("s@example.com", "pw");

    await waitFor(() =>
      expect(mocks.router.replace).toHaveBeenCalledWith("/student")
    );
  });

  it("shows the supabase error and does not redirect when sign-in fails", async () => {
    mocks.signIn.mockResolvedValue({
      data: { session: null },
      error: { message: "Invalid login credentials" },
    });
    const fetchMock = vi.fn();
    vi.stubGlobal("fetch", fetchMock);

    render(<LoginPage />);
    await submitLogin("x@example.com", "wrong");

    expect(await screen.findByText("Invalid login credentials")).toBeInTheDocument();
    expect(fetchMock).not.toHaveBeenCalled();
    expect(mocks.router.replace).not.toHaveBeenCalled();
  });

  it("shows the profile error when /api/auth/me fails", async () => {
    mocks.signIn.mockResolvedValue({
      data: { session: { access_token: "tok" } },
      error: null,
    });
    mockMeResponse(false, {}, "Profile not found");

    render(<LoginPage />);
    await submitLogin("t@example.com", "pw");

    expect(await screen.findByText("Profile not found")).toBeInTheDocument();
    expect(mocks.router.replace).not.toHaveBeenCalled();
    expect(mocks.signOut).not.toHaveBeenCalled();
  });

  it("signs out when /api/auth/me returns 401", async () => {
    mocks.signIn.mockResolvedValue({
      data: { session: { access_token: "tok" } },
      error: null,
    });
    mockMeResponse(false, {}, "Invalid token", 401);

    render(<LoginPage />);
    await submitLogin("t@example.com", "pw");

    expect(await screen.findByText("Invalid token")).toBeInTheDocument();
    await waitFor(() => expect(mocks.signOut).toHaveBeenCalledTimes(1));
  });
});
