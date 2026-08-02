import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";

import type { Session } from "@supabase/supabase-js";

import { TeacherRoomView } from "@/components/teacher/room-view";
import type {
  ClassReport,
  Participant,
  Room,
  TurnState,
} from "@/lib/types";

const mocks = vi.hoisted(() => ({
  ApiError: class ApiError extends Error {
    status: number;
    constructor(status: number, message: string) {
      super(message);
      this.status = status;
    }
  },
  router: { replace: vi.fn(), refresh: vi.fn() },
  api: {
    getRoom: vi.fn(),
    participants: vi.fn(),
    turn: vi.fn(),
    classReport: vi.fn(),
    startRoom: vi.fn(),
    endRoom: vi.fn(),
  },
  channel: {
    on: vi.fn(),
    subscribe: vi.fn(),
  },
  supabase: {
    auth: { signOut: vi.fn() },
    channel: vi.fn(() => mocks.channel),
    removeChannel: vi.fn(),
  },
}));

vi.mock("@/lib/api", () => ({ api: mocks.api, ApiError: mocks.ApiError }));
vi.mock("@/lib/supabase/client", () => ({
  createClient: () => mocks.supabase,
}));
vi.mock("next/navigation", () => ({ useRouter: () => mocks.router }));
vi.mock("@/components/sign-out-button", () => ({
  SignOutButton: () => <button>Sign out</button>,
}));

const session = { access_token: "token-123" } as Session;

const room: Room = {
  id: "r1",
  room_code: "IELTS1234",
  title: "Speaking Practice",
  part: 2,
  teacher_id: "t1",
  status: "waiting",
};

const liveRoom: Room = { ...room, status: "live" };

const endedRoom: Room = { ...room, status: "ended" };

const participants: Participant[] = [
  {
    id: "p1",
    room_id: "r1",
    student_id: "s1",
    student_name: "Alice",
    status: "waiting",
  },
];

const idleTurn: TurnState = {
  room_id: "r1",
  current_student_id: null,
  current_student_name: null,
  question_id: null,
  question: null,
  status: "waiting",
};

const liveTurn: TurnState = {
  ...idleTurn,
  current_student_id: "s1",
  current_student_name: "Alice",
  status: "live",
};

const classReport: ClassReport = {
  room_id: "r1",
  room_code: "IELTS1234",
  participants: [
    { student_id: "s1", student_name: "Alice", status: "completed", band: 7 },
  ],
  average_band: 7,
  common_problems: ["Repetition"],
};

function setUpRoom(statusRoom: Room = room) {
  mocks.api.getRoom.mockResolvedValue(statusRoom);
  mocks.api.participants.mockResolvedValue(participants);
  mocks.api.turn.mockResolvedValue(idleTurn);
  mocks.api.classReport.mockResolvedValue(classReport);
}

