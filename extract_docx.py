import zipfile
import re

doc_path = r'C:\Users\杢之助\2nd-Brain\99_Sbox\260304_匿名通報（(株)誠工業 営業所技術者の常勤性に疑義）\260307_戦略助言【栗田】：(株)誠工業 営業所技術者の常勤性疑義に係る匿名通報への対応.docx'
out_path = r'C:\Users\杢之助\2nd-Brain\99_Sbox\260304_匿名通報（(株)誠工業 営業所技術者の常勤性に疑義）\extracted_docx_text.txt'

with zipfile.ZipFile(doc_path) as doc:
    xml_content = doc.read('word/document.xml').decode('utf-8')
    texts = re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml_content)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(texts))
