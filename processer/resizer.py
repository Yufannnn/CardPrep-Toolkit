import os

from PIL import Image

image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'raw')
image_dir = os.path.normpath(image_dir)  # Normalize the path


def resize_images_to_poker_card_size():
    # Loop through each file in the image directory
    for filename in os.listdir(image_dir):
        # Get the full path of the file
        filepath = os.path.join(image_dir, filename)

        # Skip directories and non-PNG files
        if os.path.isdir(filepath) or not filename.endswith('.png'):
            continue

        try:
            # Open the image file
            with Image.open(filepath) as img:
                # Resize the image to poker card size (750x1050 pixels)
                resized_img = img.resize((750, 1050), Image.LANCZOS)

                # Save the resized image back to the file
                resized_img.save(filepath)
        except OSError as e:
            print(f"Failed to process {filename}: {e}")


if __name__ == "__main__":
    resize_images_to_poker_card_size()
