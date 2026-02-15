import requests
import json

# Production URL
url = "https://rdp-three-ruby.vercel.app/api/v1/chat"

# Correct API Key
headers = {
    "x-api-key": "o-RDToE1mPtDwGUPjsQ_HT12BrB5VLRjlT6dgqz_s6Q",
    "Content-Type": "application/json"
}

# Payload
payload = {
    "content": "Hello Scam",
    "sessionId": "prod_test"
}

print(f"Testing URL: {url}")
try:
    response = requests.post(url, headers=headers, json=payload)
    print(f"Status Code: {response.status_code}")
    print("Response Body:")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
