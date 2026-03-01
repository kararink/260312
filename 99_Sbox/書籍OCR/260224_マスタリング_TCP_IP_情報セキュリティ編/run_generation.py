import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

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

prompt_file = r"C:\Users\杢之助\2nd-Brain\00_システム\01_Prompts\Note拡散ワークフロー\2_Note拡散_生成プロンプト.md"
extraction_file = r"C:\Users\杢之助\2nd-Brain\04_アウトプット\NoteDiffusion_Extraction.md"

with open(prompt_file, 'r', encoding='utf-8') as f:
    prompt_text = f.read()

with open(extraction_file, 'r', encoding='utf-8') as f:
    extraction_text = f.read()
    
# プレースホルダーを置換
prompt_text = prompt_text.replace("{EXTRACTION_RESULT}", extraction_text)
prompt_text = prompt_text.replace("{TARGET_SOURCE}", "添付のPDFファイル群（マスタリングTCP/IP 情報セキュリティ編）")

print("Generating contents...")
response = model.generate_content([prompt_text] + uploaded_files)

out_file = r"C:\Users\杢之助\2nd-Brain\04_アウトプット\NoteDiffusion_Draft.md"
with open(out_file, 'w', encoding='utf-8') as f:
    f.write(response.text)

print(f"Finished generating draft to {out_file}")

# Clean up remote files
for u in uploaded_files:
    genai.delete_file(u.name)
