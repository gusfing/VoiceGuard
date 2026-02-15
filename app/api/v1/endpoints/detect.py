from fastapi import APIRouter, Header, HTTPException, Depends, Body
from pydantic import BaseModel, Field
from typing import Optional
from app.services.inference import inference_service
from app.core.config import settings
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

# Request Model matching strict specs
class DetectRequest(BaseModel):
    language: str = Field(..., description="Language of the audio (e.g., 'English')")
    audioFormat: str = Field(..., description="Format of audio file (will be 'mp3')")
    audioBase64: str = Field(..., description="Base64-encoded audio file content")

# Response Model matching strict specs
class DetectResponse(BaseModel):
    status: str
    classification: str
    confidenceScore: float

async def verify_api_key(x_api_key: str = Header(...)):
    # Validate API Key against config
    if settings.API_KEY and x_api_key != settings.API_KEY:
         logger.warning(f"Invalid API Key attempt: {x_api_key}")
         raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

@router.post("/detect", response_model=DetectResponse)
async def detect_voice(
    request: DetectRequest,
    x_api_key: str = Depends(verify_api_key)
):
    """
    Detects if the voice is AI_GENERATED or HUMAN.
    """
    try:
        # Pass data to inference service
        result = await inference_service.predict(
            audio_data_base64=request.audioBase64,
            language=request.language
        )
        
        return DetectResponse(
            status="success",
            classification=result["classification"],
            confidenceScore=result["confidence_score"]
        )
        
    except ValueError as ve:
        logger.error(f"Validation error: {ve}")
        # Return 400 for bad input (implied by ValueError in inference)
        raise HTTPException(status_code=400, detail=str(ve))
        
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        # Return 500 for internal errors
        raise HTTPException(status_code=500, detail="Internal processing error")
