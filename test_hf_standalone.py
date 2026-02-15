import os
import requests
import dotenv

# Load env
dotenv.load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
# UPDATED URL: Trying 'dima806' (Generic Audio Classification often works better)
# If this fails, we will stick to our local checks which are working 100%.
HF_URL = "https://api-inference.huggingface.co/models/dima806/deepfake_audio_detection"

def test_hf_direct():
    print(f"🔑 Token: {HF_TOKEN[:5]}... (Loaded)")
    print(f"🌐 URL: {HF_URL}")
    
    # Find a test file
    test_files = [f for f in os.listdir("my_test_files") if f.endswith(".mp3")]
    if not test_files:
        print("❌ No files in my_test_files")
        return
        
    target_file = os.path.join("my_test_files", test_files[0])
    print(f"📁 Sending: {target_file}")
    
    with open(target_file, "rb") as f:
        data = f.read()
    
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    
    try:
        response = requests.post(HF_URL, headers=headers, data=data)
        print(f"⬇️  Status: {response.status_code}")
        print(f"📄 Response: {response.json()}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if not HF_TOKEN:
        print("❌ HF_TOKEN not found in .env")
    else:
        test_hf_direct()
