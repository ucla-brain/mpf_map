import os
import sys
from PIL import Image
from tqdm import tqdm

# Disable DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None

def tint_non_transparent(image, tint_color):
    """
    Tints the non-transparent parts of an image with the given color.
    
    Args:
        image (PIL.Image.Image): The input image to tint.
        tint_color (tuple): The tint color as an (R, G, B) tuple.
    
    Returns:
        PIL.Image.Image: The tinted image.
    """
    # Convert the image to RGBA if it is not already
    image = image.convert("RGBA")

    # Extract the alpha channel as a mask
    alpha = image.split()[3]

    # Create a solid color image with the tint color
    solid_color = Image.new('RGBA', image.size, tint_color + (255,))

    # Composite the tint color onto the image using the alpha mask
    tinted_image = Image.composite(solid_color, image, alpha)

    return tinted_image

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

            injectionSite = ''
            if len(filename_parts) == 9:
                injectionSite = filename_parts[5]
            elif len(filename_parts) == 8:
                injectionSite = filename_parts[4]

            # atlas image path pattern
            atlas_image_path = os.path.join(input_atlas_folder, f'ARA-Coronal-{level.zfill(3)}_full_labels_15pct.png')
            
            if os.path.exists(atlas_image_path):
                with Image.open(atlas_image_path) as atlas_img:
                    # Ensure both images have the same size
                    atlas_img = atlas_img.resize(img.size, Image.LANCZOS)

                    # Tint the non-transparent parts of the image
                    tint_color = (255,255,255)
                    if injectionSite == 'ILA':
                        tint_color = (56, 127, 185)
                    elif injectionSite == 'PL':
                        tint_color = (255, 127, 0)
                    elif injectionSite == 'deep':
                        tint_color = (76, 175, 74)
                    elif injectionSite == 'DP':
                        tint_color = (228, 26, 28)
                    elif injectionSite == 'ACAd':
                        tint_color = (166, 86, 41)
                    elif injectionSite == 'ACAv':
                        tint_color = (152, 79, 163)

                    img = tint_non_transparent(img, tint_color)

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
