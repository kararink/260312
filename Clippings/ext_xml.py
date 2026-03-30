import zipfile
import xml.etree.ElementTree as ET

def get_text_from_node(node, ns):
    text = []
    for elem in node.iter():
        if elem.tag == f'{{{ns["w"]}}}t' and elem.text:
            text.append(elem.text)
    return "".join(text)

def parse_docx(filepath):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    doc = zipfile.ZipFile(filepath)
    xml_content = doc.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    
    out = []
    
    # Simple top-down traversal to preserve order
    for elem in tree.iter():
        if elem.tag == f'{{{ns["w"]}}}p':
            t = get_text_from_node(elem, ns)
            if t.strip():
                # Avoid duplicates if p is iterated inside something else
                out.append(t)
            # clear the node's text so it's not double-counted if we do weird tree walks
            for child in elem.iter():
                if child.tag == f'{{{ns["w"]}}}t':
                    child.text = ""
    return "\n".join(out)

print(parse_docx(r"C:\Users\杢之助\2nd-Brain\Clippings\260330_水技C　懸案等整理票③（人事）.docx"))
