from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "VoiceGuard API"
    API_V1_STR: str = "/api/v1"
    
    # Custom API Key
    API_KEY: str = "hackathon_master_key_123"

    class Config:
        case_sensitive = True

settings = Settings()