describe("TeacherRoomView", () => {
  beforeEach(() => {
    mocks.router.replace.mockReset();
    mocks.router.refresh.mockReset();
    mocks.api.getRoom.mockReset();
    mocks.api.participants.mockReset();
    mocks.api.turn.mockReset();
    mocks.api.classReport.mockReset();
    mocks.api.startRoom.mockReset();
    mocks.api.endRoom.mockReset();
    mocks.supabase.auth.signOut.mockReset();
    mocks.supabase.channel.mockReset().mockImplementation(() => mocks.channel);
    mocks.channel.on.mockReset().mockReturnValue(mocks.channel);
    mocks.channel.subscribe.mockReset().mockReturnValue(mocks.channel);
    mocks.supabase.removeChannel.mockReset();
  });

  it("renders the room header and students", async () => {
    setUpRoom();
    render(<TeacherRoomView session={session} room={room} initialParticipants={participants} />);

    expect(screen.getByText("Speaking Practice")).toBeInTheDocument();
    expect(screen.getByText("IELTS1234")).toBeInTheDocument();
    expect(screen.getByText(/Part 2/)).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "Home" })).toHaveAttribute("href", "/teacher");
    expect(await screen.findByText("Alice")).toBeInTheDocument();
    expect(screen.getByText("Students (1)")).toBeInTheDocument();
  });

  it("shows an empty state when no students have joined", async () => {
    setUpRoom();
    mocks.api.participants.mockResolvedValue([]);
    render(<TeacherRoomView session={session} room={room} initialParticipants={[]} />);

    expect(await screen.findByText("Waiting for students to join...")).toBeInTheDocument();
    expect(screen.getByText("Students (0)")).toBeInTheDocument();
  });

  it("disables start while waiting and with no students, enables otherwise", async () => {
    setUpRoom();
    mocks.api.participants.mockResolvedValue([]);
    render(<TeacherRoomView session={session} room={room} initialParticipants={[]} />);

    expect(await screen.findByRole("button", { name: /Start session/ })).toBeDisabled();
  });

  it("starts the session and refreshes after the API responds", async () => {
    const user = userEvent.setup();
    setUpRoom();
    mocks.api.startRoom.mockResolvedValue(liveTurn);
    render(<TeacherRoomView session={session} room={room} initialParticipants={participants} />);

    const startButton = await screen.findByRole("button", { name: /Start session/ });
    expect(startButton).toBeEnabled();
    await user.click(startButton);

    await waitFor(() => expect(mocks.api.startRoom).toHaveBeenCalledWith(session, "r1"));
    await waitFor(() => expect(mocks.api.getRoom.mock.calls.length).toBe(2));
  });

  it("shows the current speaker during a live turn", async () => {
    setUpRoom();
    mocks.api.turn.mockResolvedValue(liveTurn);
    render(<TeacherRoomView session={session} room={room} initialParticipants={participants} />);

    expect(await screen.findByText(/Now speaking:/)).toBeInTheDocument();
    expect(screen.getAllByText("Alice").length).toBe(2);
  });

  it("shows the class report for an ended room", async () => {
    setUpRoom(endedRoom);
    render(<TeacherRoomView session={session} room={endedRoom} initialParticipants={participants} />);

    expect(await screen.findByText("Average band: 7")).toBeInTheDocument();
    expect(screen.getByText("Band 7")).toBeInTheDocument();
    expect(screen.getByText("Repetition")).toBeInTheDocument();
    expect(mocks.api.classReport).toHaveBeenCalledWith(session, "r1");
  });

  it("ends a live session and shows the report", async () => {
    const user = userEvent.setup();
    setUpRoom(liveRoom);
    mocks.api.endRoom.mockResolvedValue(endedRoom);
    render(<TeacherRoomView session={session} room={liveRoom} initialParticipants={participants} />);

    const endButton = await screen.findByRole("button", { name: "End session" });
    await user.click(endButton);

    await waitFor(() => expect(mocks.api.endRoom).toHaveBeenCalledWith(session, "r1"));
    expect(await screen.findByText("Average band: 7")).toBeInTheDocument();
  });

  it("subscribes to realtime channels and cleans up on unmount", async () => {
    setUpRoom();
    const { unmount } = render(
      <TeacherRoomView session={session} room={room} initialParticipants={participants} />
    );
    await screen.findByText("Alice");

    expect(mocks.supabase.channel).toHaveBeenCalledWith("room-r1");
    expect(mocks.channel.subscribe).toHaveBeenCalledTimes(1);

    unmount();
    expect(mocks.supabase.removeChannel).toHaveBeenCalledWith(mocks.channel);
  });

  it("does not poll with setInterval (realtime only)", async () => {
    const setIntervalSpy = vi.spyOn(window, "setInterval");
    setUpRoom();
    render(<TeacherRoomView session={session} room={room} initialParticipants={participants} />);
    await screen.findByText("Alice");

    const pollTimers = setIntervalSpy.mock.calls
      .map(([, delay]) => delay as number)
      .filter((delay) => delay >= 1000);
    expect(pollTimers).toHaveLength(0);
    setIntervalSpy.mockRestore();
  });

  it("signs out and redirects to /login on a 401", async () => {
    mocks.api.getRoom.mockRejectedValue(new mocks.ApiError(401, "Invalid token"));
    render(<TeacherRoomView session={session} room={room} initialParticipants={participants} />);

    await waitFor(() =>
      expect(mocks.supabase.auth.signOut).toHaveBeenCalledTimes(1)
    );
    await waitFor(() => expect(mocks.router.replace).toHaveBeenCalledWith("/login"));
    expect(mocks.router.refresh).toHaveBeenCalled();
  });
});
