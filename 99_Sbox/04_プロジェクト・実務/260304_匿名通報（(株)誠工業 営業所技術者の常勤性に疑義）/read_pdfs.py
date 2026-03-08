import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
    def extract_text(pdf_path):
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
except ImportError:
    try:
        import PyPDF2
        def extract_text(pdf_path):
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
            return text
    except ImportError:
        print("Please install PyMuPDF or PyPDF2")
        sys.exit(1)

def main():
    target_dir = Path(sys.argv[1])
    for pdf_file in target_dir.glob("*.pdf"):
        print(f"--- {pdf_file.name} ---")
        try:
            text = extract_text(pdf_file)
            out_file = pdf_file.with_suffix('.txt')
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Extracted to {out_file.name}")
        except Exception as e:
            print(f"Error reading {pdf_file.name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    else:
        print("Usage: python read_pdfs.py <dir>")
