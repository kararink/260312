import sys
import os

pdf_dir = r"C:\Users\杢之助\2nd-Brain\99_Sbox\書籍OCR\260224_マスタリング_TCP_IP_情報セキュリティ編"
output_file = os.path.join(pdf_dir, "combined.md")

combined_text = ""

try:
    import fitz
    for i in range(1, 4):
        pdf_path = os.path.join(pdf_dir, f"260224-0{i}_マスタリング_TCP_IP_情報セキュリティ編.pdf")
        if os.path.exists(pdf_path):
            doc = fitz.open(pdf_path)
            for page in doc:
                combined_text += page.get_text() + "\n"
            doc.close()
except ImportError:
    try:
        from PyPDF2 import PdfReader
        for i in range(1, 4):
            pdf_path = os.path.join(pdf_dir, f"260224-0{i}_マスタリング_TCP_IP_情報セキュリティ編.pdf")
            if os.path.exists(pdf_path):
                reader = PdfReader(pdf_path)
                for page in reader.pages:
                    combined_text += page.extract_text() + "\n"
    except ImportError:
        print("Please install PyMuPDF (fitz) or PyPDF2")
        sys.exit(1)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(combined_text)

print(f"Extracted {len(combined_text)} characters.")
