import json
import httpx
from app.core.config import settings


async def transcribe_audio_groq(audio_bytes: bytes, mime_type: str = "audio/webm") -> str:
    """Transcribe audio using Groq Cloud Whisper API (whisper-large-v3-turbo)."""
    if not settings.groq_api_key:
        raise ValueError("GROQ_API_KEY is not configured")

    url = "https://api.groq.com/openai/v1/audio/transcriptions"
    headers = {"Authorization": f"Bearer {settings.groq_api_key}"}

    ext = "webm"
    if "mp4" in mime_type or "m4a" in mime_type:
        ext = "m4a"
    elif "wav" in mime_type:
        ext = "wav"
    elif "ogg" in mime_type:
        ext = "ogg"

    files = {"file": (f"audio.{ext}", audio_bytes, mime_type)}
    data = {"model": "whisper-large-v3-turbo"}

    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(url, headers=headers, files=files, data=data)
        if resp.status_code != 200:
            raise ValueError(f"Groq Whisper API error {resp.status_code}: {resp.text[:500]}")
        res_json = resp.json()
        return res_json.get("text", "").strip()


async def evaluate_answer_groq(
    transcript: str,
    criteria: str,
    part: int,
    question: str,
    history: str = "",
) -> dict:
    """Evaluate speaking answer using Groq Llama-3 model."""
    if not settings.groq_api_key:
        raise ValueError("GROQ_API_KEY is not configured")

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.groq_api_key}",
        "Content-Type": "application/json",
    }

    system = (
        "You are an expert IELTS Speaking examiner. Score strictly against official IELTS Band Descriptors. "
        "Return ONLY valid JSON with this exact shape: "
        '{"fluency": float, "grammar": float, "vocabulary": float, "pronunciation": float, "overall": float, "feedback": ["concise actionable tips"]}'
    )
    user = (
        f"IELTS Speaking Part {part}.\nQuestion: {question}\n\n"
        f"Student transcript:\n{transcript}\n\n"
        f"Band Descriptors:\n{criteria}\n"
    )
    if history:
        user += f"\nTarget weaknesses:\n{history}\n"

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.3,
    }

    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.post(url, headers=headers, json=payload)
        if resp.status_code != 200:
            raise ValueError(f"Groq Evaluation API error {resp.status_code}: {resp.text[:500]}")
        content = resp.json()["choices"][0]["message"]["content"]
        return json.loads(content)
