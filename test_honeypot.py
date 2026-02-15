import requests
import json
import time

BASE_URL = "http://127.0.0.1:8000/api/v1/chat"
API_KEY = "your_secret_api_key"
HEADERS = {"x-api-key": API_KEY, "Content-Type": "application/json"}

def send_message(session_id, message):
    payload = {
        "session_id": session_id,
        "message": message
    }
    try:
        response = requests.post(BASE_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        if response:
            print(response.text)
        return None

def test_flow():
    session_id = "test_session_123"
    
    print("--- Starting Test Conversation ---")
    
    # Turn 1: Initial contact (Ambiguous)
    msg1 = "Hello, are you there?"
    print(f"\nScammer: {msg1}")
    res1 = send_message(session_id, msg1)
    if res1:
        print(f"API: Action={res1['action_taken']}, ScamDetected={res1['scam_detected']}")
        print(f"Agent Reply: {res1['reply_message']}")

    # Turn 2: Scam Attempt
    msg2 = "I am calling from the IRS. You have a refund of $5000 pending. Please verify your bank account."
    print(f"\nScammer: {msg2}")
    res2 = send_message(session_id, msg2)
    if res2:
        print(f"API: Action={res2['action_taken']}, ScamDetected={res2['scam_detected']}")
        print(f"Agent Reply: {res2['reply_message']}")
        
    # Turn 3: Extraction Attempt
    msg3 = "Great, please send the money to account 1234567890 at bank.com."
    print(f"\nScammer: {msg3}")
    res3 = send_message(session_id, msg3)
    if res3:
        print(f"API: Action={res3['action_taken']}, ScamDetected={res3['scam_detected']}")
        print(f"Agent Reply: {res3['reply_message']}")
        print(f"Intelligence Extracted: {res3['extracted_intelligence']}")

if __name__ == "__main__":
    test_flow()
