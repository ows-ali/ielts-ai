import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";

import type { Session } from "@supabase/supabase-js";

import { CreateRoomForm } from "@/components/teacher/create-room-form";
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

const mockCreateRoom = vi.fn();
vi.mock("@/lib/api", () => ({
  ApiError: class ApiError extends Error {
    status: number;
    constructor(status: number, message: string) {
      super(message);
      this.status = status;
    }
  },
  api: { createRoom: (...args: unknown[]) => mockCreateRoom(...args) },
}));

const session = { access_token: "token-123" } as Session;

describe("CreateRoomForm", () => {
  beforeEach(() => {
    mockRouter.push.mockReset();
    mockRouter.replace.mockReset();
    mockRouter.refresh.mockReset();
    mockSignOut.mockReset();
    mockCreateRoom.mockReset();
  });

  it("creates a room with a default title and redirects", async () => {
    const user = userEvent.setup();
    mockCreateRoom.mockResolvedValue({ id: "room-1" } as Room);
    render(<CreateRoomForm session={session} />);

    await user.click(screen.getByRole("button", { name: "Create room" }));

    await waitFor(() =>
      expect(mockCreateRoom).toHaveBeenCalledWith(session, "Speaking Practice", 1)
    );
    await waitFor(() => expect(mockRouter.push).toHaveBeenCalledWith("/teacher/rooms/room-1"));
  });

  it("uses the typed title and selected part", async () => {
    const user = userEvent.setup();
    mockCreateRoom.mockResolvedValue({ id: "room-2" } as Room);
    render(<CreateRoomForm session={session} />);

    await user.type(screen.getByLabelText("Room title"), "Mock exam");
    await user.selectOptions(screen.getByLabelText("IELTS Speaking Part"), "3");
    await user.click(screen.getByRole("button", { name: "Create room" }));

    await waitFor(() =>
      expect(mockCreateRoom).toHaveBeenCalledWith(session, "Mock exam", 3)
    );
  });

  it("surfaces an error when creating fails", async () => {
    const user = userEvent.setup();
    mockCreateRoom.mockRejectedValue(new Error("Already live"));
    render(<CreateRoomForm session={session} />);

    await user.click(screen.getByRole("button", { name: "Create room" }));

    expect(await screen.findByText("Already live")).toBeInTheDocument();
    expect(mockRouter.push).not.toHaveBeenCalled();
    expect(mockSignOut).not.toHaveBeenCalled();
  });

  it("signs out and redirects to /login on a 401", async () => {
    const user = userEvent.setup();
    mockCreateRoom.mockRejectedValue(new ApiError(401, "Invalid token"));
    render(<CreateRoomForm session={session} />);

    await user.click(screen.getByRole("button", { name: "Create room" }));

    await waitFor(() => expect(mockSignOut).toHaveBeenCalledTimes(1));
    await waitFor(() => expect(mockRouter.replace).toHaveBeenCalledWith("/login"));
    expect(mockRouter.refresh).toHaveBeenCalled();
  });
});
