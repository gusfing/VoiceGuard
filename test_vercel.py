import requests
import base64
import json
import os
import soundfile as sf
import numpy as np

# Configuration
API_URL = "https://rdp-three-ruby.vercel.app/api/v1/detect"
API_KEY = "hackathon_master_key_123"

# Path to your test files (Update this to where your files are!)
TEST_FOLDER = "my_test_files" 

def compress_audio(input_path):
    """Compresses audio if too large using soundfile (Native Python)"""
    try:
        print(f"   ⚠️ File > 4MB. Compressing...")
        output_path = input_path.replace(os.path.splitext(input_path)[1], "_small.wav")
        
        # Read file
        data, samplerate = sf.read(input_path)
        
        # Convert to Mono
        if len(data.shape) > 1:
            data = np.mean(data, axis=1)
            
        # Downsample to 16kHz
        target_sr = 16000
        step = int(samplerate / target_sr)
        if step > 1:
            data = data[::step]
            
        # TRIM LENGTH: Max 60 seconds to stay under Vercel 4.5MB limit
        # 16kHz * 2 bytes * 60s = ~1.9MB (Safe)
        max_samples = target_sr * 60 
        if len(data) > max_samples:
            print(f"   ✂️  Trimming to 60 seconds...")
            data = data[:max_samples]
            
        # Write 16-bit PCM wav
        sf.write(output_path, data, target_sr, subtype='PCM_16')
        print(f"   ✅ Compressed to: {os.path.basename(output_path)}")
        return output_path
    except Exception as e:
        print(f"   ❌ Compression failed: {e}")
        return None 

def test_file(file_path):
    print(f"\n🔍 Testing: {os.path.basename(file_path)}")
    
    # 1. Check Size & Compress if needed (> 4MB)
    try:
        if os.path.exists(file_path):
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            if file_size_mb > 4.0:
                compressed_path = compress_audio(file_path)
                if compressed_path:
                    file_path = compressed_path
    except Exception as e:
        print(f"   ⚠️ Warning: Size check failed: {e}")

    # 2. Encode Audio
    try:
        with open(file_path, "rb") as f:
            audio_content = base64.b64encode(f.read()).decode("utf-8")
    except Exception as e:
        print(f"   ❌ Error reading file: {e}")
        return

    # 2. Key Payload
    payload = {
        "language": "Unknown",
        "audioFormat": os.path.splitext(file_path)[1][1:], # mp3 or wav
        "audioBase64": audio_content
    }
    
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    # 3. Send Request
    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Result: {data.get('classification')}")
            print(f"   📊 Confidence: {data.get('confidenceScore')}")
        else:
            print(f"   ❌ HTTP {response.status_code}: {response.text}")
            
    except Exception as e:
        print(f"   ❌ Network Error: {e}")

def main():
    if not os.path.exists(TEST_FOLDER):
        os.makedirs(TEST_FOLDER)
        print(f"📁 Created folder: '{TEST_FOLDER}'")
        print(f"👉 Please put your audio files inside '{TEST_FOLDER}' and run this script again!")
        return

    files = [f for f in os.listdir(TEST_FOLDER) if f.lower().endswith(('.mp3', '.wav', '.ogg', '.m4a')) and '_small' not in f]
    
    if not files:
        print(f"⚠️ No audio files found in '{TEST_FOLDER}'.")
        print("👉 Please add .mp3 or .wav files there.")
        return

    print(f"🚀 Starting Test on {len(files)} files against LIVE API...")
    print(f"🌐 URL: {API_URL}")
    for f in files:
        test_file(os.path.join(TEST_FOLDER, f))
    
    print("\n✅ Testing Complete!")

if __name__ == "__main__":
    main()
