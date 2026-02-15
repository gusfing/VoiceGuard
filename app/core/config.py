from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "VoiceGuard API"
    API_V1_STR: str = "/api/v1"
    
    # Load from environment variable, default provided for local dev if needed
    API_KEY: str = "hackathon_master_key_123"

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "ignore"

settings = Settings()
