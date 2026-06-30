import os
import shutil
from PIL import Image

# Copy from brain folder to images folder, resize, and convert to WebP
brain_dir = r"C:\Users\manu1\.gemini\antigravity-ide\brain\472e8c5c-43cd-4f41-8c39-de6b5166d623"
out_dir = r"c:\Users\manu1\OneDrive\Desktop\Wearable Technology\images"

files_to_convert = {
    "product_smartwatch_elite_1782733217342.png": "product-smartwatch-elite.webp",
    "product_smartwatch_lite_1782733229783.png": "product-smartwatch-lite.webp"
}

for src_name, dst_name in files_to_convert.items():
    src_path = os.path.join(brain_dir, src_name)
    dst_path = os.path.join(out_dir, dst_name)
    
    if os.path.exists(src_path):
        with Image.open(src_path) as img:
            # Resize
            max_width = 500
            ratio = 1
            if img.width > max_width:
                ratio = max_width / img.width
            new_size = (int(img.width * ratio), int(img.height * ratio))
            
            img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Save as WebP
            img_resized.save(dst_path, "WEBP", quality=80)
            
        size_kb = os.path.getsize(dst_path) / 1024
        print(f"Saved {dst_name}: {size_kb:.1f} KB")
    else:
        print(f"Not found: {src_path}")
