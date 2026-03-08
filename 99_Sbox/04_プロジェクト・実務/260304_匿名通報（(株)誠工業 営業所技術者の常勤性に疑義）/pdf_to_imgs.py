import sys
from pathlib import Path
import fitz  # PyMuPDF

def main():
    target_dir = Path(r"C:\Users\杢之助\2nd-Brain\99_Sbox\260304_匿名通報（(株)誠工業 営業所技術者の常勤性に疑義）")
    files = [
        "260304_匿名通報（(株)誠工業 営業所技術者の常勤性に疑義）.pdf",
        "260306_決裁（報告）：匿名通報（(株)誠工業 営業所技術者の常勤性に疑義）.pdf"
    ]
    
    for f in files:
        pdf_path = target_dir / f
        try:
            doc = fitz.open(pdf_path)
            for page_num, page in enumerate(doc):
                pix = page.get_pixmap(dpi=150)
                out_path = target_dir / f"{f}_page_{page_num+1}.png"
                pix.save(out_path)
                print(f"Saved {out_path.name}")
        except Exception as e:
            print(f"Failed to process {f}: {e}")

if __name__ == "__main__":
    main()
