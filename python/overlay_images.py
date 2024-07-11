import os
import sys
from PIL import Image, ImageEnhance
from tqdm import tqdm

# Disable DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None

def overlay_images(input_folder, input_atlas_folder):
    # Gather all PNG files
    png_files = []
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('_15pct.png'):
                png_files.append((root, file))

    total_files = len(png_files)
    print(f"Total PNG files to process: {total_files}")

    # Process and overlay images with progress bar
    for root, file in tqdm(png_files, desc="Processing PNG files", unit="file"):
        png_path = os.path.join(root, file)
        new_filename = os.path.splitext(file)[0] + '_overlayed.png'
        new_png_path = os.path.join(root, new_filename)

        with Image.open(png_path) as img:
            # Extracting level from filename
            filename_parts = file.split('_')
            level = filename_parts[-2] if len(filename_parts) >= 2 else ""
            level = level.replace('ara','')

            # atlas image path pattern
            atlas_image_path = os.path.join(input_atlas_folder, f'ARA-Coronal-{level.zfill(3)}_full_labels_15pct.png')
            
            if os.path.exists(atlas_image_path):
                with Image.open(atlas_image_path) as atlas_img:
                    # Ensure both images have the same size
                    atlas_img = atlas_img.resize(img.size, Image.LANCZOS)

                    # Overlay images
                    overlayed_image = Image.alpha_composite(atlas_img.convert("RGBA"), img.convert("RGBA"))

                    # Save the new image
                    overlayed_image.save(new_png_path, 'PNG')
            else:
                print(f"Atlas image {atlas_image_path} not found. Skipping.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python overlay_images.py <input_folder> <input_atlas_folder>")
    else:
        input_folder = sys.argv[1]
        input_atlas_folder = sys.argv[2]
        if os.path.isdir(input_folder) and os.path.isdir(input_atlas_folder):
            overlay_images(input_folder, input_atlas_folder)
        else:
            print(f"Error: {input_folder} or {input_atlas_folder} is not a valid directory.")
