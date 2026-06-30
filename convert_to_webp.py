import os
from PIL import Image

image_dir = r"c:\Users\manu1\OneDrive\Desktop\Wearable Technology\images"

for file in os.listdir(image_dir):
    if file.endswith(".jpg"):
        jpg_path = os.path.join(image_dir, file)
        webp_path = os.path.join(image_dir, file.replace(".jpg", ".webp"))
        
        # Convert to WebP
        with Image.open(jpg_path) as img:
            img.save(webp_path, "WEBP", quality=80)
        
        # Get size
        size_kb = os.path.getsize(webp_path) / 1024
        print(f"Converted {file} to WebP: {size_kb:.1f} KB")
        
        # Delete original JPG
        os.remove(jpg_path)
