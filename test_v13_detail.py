import requests
import json

BASE_URL = "https://rdp-three-ruby.vercel.app"
API_KEY = "o-RDToE1mPtDwGUPjsQ_HT12BrB5VLRjlT6dgqz_s6Q"
HEADERS = {"x-api-key": API_KEY, "Content-Type": "application/json"}

def test_ps1_detailed():
    print("\n--- Testing PS1 (Detailed Explanation) ---")
    data = {
        "language": "Tamil",
        "audioFormat": "mp3",
        "audioBase64": "SGVsbG8="
    }
    resp = requests.post(f"{BASE_URL}/api/v1/detect", headers=HEADERS, json=data)
    print(json.dumps(resp.json(), indent=4))

def test_ps2_contextual():
    print("\n--- Testing PS2 (Contextual OTP Reply) ---")
    data = {
        "sessionId": "detailed-test-sess",
        "message": {"sender": "scammer", "text": "Send me the OTP code now!"},
        "conversationHistory": [
            {"sender": "scammer", "text": "Your account is blocked"},
            {"sender": "user", "text": "Oh no why?"}
        ]
    }
    resp = requests.post(f"{BASE_URL}/api/v1/chat", headers=HEADERS, json=data)
    print(json.dumps(resp.json(), indent=4))

if __name__ == "__main__":
    test_ps1_detailed()
    test_ps2_contextual()
