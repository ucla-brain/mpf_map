import os
import sys
import shutil
import json
from tqdm import tqdm
import re
import itertools

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
    index = 1
    tracerCategory = {'phal':'anterograde','aav-rfp':'anterograde','fg':'retrograde','ctb':'retrograde'}
    for root, _, files in os.walk(output_folder):
        sorted_image_list = []            
        image_list = []
        existing_ara_levels = []      
        folder_name = ''
        tracer = ''
        injectionSite = ''
        for file in files:
            if file.lower().endswith('_15pct.png'):

                # Extract the matched group
                match = re.search(r'-Coronal-(\d+)_', file)
                ara_level = -1
                if match: # ARA
                    ara_level = str(int(match.group(1)))
                    href = os.path.join(root, file).replace('/Users/seitayamashita/Documents/git_next/mpf_map','')
                    image_list.append({
                        "index": int(ara_level),
                        "href": href,
                        "atlasLevel": f'ARA {ara_level}'
                    })
                else: # Images
                    folder_name = os.path.relpath(root, output_folder).replace("\\", "/")

                    # Extracting ara_level from filename                    
                    filename_parts = file.split('_')

                    # tracer
                    if len(filename_parts) == 8:
                        tracer = filename_parts[5]
                        injectionSite = filename_parts[4]
                    if len(filename_parts) == 9:
                        tracer = filename_parts[6]
                        injectionSite = f'{filename_parts[4]}-{filename_parts[5]}'

                    ara_level = filename_parts[-2] if len(filename_parts) >= 2 else ""
                    ara_level = ara_level.replace('ara','')
                    href = os.path.join(root, file).replace('/Users/seitayamashita/Documents/git_next/mpf_map','')
                    image_list.append({
                        "index": int(ara_level),
                        "href": f'/mpf{href}',
                        "atlasHref": f'/mpf/static/ara/ARA-Coronal-{ara_level:03}_full_labels_15pct.png',
                        "atlasLevel": f'ARA {ara_level:03}',
                        "folderName": folder_name,
                        "tracer": tracer,
                        "tracerCategory": tracerCategory[tracer],
                        "injectionSite": injectionSite
                    })
                    existing_ara_levels.append(int(ara_level))


        # Adding blank data for missing ARA levels
        for ara_level in range(1, 133):
            if ara_level not in existing_ara_levels:
                image_list.append({
                    "index": ara_level,
                    "href": f'/mpf/static/ara/ARA-Coronal-{ara_level:03}_full_labels_15pct_shadow.png',
                    "atlasLevel": f'ARA {ara_level:03}',
                    "folderName": folder_name,
                    "tracer": '',
                    "tracerCategory": '',
                    "injectionSite": ''
                })
        sorted_image_list = sorted(image_list, key=lambda x: x["index"])

        if sorted_image_list and folder_name != '':
            data[folder_name] = sorted_image_list            
            # data[f'image{index}'] = sorted_image_list            
            # index = index + 1


        # Group sorted_image_list by folder_name
        # for folder_name, group in itertools.groupby(sorted_image_list, key=lambda x: x["folderName"]):
        #     sorted_group = sorted(group, key=lambda x: (x["tracerCategory"], x["injectionSite"]))
        #     if folder_name != '':
        #         data[folder_name] = sorted_group



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
            # copy_png_images(input_folder, output_folder)
            json_file_path = os.path.join(output_folder, 'images.json')
            generate_json(output_folder, json_file_path)
        else:
            print(f"Error: {input_folder} is not a valid directory.")
