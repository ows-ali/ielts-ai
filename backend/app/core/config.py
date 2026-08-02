from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    supabase_url: str = ""
    supabase_service_role_key: str = ""
    supabase_jwt_secret: str = ""
    supabase_anon_key: str = ""

    gemini_api_key: str = ""
    gemini_eval_model: str = "gemini-2.5-pro"
    gemini_stt_model: str = "gemini-2.5-flash"

    environment: str = "development"
    cors_origins: str = "http://localhost:3000"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
