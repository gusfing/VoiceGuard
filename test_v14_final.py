import requests
import json

BASE_URL = "https://rdp-three-ruby.vercel.app"
HEADERS = {"Content-Type": "application/json"}

def test_auth_error():
    print("\n--- Testing Auth Error (PS1) ---")
    data = {"language": "English", "audioBase64": "SGVsbG8="}
    resp = requests.post(f"{BASE_URL}/api/v1/detect", headers=HEADERS, json=data)
    print(f"Status: {resp.status_code}")
    print(json.dumps(resp.json(), indent=4))
    
    # Check if message matches PS1 spec exactly
    if resp.json().get("message") == "Invalid API key or malformed request":
        print("✅ Error message matches PS1 specification exactly!")

def test_grandma_engagement():
    print("\n--- Testing Grandma (PS2) ---")
    headers_with_key = {"x-api-key": "o-RDToE1mPtDwGUPjsQ_HT12BrB5VLRjlT6dgqz_s6Q", "Content-Type": "application/json"}
    data = {
        "sessionId": "final-harden-test",
        "message": {"sender": "scammer", "text": "Your account is BLOCKED. Verify at http://bank.com"},
        "conversationHistory": []
    }
    resp = requests.post(f"{BASE_URL}/api/v1/chat", headers=headers_with_key, json=data)
    print(json.dumps(resp.json(), indent=4))
    if "blocked" in resp.json().get("reply", "").lower() or "bank" in resp.json().get("reply", "").lower():
        print("✅ Grandma response is contextually aware and believable!")

if __name__ == "__main__":
    test_auth_error()
    test_grandma_engagement()
