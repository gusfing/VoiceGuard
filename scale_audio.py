import os
import subprocess

def scale_audio(input_path):
    output_path = input_path.replace(".wav", "_small.mp3")
    
    # Use ffmpeg to downsample to 16kHz mono mp3 (very small)
    cmd = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-ar", "16000",       # 16kHz sample rate
        "-ac", "1",           # Mono channel
        "-b:a", "32k",        # 32k bitrate
        output_path
    ]
    
    print(f"Compressing {input_path}...")
    try:
        subprocess.run(cmd, check=True)
        print(f"Success! Created: {output_path}")
        return output_path
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    file_path = r"c:\Users\ks209\Downloads\rdp\final docs\Impact AI Hackathon Voice-20260215T161739Z-1-001\Impact AI Hackathon Voice\1763550506667944927-335862601289795-enhanced-v2.wav"
    scale_audio(file_path)
