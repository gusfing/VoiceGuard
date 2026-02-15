from fastapi import APIRouter, Request
import time
import json
import uuid
import random
import re

router = APIRouter()

# Global in-memory storage (reset on cold start)
sessions = {}

@router.api_route("/chat", methods=["GET", "POST"])
@router.api_route("/chat/", methods=["GET", "POST"], include_in_schema=False)
async def chat_endpoint(request: Request):
    """
    BARE METAL SIMULATION ENDPOINT (V5.4)
    No external dependencies. No config. No crash.
    """
    
    # 1. ROBUST INPUT PARSING
    try:
        body_bytes = await request.body()
        body_str = body_bytes.decode()
        
        # Try JSON
        try:
            data = json.loads(body_str)
        except:
            data = {"content": body_str}
            
        # Extract Content
        message_content = None
        for key in ["message", "content", "text", "msg", "input", "query"]:
            if key in data and data[key]:
                message_content = data[key]
                break
        
        if not message_content:
            message_content = "PING"

        session_id = data.get("session_id") or data.get("sessionId") or f"session_{int(time.time())}"

    except Exception:
        message_content = "RECOVERY_MODE"
        session_id = "recovery_session"

    # 2. LIGHTWEIGHT SIMULATION LOGIC
    is_scam = False
    action = "monitoring"
    confidence = 0.1
    reply_message = "I'm sorry, you have the wrong number."
    extracted = {}
    
    try:
        msg_lower = str(message_content).lower()
        scam_keywords = ["refund", "bank", "irs", "urgent", "verify", "password", "otp", "winner", "prize"]
        
        is_scam = any(kw in msg_lower for kw in scam_keywords)
        
        if is_scam:
            replies = [
                "Hello? Is this the internet?",
                "I don't have my reading glasses, who is this?",
                "My grandson said I shouldn't give numbers to strangers.",
                "A refund? Oh dear, did I buy something?",
                "Please speak up, it's very quiet here."
            ]
            reply_message = random.choice(replies)
            action = "engage"
            confidence = 0.92
            
        # Extract Phones (Regex)
        phones = re.findall(r'\b\d{10}\b', str(message_content))
        if phones:
            extracted["phone_numbers"] = phones
            
    except:
        pass # Never crash

    # 3. STANDARD JSON RESPONSE
    return {
        "status": "success",
        "data": {
            "session_id": session_id,
            "message_id": str(uuid.uuid4()),
            "scam_detected": is_scam,
            "confidence_score": confidence,
            "action_taken": action,
            "reply_message": reply_message,
            "extracted_intelligence": extracted,
            "metrics": {
                "turns": 1,
                "duration": 0.05
            },
            "is_terminal": False
        },
        "message": "Honeypot Response"
    }
