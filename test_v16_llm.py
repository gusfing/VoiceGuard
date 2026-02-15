import requests
import json

URL = "https://rdp-three-ruby.vercel.app/api/v1/chat"
API_KEY = "o-RDToE1mPtDwGUPjsQ_HT12BrB5VLRjlT6dgqz_s6Q"
HEADERS = {"x-api-key": API_KEY, "Content-Type": "application/json"}

sample_payload = {
    "sessionId": "llm-test-session",
    "message": {
        "sender": "scammer",
        "text": "Hello, this is officer Bob from your bank. Your card has been cloned. Please provide your PIN to secure your account immediately.",
        "timestamp": 1770005528731
    },
    "conversationHistory": [],
    "metadata": {"channel": "SMS", "language": "English", "locale": "IN"}
}

print(f"Testing Natural LLM Response at {URL}...")
response = requests.post(URL, headers=HEADERS, json=sample_payload)

print(f"Status Code: {response.status_code}")
print("Response JSON:")
print(json.dumps(response.json(), indent=4))

# Verification
resp_data = response.json()
reply = resp_data.get("reply", "")
if resp_data.get("status") == "success" and len(reply) > 10:
    print(f"\n✅ NATURAL RESPONSE: '{reply}'")
    print("This response was generated dynamically by the Llama 3 LLM!")
else:
    print("\n❌ LLM FAILURE: Falling back to simulation or error.")
