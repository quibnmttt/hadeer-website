import os
from PIL import Image

def optimize_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                filepath = os.path.join(root, file)
                try:
                    with Image.open(filepath) as img:
                        # Convert RGBA to RGB if saving as JPEG
                        if img.mode in ("RGBA", "P") and file.lower().endswith(('.jpg', '.jpeg')):
                            img = img.convert("RGB")
                        
                        # Save with optimization
                        if file.lower().endswith('.png'):
                            img.save(filepath, optimize=True)
                        else:
                            img.save(filepath, quality=85, optimize=True)
                        print(f"Optimized: {filepath}")
                except Exception as e:
                    print(f"Error optimizing {filepath}: {e}")

if __name__ == "__main__":
    optimize_images("images")
