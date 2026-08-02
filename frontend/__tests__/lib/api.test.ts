import { beforeEach, describe, expect, it, vi } from "vitest";

import type { Session } from "@supabase/supabase-js";

import { api, ApiError } from "@/lib/api";

const session = {
  access_token: "token-123",
} as Session;

function mockFetchOnce(status: number, body: unknown) {
  const fn = vi.fn().mockResolvedValue({
    ok: status >= 200 && status < 300,
    status,
    statusText: "status text",
    json: async () => body,
  });
  vi.stubGlobal("fetch", fn);
  return fn;
}

describe("api request", () => {
  beforeEach(() => {
    delete process.env.NEXT_PUBLIC_API_URL;
  });

  it("attaches the bearer token when a session is present", async () => {
    const fetchMock = mockFetchOnce(200, { id: "u1" });
    await api.me(session);
    const [, init] = fetchMock.mock.calls[0] as [string, RequestInit];
    expect(init.headers).toMatchObject({
      Authorization: "Bearer token-123",
      "Content-Type": "application/json",
    });
  });

  it("omits the Authorization header without a session", async () => {
    const fetchMock = mockFetchOnce(200, { id: "u1" });
    await api.me(null);
    const [, init] = fetchMock.mock.calls[0] as [string, RequestInit];
    expect(init.headers).not.toHaveProperty("Authorization");
  });

  it("uses NEXT_PUBLIC_API_URL as the base", async () => {
    vi.stubEnv("NEXT_PUBLIC_API_URL", "https://api.example.com");
    vi.resetModules();
    const freshApi = (await import("@/lib/api")).api;
    const fetchMock = mockFetchOnce(200, { id: "u1" });
    await freshApi.me(null);
    expect(fetchMock.mock.calls[0][0]).toBe("https://api.example.com/api/auth/me");
  });

  it("throws ApiError with the backend detail on failure", async () => {
    mockFetchOnce(404, { detail: "Room not found" });
    const err = (await api.getRoom(null, "r1").catch((e) => e)) as ApiError;
    expect(err).toBeInstanceOf(ApiError);
    expect(err.status).toBe(404);
    expect(err.message).toBe("Room not found");
  });

  it("throws ApiError with statusText when the body has no detail", async () => {
    mockFetchOnce(500, {});
    const err = (await api.me(null).catch((e) => e)) as ApiError;
    expect(err).toBeInstanceOf(ApiError);
    expect(err.status).toBe(500);
    expect(err.message).toBe("status text");
  });

  it("builds the right paths, methods and bodies", async () => {
    const fetchMock = vi.fn().mockImplementation(async (url: string, init?: RequestInit) => ({
      ok: true,
      status: 200,
      json: async () => (init?.method === "GET" ? [] : {}),
    }));
    vi.stubGlobal("fetch", fetchMock);

    await api.me(session);
    await api.listRooms(session);
    await api.createRoom(session, "Room A", 2);
    await api.joinRoom(session, "ABCD1234");
    await api.participants(session, "r1");
    await api.startRoom(session, "r1");
    await api.endRoom(session, "r1");
    await api.submitAnswer(session, "r1", "q1", "https://x/y.wav", "hello");

    const calls = fetchMock.mock.calls.map((c) => ({
      url: c[0],
      method: (c[1] as RequestInit).method ?? "GET",
      body: (c[1] as RequestInit).body ? JSON.parse((c[1] as RequestInit).body as string) : undefined,
    }));

    expect(calls[0]).toMatchObject({ url: "http://localhost:8000/api/auth/me", method: "GET" });
    expect(calls[1]).toMatchObject({ url: "http://localhost:8000/api/rooms", method: "GET" });
    expect(calls[2]).toMatchObject({
      url: "http://localhost:8000/api/rooms",
      method: "POST",
      body: { title: "Room A", part: 2 },
    });
    expect(calls[3]).toMatchObject({
      url: "http://localhost:8000/api/rooms/join",
      method: "POST",
      body: { room_code: "ABCD1234" },
    });
    expect(calls[4]).toMatchObject({
      url: "http://localhost:8000/api/rooms/r1/participants",
      method: "GET",
    });
    expect(calls[5]).toMatchObject({
      url: "http://localhost:8000/api/rooms/r1/start",
      method: "POST",
    });
    expect(calls[6]).toMatchObject({
      url: "http://localhost:8000/api/rooms/r1/end",
      method: "POST",
    });
    expect(calls[7]).toMatchObject({
      url: "http://localhost:8000/api/rooms/r1/answers",
      method: "POST",
      body: {
        room_id: "r1",
        question_id: "q1",
        audio_url: "https://x/y.wav",
        transcript: "hello",
      },
    });
  });

  it("getQuestion resolves to the question payload", async () => {
    mockFetchOnce(200, {
      question: { id: "q1", part: 1, question: "Hi" },
    });
    await expect(api.getQuestion(null, "r1")).resolves.toMatchObject({
      id: "q1",
      question: "Hi",
    });
  });

  it("exposes ApiError as an Error subclass", () => {
    const err = new ApiError(400, "bad");
    expect(err).toBeInstanceOf(Error);
    expect(err.status).toBe(400);
  });
});
