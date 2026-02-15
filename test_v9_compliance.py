import requests
import json

URL = "https://rdp-three-ruby.vercel.app/api/v1/chat"
API_KEY = "o-RDToE1mPtDwGUPjsQ_HT12BrB5VLRjlT6dgqz_s6Q"

sample_request = {
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

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

print(f"Sending request to {URL}...")
response = requests.post(URL, headers=headers, json=sample_request)

print(f"Status Code: {response.status_code}")
print("Response JSON:")
print(json.dumps(response.json(), indent=4))

# Check if it matches exactly: {"status": "success", "reply": "..."}
resp_data = response.json()
if "status" in resp_data and "reply" in resp_data and len(resp_data.keys()) == 2:
    print("\nSUCCESS: Response format matches the evaluation requirements perfectly!")
else:
    print("\nFAILURE: Response format does not match expectations.")
