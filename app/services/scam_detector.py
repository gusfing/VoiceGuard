import json
from app.services.llm import llm_service

class ScamDetector:
    def __init__(self):
        pass

    async def detect(self, message: str) -> dict:
        """
        Analyzes the message for scam intent.
        Returns a dict with 'is_scam' (bool) and 'confidence' (float).
        """
        # Simple heuristic fallback for now
        scam_keywords = ["refund", "bank", "irs", "urgency", "verify", "password", "otp", "winner", "lottery"]
        is_scam_heuristic = any(keyword in message.lower() for keyword in scam_keywords)
        
        if is_scam_heuristic:
                return {
                "is_scam": True,
                "confidence": 0.85,
                "reasoning": "Contains suspicious keywords."
            }
        
        return {
            "is_scam": False,
            "confidence": 0.1,
            "reasoning": "No obvious scam triggers found."
        }
            
scam_detector = ScamDetector()
