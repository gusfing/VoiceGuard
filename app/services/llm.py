from typing import List, Dict, Any
import random
import time

class LLMService:
    def __init__(self):
        pass

    async def generate_response(self, prompt: str, history: List[Dict[str, str]] = None) -> str:
        # Mock responses for Honeypot
        if "Analyze" in prompt:
             return '{"is_scam": true}'
        
        # Persona responses
        responses = [
            "I'm sorry, I don't understand tech very well. Can you explain?",
            "Hold on, let me find my glasses.",
            "Is there a fee I need to pay?",
            "My grandson usually helps me with this.",
            "What is a URL? Is that like a phone number?"
        ]
        return random.choice(responses)

    async def extract_info(self, text: str) -> Dict[str, Any]:
        return {}

llm_service = LLMService()
