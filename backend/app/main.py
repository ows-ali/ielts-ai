from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth, reports, rooms, speaking
from app.core.config import settings

app = FastAPI(title="IELTS AI Speaking Classroom API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.cors_origins.split(",") if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(rooms.router)
app.include_router(speaking.router)
app.include_router(reports.router)


@app.get("/api/health")
async def health() -> dict:
    return {"status": "ok"}
