import PyPDF2
import os

pdf_files = [
    r"C:\Users\杢之助\2nd-Brain\99_Sbox\03_読書・OCR\260324-01_人生を変える科学的な集中術（鈴木祐著）.pdf",
    r"C:\Users\杢之助\2nd-Brain\99_Sbox\03_読書・OCR\260324-02_人生を変える科学的な集中術（鈴木祐著）.pdf",
    r"C:\Users\杢之助\2nd-Brain\99_Sbox\03_読書・OCR\260324-03_人生を変える科学的な集中術（鈴木祐著）.pdf",
    r"C:\Users\杢之助\2nd-Brain\99_Sbox\03_読書・OCR\260324-04_人生を変える科学的な集中術（鈴木祐著）.pdf"
]

text = ""
for f in pdf_files:
    try:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            extr = page.extract_text()
            if extr:
                text += extr + "\n"
    except Exception as e:
        print(f"Error reading {f}: {e}")

output_path = r"C:\Users\杢之助\2nd-Brain\04_アウトプット\TARGET_SOURCE.md"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)
print("PDF text extracted to TARGET_SOURCE.md")
