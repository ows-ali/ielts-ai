import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";

import type { Session } from "@supabase/supabase-js";

import { JoinRoomForm } from "@/components/student/join-room-form";
import { ApiError } from "@/lib/api";
import type { Room } from "@/lib/types";

const mockRouter = { push: vi.fn(), replace: vi.fn(), refresh: vi.fn() };
vi.mock("next/navigation", () => ({
  useRouter: () => mockRouter,
}));

const mockSignOut = vi.fn();
vi.mock("@/lib/supabase/client", () => ({
  createClient: () => ({ auth: { signOut: mockSignOut } }),
}));

const mockJoinRoom = vi.fn();
vi.mock("@/lib/api", () => ({
  ApiError: class ApiError extends Error {
    status: number;
    constructor(status: number, message: string) {
      super(message);
      this.status = status;
    }
  },
  api: { joinRoom: (...args: unknown[]) => mockJoinRoom(...args) },
}));

const session = { access_token: "token-123" } as Session;

describe("JoinRoomForm", () => {
  beforeEach(() => {
    mockRouter.push.mockReset();
    mockRouter.replace.mockReset();
    mockRouter.refresh.mockReset();
    mockSignOut.mockReset();
    mockJoinRoom.mockReset();
  });

  it("renders a code input and submit button", () => {
    render(<JoinRoomForm session={session} />);
    expect(screen.getByLabelText("Room code")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Join room" })).toBeInTheDocument();
  });

  it("uppercases the room code as the user types", async () => {
    const user = userEvent.setup();
    render(<JoinRoomForm session={session} />);
    const input = screen.getByLabelText("Room code");
    await user.type(input, "ielst");
    expect(input).toHaveValue("IELST");
  });

  it("joins the room and redirects to the student room page", async () => {
    const user = userEvent.setup();
    mockJoinRoom.mockResolvedValue({ id: "room-9" } as Room);
    render(<JoinRoomForm session={session} />);

    await user.type(screen.getByLabelText("Room code"), "ABCD1234");
    await user.click(screen.getByRole("button", { name: "Join room" }));

    await waitFor(() =>
      expect(mockJoinRoom).toHaveBeenCalledWith(session, "ABCD1234")
    );
    await waitFor(() => expect(mockRouter.push).toHaveBeenCalledWith("/student/room/room-9"));
  });

  it("surfaces an error when joining fails", async () => {
    const user = userEvent.setup();
    mockJoinRoom.mockRejectedValue(new Error("Room code not found"));
    render(<JoinRoomForm session={session} />);

    await user.type(screen.getByLabelText("Room code"), "NOPE1234");
    await user.click(screen.getByRole("button", { name: "Join room" }));

    expect(await screen.findByText("Room code not found")).toBeInTheDocument();
    expect(mockRouter.push).not.toHaveBeenCalled();
    expect(mockSignOut).not.toHaveBeenCalled();
  });

  it("signs out and redirects to /login on a 401", async () => {
    const user = userEvent.setup();
    mockJoinRoom.mockRejectedValue(new ApiError(401, "Invalid token"));
    render(<JoinRoomForm session={session} />);

    await user.type(screen.getByLabelText("Room code"), "ABCD1234");
    await user.click(screen.getByRole("button", { name: "Join room" }));

    await waitFor(() => expect(mockSignOut).toHaveBeenCalledTimes(1));
    await waitFor(() => expect(mockRouter.replace).toHaveBeenCalledWith("/login"));
    expect(mockRouter.refresh).toHaveBeenCalled();
  });
});
