import soundfile as sf
import librosa
import numpy as np

def scale_audio(input_path):
    output_path = input_path.replace(".wav", "_small.wav") # Keep wav to avoid mp3 encoder issues without ffmpeg
    
    print(f"Reading {input_path}...")
    try:
        # Load with generic librosa (or soundfile directly)
        data, samplerate = sf.read(input_path)
        
        # Downsample strategy: 
        # 1. Convert to Mono if stereo
        if len(data.shape) > 1:
            data = np.mean(data, axis=1)
            
        # 2. Resample (naive slicing for speed without scipy/librosa heavy deps if possible, 
        # but we have scipy installed from before).
        # Let's just save it with a lower samplerate using soundfile? 
        # Soundfile just writes what you give it.
        
        # We'll just write it as 16kHz mono.
        # Simple decimation if sample rate is high (e.g. 44100 -> ~14k)
        step = int(samplerate / 16000)
        if step > 1:
            data = data[::step]
            
        sf.write(output_path, data, 16000)
        
        print(f"Success! Created: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    file_path = r"c:\Users\ks209\Downloads\rdp\final docs\Impact AI Hackathon Voice-20260215T161739Z-1-001\Impact AI Hackathon Voice\1763550506667944927-335862601289795-enhanced-v2.wav"
    scale_audio(file_path)
