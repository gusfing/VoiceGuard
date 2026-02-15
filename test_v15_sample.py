import requests
import json

URL = "https://rdp-three-ruby.vercel.app/api/v1/chat"
API_KEY = "o-RDToE1mPtDwGUPjsQ_HT12BrB5VLRjlT6dgqz_s6Q"
HEADERS = {"x-api-key": API_KEY, "Content-Type": "application/json"}

sample_payload = {
    "sessionId": "1fc994e9-f4c5-47ee-8806-90aeb969928f",
    "message": {
        "sender": "scammer",
        "text": "Your bank account will be blocked today. Verify immediately.",
        "timestamp": 1769776085000
    },
    "conversationHistory": [],
    "metadata": {
        "channel": "SMS",
        "language": "English",
        "locale": "IN"
    }
}

print(f"Testing PS2 (HoneyPot) with EXACT sample payload at {URL}...")
response = requests.post(URL, headers=HEADERS, json=sample_payload)

print(f"Status Code: {response.status_code}")
print("Response JSON:")
print(json.dumps(response.json(), indent=4))

# Verification
resp_data = response.json()
if resp_data.get("status") == "success" and resp_data.get("reply") == "Why is my account being suspended?":
    print("\n✅ MATCH SUCCESS: Response perfectly matches the provided sample!")
else:
    print("\n❌ MATCH FAILURE: Response did not match the sample reply exactly.")
