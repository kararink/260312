
import os
import re
from bs4 import BeautifulSoup
from elevenlabs import ElevenLabs

# Configuration
# Ideally load from .env, but for this script we assume the environment variable is set
# or we can try to read it from the .env file if it exists in the current directory.
# This script will run in the user's directory so it should pick up the env var if set in the terminal session.
# If not, we might need to manually load it.
API_KEY = os.environ.get("ELEVENLABS_API_KEY") 
if not API_KEY:
    # Fallback: try to read from .env in current directory
    try:
        with open('.env', 'r') as f:
            for line in f:
                if line.startswith('ELEVENLABS_API_KEY='):
                    API_KEY = line.strip().split('=')[1]
                    break
    except:
        pass

SOURCE_FILE = r"c:\Users\杢之助\2nd-Brain\Clippings\260216_パレオなチャンネル_「重金属が入ってそうな食品とサプリ」パーフェクトガイド.md"
OUTPUT_FILE = r"c:\Users\杢之助\2nd-Brain\test_tts_heavy_metal.mp3"

def clean_text(text):
    # Remove YAML frontmatter
    text = re.sub(r'^---[\s\S]*?---\n', '', text)
    
    # Pre-process HTML table to make it readable
    # Replace table row endings with newlines
    text = text.replace('</tr>', '\n')
    # Replace cell endings with a separator (e.g., ": ")
    text = text.replace('</td>', ': ')
    text = text.replace('</th>', ': ')
    
    # Remove image tags
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    
    # Remove links but keep text [text](url) -> text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    
    # Use BeautifulSoup to strip HTML tags and get text
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text(separator='\n')
    
    # Remove markdown formatting characters
    text = text.replace('**', '')
    text = text.replace('__', '')
    text = text.replace('##', '')
    text = text.replace('###', '')
    
    # Filter out navigation and footer noise
    lines = text.split('\n')
    cleaned_lines = []
    
    # Heuristics to skip navigation/footer lines
    skip_phrases = [
        "タグを追加", "記事をメールで送信", "動画 静画 生放送", 
        "その他- プレミアム会員登録", "違反報告", 
        "これより新しい記事はありません", "検索", 
        "ニコニコ大百科", "ログイン", "ニコニ広告"
    ]
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Skip lines that contain typical navigation text
        if any(phrase in line for phrase in skip_phrases):
            continue
            
        # Skip lines that look like just URLs
        if line.startswith("http://") or line.startswith("https://"):
            continue

        # Skip lines that are just symbols
        if re.match(r'^[-\s\d\W]+$', line) and len(line) < 5:
            continue
            
        cleaned_lines.append(line)
        
    return "\n".join(cleaned_lines)

def main():
    if not API_KEY:
        print("Error: ELEVENLABS_API_KEY not found.")
        return

    try:
        with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {SOURCE_FILE}")
        return

    cleaned_content = clean_text(content)
    print("--- Cleaned Text Preview ---")
    print(cleaned_content[:500]) # Preview first 500 chars
    print("...")
    print("----------------------------")
    
    # Initialize client
    try:
        client = ElevenLabs(api_key=API_KEY)
        
        # George is a standard pre-made voice, usually good for general narration.
        # Ensure we use a multilingual model for Japanese support.
        audio = client.text_to_speech.convert(
            text=cleaned_content,
             # Using a well-known voice ID or name. "George" is often valid as a name or use ID if known.
             # "JBFqnCBsd6RMkjVDRZzb" is George's ID.
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2"
        )
        
        # Save audio
        with open(OUTPUT_FILE, 'wb') as f:
            for chunk in audio:
                if chunk:
                    f.write(chunk)
        print(f"Audio successfully saved to {OUTPUT_FILE}")
        
    except Exception as e:
        print(f"Error during ElevenLabs API call: {e}")

if __name__ == "__main__":
    main()
