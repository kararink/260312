import os
import sys
import fitz
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path
from PIL import Image
import io
import time

# Setup Gemini
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY not found in .env")
    sys.exit(1)

genai.configure(api_key=GEMINI_API_KEY)
# We can use gemini-2.5-flash since it's fast and supports vision.
model = genai.GenerativeModel('gemini-2.5-flash')

def get_text_from_image(img_bytes, retries=5):
    image = Image.open(io.BytesIO(img_bytes))
    prompt = (
        "提供された画像に含まれる文章を、一言一句正確に文字起こししてください。"
        "縦書き、横書き、ルビ（フリガナ）、複雑なレイアウトであっても、意味が通るように自然なテキストとして出力してください。"
        "ページ番号やシステムの文字は除外して、本文のみを抽出してください。"
        "出力は抽出したテキストのみとし、説明や挨拶は絶対に含めないでください。"
    )
    for attempt in range(retries):
        try:
            response = model.generate_content([prompt, image])
            time.sleep(4.5)  # Respect 15 RPM
            return response.text.strip()
        except Exception as e:
            err_msg = str(e)
            if "429" in err_msg or "quota" in err_msg.lower():
                print(f"[Attempt {attempt+1}/{retries}] Rate limited, waiting 45 seconds... {err_msg}")
                time.sleep(45)
            else:
                return f"[Gemini API Error] {e}"
    return "[Gemini API Error] Max retries exceeded"

def extract_pdf_ocr(pdf_path):
    print(f"Opening: {pdf_path}")
    doc = fitz.open(pdf_path)
    output = []
    output.append(f"## Source: {os.path.basename(pdf_path)}\n")
    
    for page_num in range(len(doc)):
        print(f"Processing {pdf_path} - Page {page_num + 1}/{len(doc)}")
        page = doc[page_num]
        
        # Render to image: zoom factor to get good quality
        zoom = 2.0
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        img_bytes = pix.tobytes("png")
        
        text = get_text_from_image(img_bytes)
        output.append(f"### Page {page_num+1}\n")
        output.append(text + "\n")
        output.append("---\n")
        
    return "\n".join(output)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pdf_ocr_gemini.py <output.md> <pdf1> <pdf2> ...")
        sys.exit(1)
        
    out_path = sys.argv[1]
    pdfs = sys.argv[2:]
    
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    
    with open(out_path, 'w', encoding='utf-8') as f:
        for pdf in pdfs:
            content = extract_pdf_ocr(pdf)
            f.write(content + "\n\n")
            
    print(f"Done. Saved to {out_path}")
