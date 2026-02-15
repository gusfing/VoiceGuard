import requests
import base64
import json
import os

def evaluate_voice_detection_api(endpoint_url, api_key, test_files):
    """
    Evaluate your voice detection API locally using the same logic as the official evaluator.
    """
    if not endpoint_url:
        print("❌ Error: Endpoint URL is required")
        return False
    
    if not test_files or len(test_files) == 0:
        print("❌ Error: No test files provided")
        return False
    
    total_files = len(test_files)
    score_per_file = 100 / total_files
    total_score = 0
    file_results = []
    
    print(f"\n{'='*60}")
    print(f"🚀 Starting Evaluation")
    print(f"{'='*60}")
    print(f"Endpoint: {endpoint_url}")
    print(f"Total Test Files: {total_files}")
    print(f"Score per File: {score_per_file:.2f}")
    print(f"{'='*60}\n")
    
    for idx, file_data in enumerate(test_files):
        language = file_data.get('language', 'English')
        file_path = file_data.get('file_path', '')
        expected_classification = file_data.get('expected_classification', '')
        
        print(f"📝 Test {idx + 1}/{total_files}: {file_path}")
        
        if not file_path or not expected_classification:
            print(f"   ⚠️  Skipped: Missing file path or expected classification\n")
            continue
        
        # Read and encode audio file
        try:
            with open(file_path, 'rb') as audio_file:
                audio_base64 = base64.b64encode(audio_file.read()).decode('utf-8')
        except Exception as e:
            print(f"   ❌ Failed to read file: {str(e)}\n")
            continue
        
        # Prepare request
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': api_key
        }
        
        request_body = {
            'language': language,
            'audioFormat': 'mp3',
            'audioBase64': audio_base64
        }
        
        try:
            # Send request
            response = requests.post(endpoint_url, headers=headers, json=request_body, timeout=30)
            
            if response.status_code != 200:
                print(f"   ❌ HTTP Status: {response.status_code}")
                print(f"   Response: {response.text}\n")
                continue
            
            response_data = response.json()
            
            if not isinstance(response_data, dict):
                print(f"   ❌ Invalid response type (not a JSON object)\n")
                continue
            
            response_status = response_data.get('status', '')
            response_classification = response_data.get('classification', '')
            confidence_score = response_data.get('confidenceScore', None)
            
            if not response_status or not response_classification or confidence_score is None:
                print(f"   ❌ Missing required fields")
                print(f"   Response: {json.dumps(response_data, indent=2)}\n")
                continue
            
            if response_status != 'success':
                print(f"   ❌ Status not 'success': {response_status}\n")
                continue
            
            # Score calculation
            file_score = 0
            if response_classification == expected_classification:
                if confidence_score >= 0.8:
                    file_score = score_per_file
                elif confidence_score >= 0.6:
                    file_score = score_per_file * 0.75
                elif confidence_score >= 0.4:
                    file_score = score_per_file * 0.5
                else:
                    file_score = score_per_file * 0.25
                
                total_score += file_score
                print(f"   ✅ Classification: {response_classification} (Correct!)")
                print(f"   📊 Confidence: {confidence_score:.2f}")
                print(f"   🎯 Score: {file_score:.2f}/{score_per_file:.2f}\n")
            else:
                print(f"   ❌ Classification: {response_classification} (Expected: {expected_classification})")
                print(f"   📊 Confidence: {confidence_score:.2f}")
                print(f"   🎯 Score: 0/{score_per_file:.2f}\n")
        
        except Exception as e:
            print(f"   ❌ Error: {str(e)}\n")
    
    print(f"{'='*60}")
    print(f"📊 EVALUATION SUMMARY")
    print(f"{'='*60}")
    print(f"Final Score: {round(total_score)}/100")
    print(f"{'='*60}\n")
    return True

if __name__ == '__main__':
    # Default to localhost, but allow user to change it for Vercel
    print("\n--- API Testing Configuration ---")
    use_vercel = input("Do you want to test your Vercel deployment? (y/n): ").lower().strip() == 'y'
    
    if use_vercel:
        vercel_url = input("Enter your Vercel URL (e.g., https://voiceguard.vercel.app): ").strip()
        # Ensure no trailing slash and correct endpoint path
        if vercel_url.endswith('/'):
            vercel_url = vercel_url[:-1]
        if not vercel_url.endswith('/api/v1/detect'):
            ENDPOINT_URL = f"{vercel_url}/api/v1/detect"
        else:
            ENDPOINT_URL = vercel_url
    else:
        ENDPOINT_URL = 'http://127.0.0.1:8000/api/v1/detect'

    print(f"\nTesting Endpoint: {ENDPOINT_URL}")
    API_KEY = 'hackathon_master_key_123'
    
    # Path to reference audio files
    BASE_DIR = r"c:\Users\ks209\Downloads\rdp\final docs\Impact AI Hackathon Voice-20260215T161739Z-1-001\Impact AI Hackathon Voice"
    
    TEST_FILES = [
        {
            'language': 'English',
            'file_path': os.path.join(BASE_DIR, 'English_voice_AI_GENERATED.mp3'),
            'expected_classification': 'AI_GENERATED'
        },
        {
            'language': 'Hindi',
            'file_path': os.path.join(BASE_DIR, 'Hindi_Voice_HUMAN.mp3'),
            'expected_classification': 'HUMAN'
        },
        {
            'language': 'Malayalam',
            'file_path': os.path.join(BASE_DIR, 'Malayalam_AI_GENERATED.mp3'),
            'expected_classification': 'AI_GENERATED'
        },
        {
            'language': 'Tamil',
            'file_path': os.path.join(BASE_DIR, 'TAMIL_VOICE__HUMAN.mp3'),
            'expected_classification': 'HUMAN'
        },
        {
            'language': 'Telugu',
            'file_path': os.path.join(BASE_DIR, 'Telugu_Voice_AI_GENERATED.mp3'),
            'expected_classification': 'AI_GENERATED'
        },
        {
            'language': 'Unknown',
            'file_path': r'C:\Users\ks209\Downloads\rdp\final docs\Impact AI Hackathon Voice-20260215T161739Z-1-001\WhatsApp Ptt 2026-02-16 at 12.57.10 AM.ogg',
            'expected_classification': 'HUMAN'
        },
        {
            'language': 'Unknown',
            'file_path': r'c:\Users\ks209\Downloads\rdp\final docs\Impact AI Hackathon Voice-20260215T161739Z-1-001\Impact AI Hackathon Voice\1763550506667944927-335862601289795-enhanced-v2_small.wav',
            'expected_classification': 'AI_GENERATED'
        },
        {
            'language': 'Unknown',
            'file_path': r'c:\Users\ks209\Downloads\rdp\final docs\Impact AI Hackathon Voice-20260215T161739Z-1-001\Impact AI Hackathon Voice\kawaki reel 4.mp3',
            'expected_classification': 'AI_GENERATED'
        }
    ]
    
    evaluate_voice_detection_api(ENDPOINT_URL, API_KEY, TEST_FILES)
