import os
import sys
import subprocess
from tqdm import tqdm
import cv2

# outspector module
external_repo_path = '/ifshome/syamashi/Documents/gittest/outspector/src/'
sys.path.append(external_repo_path)

from cell_segmentation import CellSegmentation

# List of partial folder names of retrogrades
partial_folder_names = [
    "SW110614-01B-ACAd/5-ctb",
    "SW120530-03A-ACAd/3-fg",
    "SW170420-04A-ACAd/3-fg",
    "SW110321-04B-ACAv/5-ctb",
    "SW110606-01A-ACAv/5-ctb",
    "SW120403-02A-ACAv/5-ctb",
    "SW151027-02B-DP/4-ctb",
    "SW160120-01B-DP/5-ctb",
    "SW160120-03A-DP/5-ctb",
    "SW170420-04A-DP_deep/5-ctb",
    "SW120404-02A-ILA/5-ctb",
    "SW120404-04A-ILA/5-ctb",
    "SW120404-01A-PL/3-fg",
    "SW120404-02A-PL/3-fg"
]

def should_process(file_path, partial_folder_names):
    for partial_name in partial_folder_names:
        if partial_name in file_path:
            return True
    return False

# python batch_cell_segmentation.py /panfs/dong/mpf_map/originals/ /panfs/dong/mpf_map/output/
def main():
    if len(sys.argv) != 3:
        print("Usage: python batch_cell_segmentation.py <input_dir> <output_dir>")        
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    image_files = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.tif', '.tiff')):
                file_path = os.path.join(root, file)
                if should_process(file_path, partial_folder_names):
                    image_files.append(file_path)

    with tqdm(total=len(image_files), desc="Processing images") as pbar:
        for file in image_files:
            relative_path = os.path.relpath(file, input_dir)
            output_path = os.path.join(output_dir, relative_path)
            output_dir_path = os.path.dirname(output_path)
            if not os.path.exists(output_dir_path):
                os.makedirs(output_dir_path)

            # Reads image, and invert pixel intensity: 255 - image
            image = CellSegmentation.load_img(file)
            # Draw circle centered at each single pixel. `r` controls radius.
            reconstructed_image = CellSegmentation.reconstruct_degenerated(image, r=15)

            # Invert the reconstructed image (black/white)
            inverted_image = cv2.bitwise_not(reconstructed_image)

            # Save image. The image is gray (single channel), white pixels are cells.
            # cv2.imwrite(output_path, reconstructed_image)
            # Save the inverted image
            cv2.imwrite(output_path, inverted_image)

            pbar.update(1)



if __name__ == "__main__":
    main()
