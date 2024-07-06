import os
import sys
import shutil
import json
from tqdm import tqdm

def copy_png_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Gather all PNG files
    png_files = []
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('_15pct.png'):
                relative_path = os.path.relpath(root, input_folder)
                png_files.append((root, file, relative_path))

    total_files = len(png_files)
    print(f"Total PNG files to copy: {total_files}")

    # Copy files with progress bar and maintain folder structure
    for root, file, relative_path in tqdm(png_files, desc="Copying PNG files", unit="file"):
        png_path = os.path.join(root, file)
        destination_dir = os.path.join(output_folder, relative_path)
        new_png_path = os.path.join(destination_dir, file)

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        shutil.copy2(png_path, new_png_path)
    
    print(f"Copied images have been saved to {output_folder}")
    
def generate_json(output_folder, json_file_path):
    data = {}
    
    for root, _, files in os.walk(output_folder):
        folder_name = os.path.relpath(root, output_folder).replace("\\", "/")
        image_list = []
        for file in files:
            if file.lower().endswith('_15pct.png'):
                # Extracting ara_level from filename
                filename_parts = file.split('_')
                ara_level = filename_parts[-2] if len(filename_parts) >= 2 else ""
                ara_level_formatted = f"ARA {ara_level[3:]}" if ara_level.startswith("ara") else ara_level
                
                href = os.path.join(root, file).replace(output_folder, '').lstrip(os.sep).replace("\\", "/")
                image_list.append({
                    "href": href,
                    "atlasLevel": ara_level_formatted
                })
        
        if image_list:
            data[folder_name] = image_list

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"JSON file has been created at {json_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_folder>")
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        if os.path.isdir(input_folder):
            copy_png_images(input_folder, output_folder)
            json_file_path = os.path.join(output_folder, 'images.json')
            generate_json(output_folder, json_file_path)
        else:
            print(f"Error: {input_folder} is not a valid directory.")
