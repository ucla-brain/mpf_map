import os
import sys
from PIL import Image, ImageFile
from tqdm import tqdm
import argparse

# Disable DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None

def convert_tiff_to_png_file(tiff_path, png_path):
    with Image.open(tiff_path) as img:
        img = img.convert("RGBA")  # Ensure image is in RGBA mode
        datas = img.getdata()

        new_data = []
        for item in datas:
            # Change all white (also shades of whites)
            # pixels to transparent
            if item[:3] == (255, 255, 255):
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(png_path, 'PNG')

def convert_tiff_to_png_folder(input_folder):
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
        convert_tiff_to_png_file(tiff_path, png_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert TIFF images to PNG format.")
    parser.add_argument("input_folder", nargs="?", help="The folder containing TIFF files to convert.")
    parser.add_argument("-i", "--input", help="The input TIFF file to convert.")
    parser.add_argument("-o", "--output", help="The output PNG file path.")

    args = parser.parse_args()

    if args.input and args.output:
        if os.path.isfile(args.input) and (args.input.lower().endswith('.tiff') or args.input.lower().endswith('.tif')):
            convert_tiff_to_png_file(args.input, args.output)
        else:
            print(f"Error: {args.input} is not a valid TIFF file.")
    elif args.input_folder:
        if os.path.isdir(args.input_folder):
            convert_tiff_to_png_folder(args.input_folder)
        else:
            print(f"Error: {args.input_folder} is not a valid directory.")
    else:
        print("Usage:")
        print("  python convert_tiff_to_png.py <input_folder>")
        print("  python convert_tiff_to_png.py -i <input_file.tiff> -o <output_file.png>")
