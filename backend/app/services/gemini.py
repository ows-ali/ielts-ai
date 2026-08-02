import base64
import json
from typing import Any

import httpx

from app.core.config import settings


def _api_url(model: str, method: str = "generateContent") -> str:
    return (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:{method}?key={settings.gemini_api_key}"
    )


async def transcribe_audio(audio_bytes: bytes, mime_type: str) -> str:
    """Transcribe audio using the Gemini Flash model."""
    url = _api_url(settings.gemini_stt_model)
    inline_data = {
        "mime_type": mime_type,
        "data": base64.b64encode(audio_bytes).decode("ascii"),
    }
    body: dict[str, Any] = {
        "contents": [
            {
                "parts": [
                    {
                        "text": (
                            "Transcribe the following speech verbatim. "
                            "Return only the transcript, no commentary."
                        )
                    },
                    {"inline_data": inline_data},
                ]
            }
        ]
    }
    return await _generate_text(url, body)


async def evaluate_answer(
    transcript: str,
    criteria: str,
    part: int,
    question: str,
    history: str = "",
) -> dict:
    """Score a speaking answer using the Gemini Pro model."""
    url = _api_url(settings.gemini_eval_model)
    system = (
        "You are an expert IELTS Speaking examiner. Score strictly against the "
        "official IELTS Band Descriptors. Return ONLY valid JSON with this exact "
        "shape: {\"fluency\": float, \"grammar\": float, \"vocabulary\": float, "
        "\"pronunciation\": float, \"overall\": float, "
        "\"feedback\": [\"concise actionable tips\"]}. "
        "Scores are bands 0-9 (halves allowed). Do not round the overall up."
    )
    user = (
        f"IELTS Speaking Part {part}.\n"
        f"Question: {question}\n\n"
        f"Student transcript:\n{transcript}\n\n"
        f"Relevant IELTS Band Descriptors:\n{criteria}\n"
    )
    if history:
        user += f"\nStudent's previous weaknesses to target:\n{history}\n"

    body = {
        "system_instruction": {"parts": [{"text": system}]},
        "contents": [{"parts": [{"text": user}]}],
        "generationConfig": {
            "temperature": 0.4,
            "responseMimeType": "application/json",
        },
    }
    text = await _generate_text(url, body)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        raise ValueError(f"Gemini returned invalid JSON for evaluation: {text[:500]}")


async def summarize_class_problems(evaluations: list[dict]) -> list[str]:
    """Aggregate common weaknesses across a class."""
    if not evaluations:
        return []
    url = _api_url(settings.gemini_eval_model)
    joined = json.dumps(evaluations, ensure_ascii=False)
    body = {
        "contents": [
            {
                "parts": [
                    {
                        "text": (
                            "Here are the IELTS evaluations of several students. "
                            "Return a JSON list of up to 4 common problems across "
                            "the class, phrased as short actionable items. "
                            "Return ONLY valid JSON: [\"problem\", ...]\n\n"
                            f"{joined}"
                        )
                    }
                ]
            }
        ],
        "generationConfig": {"temperature": 0.3, "responseMimeType": "application/json"},
    }
    text = await _generate_text(url, body)
    try:
        data = json.loads(text)
        return data if isinstance(data, list) else [str(data)]
    except json.JSONDecodeError:
        return []


async def _generate_text(url: str, body: dict) -> str:
    import asyncio
    max_retries = 3
    for attempt in range(max_retries):
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(url, json=body)
            if resp.status_code == 429:
                if settings.groq_api_key:
                    raise ValueError(f"Gemini API rate limit 429: {resp.text[:300]}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(4 * (attempt + 1))
                    continue
            if resp.status_code != 200:
                raise ValueError(f"Gemini API error {resp.status_code}: {resp.text[:500]}")
            data = resp.json()
            try:
                return data["candidates"][0]["content"]["parts"][0]["text"].strip()
            except (KeyError, IndexError):
                raise ValueError(f"Unexpected Gemini response: {data}")
