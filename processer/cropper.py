import os
from PIL import Image, ImageChops


# Function to trim the white margins
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -200)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


# Define the directory where the images are stored
image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'raw')
image_dir = os.path.normpath(image_dir)  # Normalize the path


def main():
    # Loop through each file in the image directory
    for filename in os.listdir(image_dir):
        # Get the full path of the file
        filepath = os.path.join(image_dir, filename)

        # Skip directories and non-PNG files
        if os.path.isdir(filepath) or not filename.endswith('.png'):
            continue

        # Open the image file
        with Image.open(filepath) as im:
            # Trim the white margins
            trimmed_im = trim(im)

            # If trimming was successful, save the trimmed image back to the file
            if trimmed_im:
                trimmed_im.save(filepath)


if __name__ == "__main__":
    main()
