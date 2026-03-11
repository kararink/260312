import fitz
import sys

def extract_pdf_to_md(pdf_paths, output_md_path):
    all_text = []
    
    for path in pdf_paths:
        try:
            doc = fitz.open(path)
            all_text.append(f"# Source: {path}\n")
            for page in doc:
                text = page.get_text("text") # Extract as normal text
                all_text.append(text)
            doc.close()
        except Exception as e:
            print(f"Error reading {path}: {e}")
            
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(all_text))
        
    print(f"Extraction complete. Saved to {output_md_path}")

if __name__ == "__main__":
    pdf_paths = [
        r"c:\Users\杢之助\2nd-Brain\99_Sbox\03_読書・OCR\260309-01_「答えを急がない」_ほうがうまくいく（三浦麻子著）.pdf",
        r"c:\Users\杢之助\2nd-Brain\99_Sbox\03_読書・OCR\260309-02_「答えを急がない」_ほうがうまくいく（三浦麻子著）.pdf"
    ]
    output_md_path = r"c:\Users\杢之助\2nd-Brain\04_アウトプット\TARGET_SOURCE.md"
    extract_pdf_to_md(pdf_paths, output_md_path)
