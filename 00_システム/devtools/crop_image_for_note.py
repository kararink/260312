import sys
import os
from PIL import Image

def process_thumbnail(base_image_path, stamp_image_path, output_path):
    # 1. Load Base Image
    base_img = Image.open(base_image_path).convert("RGBA")
    
    # Target resolution for Note header (1280x670 -> 1.91:1)
    target_w, target_h = 1280, 670
    target_ratio = target_w / target_h
    
    # Current resolution
    bw, bh = base_img.size
    current_ratio = bw / bh
    
    # 2. Crop so it fills exactly 1.91:1
    if current_ratio > target_ratio:
        # Too wide, crop horizontally
        new_w = int(bh * target_ratio)
        left = (bw - new_w) // 2
        right = left + new_w
        base_img = base_img.crop((left, 0, right, bh))
    else:
        # Too tall, crop vertically
        new_h = int(bw / target_ratio)
        top = (bh - new_h) // 2
        bottom = top + new_h
        base_img = base_img.crop((0, top, bw, bottom))
        
    # 3. Resize to exactly 1280x670
    base_img = base_img.resize((1280, 670), Image.Resampling.LANCZOS)
    
    # 4. Load Stamp Image
    try:
        stamp_img = Image.open(stamp_image_path).convert("RGBA")
        
        # Scale stamp (e.g. 20% of the height)
        stamp_h = int(670 * 0.20)
        sw, sh = stamp_img.size
        # keep stamp aspect ratio
        stamp_w = int(sw * (stamp_h / sh))
        stamp_img = stamp_img.resize((stamp_w, stamp_h), Image.Resampling.LANCZOS)
        
        # Position at bottom-right corner with 30px margin
        margin_x = 30
        margin_y = 30
        pos = (1280 - stamp_w - margin_x, 670 - stamp_h - margin_y)
        
        # Create composite
        composite = Image.new("RGBA", (1280, 670), (0, 0, 0, 0))
        composite.paste(base_img, (0, 0))
        composite.paste(stamp_img, pos, mask=stamp_img)
    except Exception as e:
        print(f"Warning: Could not load or apply stamp ({e}). Stamping will be skipped.")
        composite = base_img

    # 5. Save output
    if output_path.lower().endswith(('.jpg', '.jpeg')):
         composite = composite.convert("RGB")
    
    composite.save(output_path, quality=95)
    print(f"Saved highly processed Note thumbnail to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python crop_and_stamp.py <base_image> <stamp_image> <output_image>")
        sys.exit(1)
        
    base_path = sys.argv[1]
    stamp_path = sys.argv[2]
    out_path = sys.argv[3]
    process_thumbnail(base_path, stamp_path, out_path)
