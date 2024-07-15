from PIL import Image
import sys
import os

# Disable DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None

def remove_black_border(input_image_path, output_image_path):
    # Open the image
    img = Image.open(input_image_path)
    img = img.convert("RGB")
    img_data = img.load()

    # Get the image size
    width, height = img.size

    # Define the coordinates for the cropping box
    left, top, right, bottom = 0, 0, width, height

    # Find top border
    for y in range(height):
        if any(img_data[x, y] != (0, 0, 0) for x in range(width)):
            top = y
            break

    # Find bottom border
    for y in range(height - 1, -1, -1):
        if any(img_data[x, y] != (0, 0, 0) for x in range(width)):
            bottom = y + 1
            break

    # Find left border
    for x in range(width):
        if any(img_data[x, y] != (0, 0, 0) for y in range(height)):
            left = x
            break

    # Find right border
    for x in range(width - 1, -1, -1):
        if any(img_data[x, y] != (0, 0, 0) for y in range(height)):
            right = x + 1
            break

    # Crop the image
    cropped_img = img.crop((left, top, right, bottom))

    # Save the new image
    cropped_img.save(output_image_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_black_border.py <input_image_path> <output_image_path>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    remove_black_border(input_image_path, output_image_path)
    print(f"Saved the image without black borders to {output_image_path}")
