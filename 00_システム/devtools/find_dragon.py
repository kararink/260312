import sys
from PIL import Image

def get_redness(image_path):
    try:
        img = Image.open(image_path).convert("RGB")
        img.thumbnail((100, 100)) # small size for speed
        pixels = list(img.getdata())
        red_score = 0
        for r, g, b in pixels:
            if r > 150 and r > g + 40 and r > b + 40:
                red_score += 1
        return red_score / len(pixels)
    except Exception as e:
        return -1

if __name__ == "__main__":
    candidates = [
        r"C:\Users\杢之助\2nd-Brain\00_システム\03_Assets\Stamps\copilot_image_1752743988811.jpeg",
        r"C:\Users\杢之助\2nd-Brain\00_システム\03_Assets\Stamps\copilot_image_1752744538286.jpeg",
        r"C:\Users\杢之助\2nd-Brain\00_システム\03_Assets\Stamps\Gemini_Generated_Image_g5n2dhg5n2dhg5n2.png"
    ]
    
    for c in candidates:
        score = get_redness(c)
        print(f"Redness score for {c.split('\\')[-1]}: {score:.3f}")
