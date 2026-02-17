import sys
import os
import datetime
import whisper
import argparse

# --- Configuration ---
# Paths are relative to the *script location* if needed, but we use absolute paths for robustness based on the devtools structure.
# This script is located at .agent/skills/transcriber/scripts/transcribe_target.py
# The venv acts as the execution environment.

# Output Directory (Same as the original tool)
OUTPUT_DIR = r"c:\Users\杢之助\2nd-Brain\03_知識ベース\00_文字起こしログ"

def process_file(filepath):
    print(f"\n[Processing] {filepath}")
    
    if not os.path.exists(filepath):
        print(f"[Error] File not found: {filepath}")
        return False

    try:
        # Load Model
        print("[System] Loading Whisper Model (base)...")
        model = whisper.load_model("base")
        
        # Transcribe directly using Whisper
        print(f"  Transcribing with Whisper (Base)...")
        result = model.transcribe(filepath, verbose=False, language="ja")
        text = result["text"]

        # Prepare Output Filename
        filename = os.path.basename(filepath)
        date_str = datetime.date.today().strftime("%Y-%m-%d")
        out_filename = f"{date_str}_Transcript_{os.path.splitext(filename)[0]}.md"
        out_path = os.path.join(OUTPUT_DIR, out_filename)
        
        # Ensure output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        header_text = f"# 文字起こし: {os.path.splitext(filename)[0]}\n\n"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(header_text + text)
        
        print(f"  -> Saved transcript to: {out_path}")
        return out_path

    except Exception as e:
        print(f"[Error] Failed processing {filepath}: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    parser = argparse.ArgumentParser(description="Transcribe a single audio file using Whisper.")
    parser.add_argument("audio_path", help="Path to the audio file to transcribe")
    args = parser.parse_args()

    audio_path = args.audio_path.strip('"').strip("'") # Remove quotes if passed deeply nested

    print(f"=== Single File Transcription ===")
    print(f"Target: {audio_path}")

    result_path = process_file(audio_path)
    
    if result_path:
        print(f"SUCCESS: Transcription saved to {result_path}")
    else:
        print("FAILURE: Transcription failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
