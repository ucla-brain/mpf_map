import os
import sys
from PIL import Image, ImageFile
from tqdm import tqdm

# Disable DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None

def convert_tiff_to_png(input_folder):
    # Count total number of TIFF files
    tiff_files = []
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('.tiff') or file.lower().endswith('.tif'):
                tiff_files.append((root, file))

    total_files = len(tiff_files)
    print(f"Total TIFF files to process: {total_files}")

    # Process and convert files with progress bar
    for root, file in tqdm(tiff_files, desc="Processing TIFF files", unit="file"):
        tiff_path = os.path.join(root, file)
        png_path = os.path.join(root, os.path.splitext(file)[0] + '.png')

        with Image.open(tiff_path) as img:
            img.save(png_path, 'PNG')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_tiff_to_png.py <input_folder>")
    else:
        input_folder = sys.argv[1]
        if os.path.isdir(input_folder):
            convert_tiff_to_png(input_folder)
        else:
            print(f"Error: {input_folder} is not a valid directory.")
