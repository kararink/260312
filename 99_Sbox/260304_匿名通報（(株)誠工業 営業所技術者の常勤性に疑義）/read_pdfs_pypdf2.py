import sys
from pathlib import Path
import PyPDF2

def extract_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
    except Exception as e:
        return f"Error: {e}"

def main():
    target_dir = Path(r"C:\Users\杢之助\2nd-Brain\99_Sbox\260304_匿名通報（(株)誠工業 営業所技術者の常勤性に疑義）")
    files_to_try = [
        "251225-00_メール 公益通報者保護制度に係る要綱の改正.pdf",
        "260304_匿名通報（(株)誠工業 営業所技術者の常勤性に疑義）.pdf",
        "260306_決裁（報告）：匿名通報（(株)誠工業 営業所技術者の常勤性に疑義）.pdf"
    ]
    for filename in files_to_try:
        pdf_file = target_dir / filename
        if pdf_file.exists():
            print(f"Extracting {filename} with PyPDF2...")
            text = extract_text(pdf_file)
            out_file = pdf_file.with_suffix('.txt')
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Done: {out_file.name}")

if __name__ == "__main__":
    main()
