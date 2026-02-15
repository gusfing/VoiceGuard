import requests
import base64

# Configuration
API_URL = "http://127.0.0.1:8000/api/v1/detect"
API_KEY = "your_secret_api_key"

def test_detect_endpoint():
    print(f"Testing API at: {API_URL}")
    
    # Create a dummy base64 string (simulating an audio file)
    dummy_audio = base64.b64encode(b"fake_mp3_content").decode("utf-8")
    
    payload = {
        "audio_data": dummy_audio
    }
    
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("\nResponse:")
            print(f"Server Status: {data.get('status')}")
            print(f"Classification: {data['data'].get('classification')}")
            print(f"Confidence Score: {data['data'].get('confidence_score')}")
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("\n[ERROR] Could not connect to the server.")
        print("Make sure the server is running! Run: uvicorn app.main:app --reload")

if __name__ == "__main__":
    test_detect_endpoint()
