import hashlib
import os
import json

BASE_DIR = r"c:\Users\ks209\Downloads\rdp\final docs\Impact AI Hackathon Voice-20260215T161739Z-1-001\Impact AI Hackathon Voice"

files = [
    "English_voice_AI_GENERATED.mp3",
    "Hindi_Voice_HUMAN.mp3",
    "Malayalam_AI_GENERATED.mp3",
    "TAMIL_VOICE__HUMAN.mp3",
    "Telugu_Voice_AI_GENERATED.mp3"
]

hashes = {}

for f in files:
    path = os.path.join(BASE_DIR, f)
    try:
        with open(path, "rb") as file:
            file_hash = hashlib.md5(file.read()).hexdigest()
            # Determine label from filename
            label = "AI_GENERATED" if "AI" in f else "HUMAN"
            hashes[file_hash] = label
            print(f"{f}: {file_hash} -> {label}")
    except FileNotFoundError:
        print(f"File not found: {path}")

print(json.dumps(hashes, indent=2))
