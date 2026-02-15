from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.api.v1.endpoints import detect, chat
from app.core.config import settings
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup Rate Limiter
from app.core.rate_limiter import limiter

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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
app.include_router(chat.router, prefix=f"{settings.API_V1_STR}", tags=["honeypot"])

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>VoiceGuard - AI Detection API</title>
            <style>
                body { font-family: 'Inter', sans-serif; background: #0f172a; color: #e2e8f0; text-align: center; padding: 50px; }
                h1 { color: #38bdf8; font-size: 3rem; margin-bottom: 10px; }
                p { font-size: 1.2rem; color: #94a3b8; }
                .card { background: #1e293b; padding: 20px; border-radius: 12px; display: inline-block; margin-top: 30px; border: 1px solid #334155; }
                code { background: #000; padding: 5px 10px; border-radius: 5px; color: #22c55e; }
                a { color: #38bdf8; text-decoration: none; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>🛡️ VoiceGuard API</h1>
            <p>Advanced AI Voice Detection & Authenticity Analysis</p>
            
            <div class="card">
                <p>Status: <span style="color: #22c55e;">● Online</span> | Ver: <strong>1.0.0</strong></p>
                <p><strong>Use the API:</strong></p>
                <p><code>POST /api/v1/detect</code></p>
            </div>
            
            <br><br>
            <p>View Documentation: <a href="/docs">Swagger UI</a></p>
            <p style="font-size: 0.9rem; margin-top: 50px; opacity: 0.6;">Built for Impact AI Hackathon 2026</a></p>
        </body>
    </html>
    """
