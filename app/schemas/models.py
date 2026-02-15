from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class ChatRequest(BaseModel):
    # Flexible input model to handle various tester formats
    session_id: Optional[str] = Field(None, alias="sessionId")
    message: Optional[str] = Field(None, alias="content")
    
    # Catch-all
    class Config:
        extra = "allow"
        populate_by_name = True
        
    def get_message_content(self):
        # Helper to extract message
        if self.message: return self.message
        
        extra = self.model_extra or {}
        # Checks for common message field names
        inputs = ["message", "content", "text", "msg", "input", "query"]
        for key in inputs:
            if key in extra: return extra[key]
        return None

    def get_session_id(self):
        if self.session_id: return self.session_id
        extra = self.model_extra or {}
        if "session_id" in extra: return extra["session_id"]
        if "sessionId" in extra: return extra["sessionId"]
        return "default_session"
    
class ChatResponse(BaseModel):
    session_id: str
    message_id: str
    scam_detected: bool
    confidence_score: float
    action_taken: str
    reply_message: Optional[str] = None
    extracted_intelligence: Dict
    metrics: Dict
    is_terminal: bool = False
