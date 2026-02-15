import re
from typing import List, Dict

class IntelligenceExtractor:
    def __init__(self):
        pass

    def extract(self, text: str) -> Dict:
        data = {
            "bank_account_numbers": [],
            "upi_ids": [],
            "phishing_links": [],
            "phone_numbers": [],
            "other_info": {}
        }
        
        # Regex for URLs
        url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
        data["phishing_links"] = re.findall(url_pattern, text)
        
        # Regex for generic 10-12 digit numbers (potential bank accounts)
        account_pattern = r'\b\d{10,12}\b'
        data["bank_account_numbers"] = re.findall(account_pattern, text)
        
        # Regex for UPI
        upi_pattern = r'[\w\.-]+@[\w\.-]+'
        possible_upis = re.findall(upi_pattern, text)
        data["upi_ids"] = [u for u in possible_upis if ".com" not in u] 
        
        return data

intelligence_extractor = IntelligenceExtractor()
