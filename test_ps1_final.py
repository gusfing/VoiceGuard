import requests
import json

URL = "https://rdp-three-ruby.vercel.app/api/voice-detection"
API_KEY = "o-RDToE1mPtDwGUPjsQ_HT12BrB5VLRjlT6dgqz_s6Q"

sample_request = {
    "language": "Tamil",
    "audioFormat": "mp3",
    "audioBase64": "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU2LjM2LjEwMAAAAAAA..."
}

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

print(f"Testing PS1 (Voice Detection) at {URL}...")
response = requests.post(URL, headers=headers, json=sample_request)

print(f"Status Code: {response.status_code}")
print("Response JSON:")
print(json.dumps(response.json(), indent=4))

# Verification
resp_data = response.json()
required_fields = ["status", "language", "classification", "confidenceScore", "explanation"]
missing = [f for f in required_fields if f not in resp_data]

if not missing and resp_data.get("status") == "success":
    print("\nSUCCESS: PS1 (Voice Detection) is 100% compliant!")
else:
    print(f"\nFAILURE: PS1 is missing fields: {missing}")
