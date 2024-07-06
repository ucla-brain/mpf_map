import os
import sys
from PIL import Image
from tqdm import tqdm

# Disable DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None

def resize_png_images(input_folder):
    # Gather all PNG files
    png_files = []
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('.png'):
                png_files.append((root, file))

    total_files = len(png_files)
    print(f"Total PNG files to process: {total_files}")

    # Remove existing _15pct.png files before processing
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('_15pct.png'):
                os.remove(os.path.join(root, file))
                print(f"Removed existing file: {file}")

    # Process and resize files with progress bar
    for root, file in tqdm(png_files, desc="Processing PNG files", unit="file"):
        png_path = os.path.join(root, file)
        new_filename = os.path.splitext(file)[0] + '_15pct.png'
        new_png_path = os.path.join(root, new_filename)

        with Image.open(png_path) as img:
            width, height = img.size
            new_size = (int(width * 0.15), int(height * 0.15))
            resized_img = img.resize(new_size, Image.LANCZOS)
            resized_img.save(new_png_path, 'PNG')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python resize_png_images.py <input_folder>")
    else:
        input_folder = sys.argv[1]
        if os.path.isdir(input_folder):
            resize_png_images(input_folder)
        else:
            print(f"Error: {input_folder} is not a valid directory.")
