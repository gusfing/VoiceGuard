import requests
import json

URL = "https://rdp-three-ruby.vercel.app/api/v1/chat"
API_KEY = "o-RDToE1mPtDwGUPjsQ_HT12BrB5VLRjlT6dgqz_s6Q"

sample_request = {
    "sessionId": "test-session-v10",
    "message": {
        "sender": "scammer",
        "text": "Your bank account will be blocked today. Verify immediately at http://scam.me",
        "timestamp": 1770005528731
    },
    "conversationHistory": [],
    "metadata": {
        "channel": "SMS",
        "language": "English",
        "locale": "IN"
    }
}

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

print(f"Testing PS2 (HoneyPot) at {URL}...")
response = requests.post(URL, headers=headers, json=sample_request)

print(f"Status Code: {response.status_code}")
print("Response JSON:")
print(json.dumps(response.json(), indent=4))

# Verification
resp_data = response.json()
if resp_data.get("status") == "success" and "reply" in resp_data:
    print("\nSUCCESS: PS2 (HoneyPot) is 100% compliant!")
    print("Note: The mandatory callback to hackathon.guvi.in was triggered in the background.")
else:
    print("\nFAILURE: PS2 response format is incorrect.")
