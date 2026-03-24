import fitz
import sys

pdf_files = [
    r"C:\Users\杢之助\2nd-Brain\99_Sbox\03_読書・OCR\260324-01_人生を変える科学的な集中術（鈴木祐著）.pdf",
    r"C:\Users\杢之助\2nd-Brain\99_Sbox\03_読書・OCR\260324-02_人生を変える科学的な集中術（鈴木祐著）.pdf",
    r"C:\Users\杢之助\2nd-Brain\99_Sbox\03_読書・OCR\260324-03_人生を変える科学的な集中術（鈴木祐著）.pdf",
    r"C:\Users\杢之助\2nd-Brain\99_Sbox\03_読書・OCR\260324-04_人生を変える科学的な集中術（鈴木祐著）.pdf"
]

text = ""
for f in pdf_files:
    try:
        doc = fitz.open(f)
        for page in doc:
            text += page.get_text() + "\n"
    except Exception as e:
        print(f"Error reading {f}: {e}")

with open(r"C:\Users\杢之助\2nd-Brain\04_アウトプット\TARGET_SOURCE.md", "w", encoding="utf-8") as f:
    f.write(text)
print(f"Extraction complete. Length: {len(text)}")
