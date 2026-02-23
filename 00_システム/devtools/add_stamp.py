import os
import sys
import random
import argparse
from PIL import Image

def get_random_stamp(stamps_dir):
    """Get a random stamp image from the stamps directory."""
    valid_extensions = {".png", ".jpg", ".jpeg"}
    stamps = [
        f for f in os.listdir(stamps_dir)
        if os.path.isfile(os.path.join(stamps_dir, f)) and os.path.splitext(f)[1].lower() in valid_extensions
    ]
    if not stamps:
        return None
    return os.path.join(stamps_dir, random.choice(stamps))

def add_watermark(base_image_path, stamp_image_path, output_path, scale_factor=0.2):
    """
    Overlay the stamp image onto the base image at a random corner.
    
    Args:
        base_image_path: Path to the main generated image
        stamp_image_path: Path to the character stamp image
        output_path: Path to save the composite image
        scale_factor: How large the stamp should be relative to the base image (0.0 to 1.0)
    """
    try:
        base_img = Image.open(base_image_path).convert("RGBA")
        stamp_img = Image.open(stamp_image_path).convert("RGBA")
        
        # Calculate new size for the stamp
        base_width, base_height = base_img.size
        # Scale based on the smaller dimension of the base image
        target_dim = int(min(base_width, base_height) * scale_factor)
        
        # Keep aspect ratio of stamp
        stamp_width, stamp_height = stamp_img.size
        aspect_ratio = stamp_width / stamp_height
        
        if stamp_width > stamp_height:
            new_width = target_dim
            new_height = int(target_dim / aspect_ratio)
        else:
            new_height = target_dim
            new_width = int(target_dim * aspect_ratio)
            
        stamp_img = stamp_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Determine a random corner (0: top-left, 1: top-right, 2: bottom-left, 3: bottom-right)
        margin = int(min(base_width, base_height) * 0.05) # 5% margin
        corner = random.randint(0, 3)
        
        if corner == 0:
            pos = (margin, margin)
        elif corner == 1:
            pos = (base_width - new_width - margin, margin)
        elif corner == 2:
            pos = (margin, base_height - new_height - margin)
        else:
            pos = (base_width - new_width - margin, base_height - new_height - margin)
            
        # Create a new transparent image the size of the base image
        composite = Image.new("RGBA", base_img.size, (0, 0, 0, 0))
        composite.paste(base_img, (0, 0))
        # Use the stamp image as its own mask for transparency
        composite.paste(stamp_img, pos, mask=stamp_img)
        
        # Convert back to RGB if saving as JPG, otherwise keep RGBA for PNG
        if output_path.lower().endswith(('.jpg', '.jpeg')):
            composite = composite.convert("RGB")
            composite.save(output_path, quality=95)
        else:
            composite.save(output_path)
            
        print(f"Successfully added stamp to: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error adding stamp to image: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a random character stamp to an image.")
    parser.add_argument("input_image", help="Path to the original generated image")
    parser.add_argument("output_image", help="Path to save the stamped image")
    parser.add_argument("--stamps_dir", default=r"C:\Users\杢之助\2nd-Brain\00_システム\03_Assets\Stamps", 
                        help="Directory containing the character stamps")
    parser.add_argument("--scale", type=float, default=0.2, 
                        help="Scale factor for the stamp (default: 0.2)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_image):
        print(f"Error: Input image not found: {args.input_image}")
        sys.exit(1)
        
    if not os.path.exists(args.stamps_dir):
        print(f"Error: Stamps directory not found: {args.stamps_dir}")
        sys.exit(1)
        
    stamp_path = get_random_stamp(args.stamps_dir)
    if not stamp_path:
        print(f"Error: No valid images found in {args.stamps_dir}")
        sys.exit(1)
        
    print(f"Selected stamp: {stamp_path}")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(args.output_image)), exist_ok=True)
    
    success = add_watermark(args.input_image, stamp_path, args.output_image, args.scale)
    if not success:
        sys.exit(1)
