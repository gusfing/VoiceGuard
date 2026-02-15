from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import detect
from app.core.config import settings
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Debug: Print loaded API Key
print(f"DEBUG: Loaded API Key from settings: '{settings.API_KEY}'")

# CORS - Allow all for hackathon
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global Error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "Internal Server Error",
            "details": str(exc) # Include details for debugging
        }
    )

app.include_router(detect.router, prefix=f"{settings.API_V1_STR}", tags=["detection"])
from app.api.v1.endpoints import chat
app.include_router(chat.router, prefix=f"{settings.API_V1_STR}", tags=["honeypot"])

@app.get("/")
def root():
    return {"message": "VoiceGuard API is running"}
