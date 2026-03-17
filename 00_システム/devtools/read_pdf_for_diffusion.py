import fitz
import sys
import os

def extract_pdf_data(pdf_path):
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        return f"Error opening {pdf_path}: {e}"
        
    output = []
    output.append(f"## Source: {os.path.basename(pdf_path)}")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Extract text
        text = page.get_text()
        
        # Extract highlights/annotations
        annots = page.annots()
        highlights = []
        if annots:
            for annot in annots:
                # 8 = Highlight, 9 = Underline, 10 = Squiggly, 11 = StrikeOut
                if annot.type[0] in [8, 9]:
                    try:
                        highlight_text = page.get_textbox(annot.rect).strip()
                        # Sometimes highlight_text has newlines, replace them
                        highlight_text = " ".join(highlight_text.splitlines())
                        if highlight_text:
                            highlights.append(f"[Highlight] {highlight_text}")
                    except:
                        pass
                
                # notes
                content = annot.info.get('content')
                if content:
                    highlights.append(f"[Note] {content}")
        
        output.append(f"### Page {page_num+1}")
        if highlights:
            output.append("#### Highlights & Notes on this page:")
            for h in highlights:
                output.append(f"- {h}")
            output.append("")
            
        output.append("#### Text:")
        output.append(text)
        output.append("---\n")
        
    return "\n".join(output)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python read_pdf.py <output.md> <pdf1> <pdf2> ...")
        sys.exit(1)
        
    out_path = sys.argv[1]
    pdfs = sys.argv[2:]
    
    # Ensure distinct output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    
    with open(out_path, 'w', encoding='utf-8') as f:
        for pdf in pdfs:
            print(f"Extracting: {pdf}")
            content = extract_pdf_data(pdf)
            f.write(content + "\n\n")
    print(f"Done. Extracted content to {out_path}")
