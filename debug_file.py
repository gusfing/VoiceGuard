import os
import math
from collections import Counter
import binascii

# FILE TO DEBUG
TEST_FOLDER = "my_test_files"
TARGET_FILE = "voice_preview_raqib - news reporter.mp3"  # The file that failed

def analyze_file(file_path):
    print(f"🚀 Analyzing: {os.path.basename(file_path)}")
    
    with open(file_path, "rb") as f:
        data = f.read()
        
    # 1. HEADER DUMP (Look for AI tags)
    print("\n--- 1. HEADER DUMP (First 200 bytes) ---")
    header = data[:200]
    try:
        print(f"ASCII: {header.decode('utf-8', errors='ignore')}")
    except:
        pass
    print(f"HEX: {binascii.hexlify(header)}")

    # 2. FOOTER DUMP (Tag info often here)
    print("\n--- 2. FOOTER DUMP (Last 200 bytes) ---")
    footer = data[-200:]
    try:
        print(f"ASCII: {footer.decode('utf-8', errors='ignore')}")
    except:
        pass
        
    # 3. ENTROPY ANALYSIS
    print("\n--- 3. DETAILED ENTROPY ---")
    
    # Global Entropy
    counts = Counter(data)
    total = len(data)
    ent = 0.0
    for c in counts.values():
        p = c / total
        ent -= p * math.log2(p)
    print(f"Global Entropy: {ent}")
    
    # Chunked Entropy (Variance check)
    # AI often has consistent entropy; Humans vary (pauses, breaths)
    chunk_size = 1000
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    entropies = []
    for chunk in chunks[:50]: # Check first 50 chunks
        c = Counter(chunk)
        l = len(chunk)
        e = 0.0
        for v in c.values():
            p = v / l
            e -= p * math.log2(p)
        entropies.append(e)
        
    avg_ent = sum(entropies) / len(entropies)
    max_ent = max(entropies)
    min_ent = min(entropies)
    variance = max_ent - min_ent
    
    print(f"Chunk Entropy Variance: {variance:.4f}")
    print(f"Avg Chunk Entropy: {avg_ent:.4f}")
    
    if variance < 0.5:
        print(">> LOW VARIANCE: Signal is suspiciously consistent (Likely AI)")
    else:
        print(">> HIGH VARIANCE: Signal changes a lot (Likely Human)")

def main():
    target_path = os.path.join(TEST_FOLDER, TARGET_FILE)
    
    if not os.path.exists(target_path):
        # Try to find any mp3 if specific one missing
        files = [f for f in os.listdir(TEST_FOLDER) if f.endswith('.mp3')]
        if files:
            target_path = os.path.join(TEST_FOLDER, files[0])
        else:
            print("File not found!")
            return
            
    analyze_file(target_path)

if __name__ == "__main__":
    main()
