import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/v1/detect"
API_KEY = "o-RDToE1mPtDwGUPjsQ_HT12BrB5VLRjlT6dgqz_s6Q"
HEADERS = {"x-api-key": API_KEY, "Content-Type": "application/json"}

def test_voice_detection():
    payload = {
        "audio_url": "https://example.com/sample_voice.mp3",
        "description": "Test audio file for detection"
    }
    
    print(f"Sending request to {BASE_URL}...")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    
    try:
        response = requests.post(BASE_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        print("\nResponse:")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"Error: {e}")
        if 'response' in locals():
            print(response.text)

if __name__ == "__main__":
    test_voice_detection()
