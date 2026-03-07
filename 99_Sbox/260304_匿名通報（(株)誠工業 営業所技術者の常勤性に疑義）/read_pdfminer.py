import sys
import subprocess
from pathlib import Path

def main():
    target_dir = Path(r"C:\Users\杢之助\2nd-Brain\99_Sbox\260304_匿名通報（(株)誠工業 営業所技術者の常勤性に疑義）")
    files = [
        "260304_匿名通報（(株)誠工業 営業所技術者の常勤性に疑義）.pdf",
        "260306_決裁（報告）：匿名通報（(株)誠工業 営業所技術者の常勤性に疑義）.pdf"
    ]
    
    # Try using pdfminer.six if installed
    try:
        from pdfminer.high_level import extract_text
        for f in files:
            pdf_path = target_dir / f
            print(f"pdfminer extracting {f}...")
            text = extract_text(pdf_path)
            out = target_dir / (f + ".pdfminer.txt")
            out.write_text(text, encoding='utf-8')
            print(f"Done pdfminer {f}, len: {len(text)}")
    except ImportError:
        print("pdfminer.six not installed.")
        subprocess.run([sys.executable, "-m", "pip", "install", "pdfminer.six"])
        from pdfminer.high_level import extract_text
        for f in files:
            pdf_path = target_dir / f
            print(f"pdfminer extracting {f}...")
            text = extract_text(pdf_path)
            out = target_dir / (f + ".pdfminer.txt")
            out.write_text(text, encoding='utf-8')
            print(f"Done pdfminer {f}, len: {len(text)}")

if __name__ == "__main__":
    main()
