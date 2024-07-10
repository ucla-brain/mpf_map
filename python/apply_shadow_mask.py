import os
import sys
from PIL import Image, ImageEnhance
from tqdm import tqdm

def apply_shadow_mask(image_path, output_path):
    # Open the image
    image = Image.open(image_path).convert("RGBA")

    # Split the image into RGBA channels
    r, g, b, a = image.split()

    # Create a shadow mask by darkening the RGB channels
    enhancer = ImageEnhance.Brightness(image)
    dark_image = enhancer.enhance(0.3)  # Adjust the factor to make it darker or lighter

    # Combine the darkened image with the original alpha channel
    shadowed_image = Image.merge("RGBA", (dark_image.split()[0], dark_image.split()[1], dark_image.split()[2], a))

    # Save the result
    shadowed_image.save(output_path)

def process_images(input_folder):
    # Remove all "_shadow.png" images in the folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('_shadow.png'):
            os.remove(os.path.join(input_folder, filename))

    # Get a list of all PNG files in the input folder
    files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png') and not f.lower().endswith('_shadow.png')]

    # Iterate over all files with a progress bar
    for filename in tqdm(files, desc="Processing images"):
        # Construct the full input path
        input_path = os.path.join(input_folder, filename)
        
        # Construct the output path
        base, ext = os.path.splitext(filename)
        output_filename = f"{base}_shadow{ext}"
        output_path = os.path.join(input_folder, output_filename)
        
        # Apply the shadow mask
        apply_shadow_mask(input_path, output_path)

if __name__ == "__main__":
    # Ensure an input folder is provided
    if len(sys.argv) != 2:
        print("Usage: python apply_shadow_mask.py <input_folder>")
        sys.exit(1)

    # Get the input folder from command line arguments
    input_folder = sys.argv[1]

    # Process the images in the specified folder
    process_images(input_folder)
