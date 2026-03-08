import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

# Load env
env_path = r"C:\Users\杢之助\2nd-Brain\00_システム\devtools\.env"
load_dotenv(dotenv_path=env_path)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-2.5-flash')

pdf_dir = r"C:\Users\杢之助\2nd-Brain\99_Sbox\書籍OCR\260224_マスタリング_TCP_IP_情報セキュリティ編"
files_to_upload = [
    os.path.join(pdf_dir, "260224-01_マスタリング_TCP_IP_情報セキュリティ編.pdf"),
    os.path.join(pdf_dir, "260224-02_マスタリング_TCP_IP_情報セキュリティ編.pdf"),
    os.path.join(pdf_dir, "260224-03_マスタリング_TCP_IP_情報セキュリティ編.pdf")
]

uploaded_files = []
for p in files_to_upload:
    if os.path.exists(p):
        print(f"Uploading {p}...")
        u = genai.upload_file(p)
        uploaded_files.append(u)
        time.sleep(2)

print("Waiting for files to be processed...")
for u in uploaded_files:
    while True:
        f = genai.get_file(u.name)
        if f.state.name == "ACTIVE":
            break
        elif f.state.name == "FAILED":
            print("File processing failed.")
            sys.exit(1)
        time.sleep(2)

prompt_file = r"C:\Users\杢之助\2nd-Brain\00_システム\01_Prompts\Note拡散ワークフロー\1_Note拡散_抽出プロンプト.md"
with open(prompt_file, 'r', encoding='utf-8') as f:
    prompt_text = f.read()
    
# プレースホルダーを置換
prompt_text = prompt_text.replace("{TARGET_SOURCE}", "添付のPDFファイル群（マスタリングTCP/IP 情報セキュリティ編）")

print("Generating content...")
response = model.generate_content([prompt_text] + uploaded_files)

out_file = r"C:\Users\杢之助\2nd-Brain\04_アウトプット\NoteDiffusion_Extraction.md"
os.makedirs(os.path.dirname(out_file), exist_ok=True)
with open(out_file, 'w', encoding='utf-8') as f:
    f.write(response.text)

print(f"Finished extracting insights to {out_file}")

# Clean up remote files
for u in uploaded_files:
    genai.delete_file(u.name)
