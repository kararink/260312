import pytesseract
import os
import sys

# Set path
TESSERACT_PATHS = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
]
tesseract_cmd = None
for path in TESSERACT_PATHS:
    if os.path.exists(path):
        tesseract_cmd = path
        break

if not tesseract_cmd:
    print("Tesseract not found")
    sys.exit(1)

pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
print(f"Using Tesseract at: {tesseract_cmd}")

try:
    langs = pytesseract.get_languages()
    print(f"Available languages: {langs}")
except Exception as e:
    print(f"Error getting languages: {e}")

# Check tessdata file specifically
tessdata_dir = os.path.join(os.path.dirname(tesseract_cmd), 'tessdata')
jpn_file = os.path.join(tessdata_dir, 'jpn.traineddata')

if os.path.exists(jpn_file):
    size = os.path.getsize(jpn_file)
    print(f"jpn.traineddata found. Size: {size} bytes")
else:
    print(f"jpn.traineddata NOT found at {jpn_file}")
