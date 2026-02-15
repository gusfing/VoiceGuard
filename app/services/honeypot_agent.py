from typing import List, Dict
from app.services.llm import llm_service

class HoneyPotAgent:
    def __init__(self):
        pass

    async def generate_reply(self, message: str, history: List[Dict[str, str]]) -> str:
        return await llm_service.generate_response(message, history)

honeypot_agent = HoneyPotAgent()
