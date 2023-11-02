import random
import os

# Define the directory where the images are stored
image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'finalized')
image_dir = os.path.normpath(image_dir)  # Normalize the path


def rename_files():
    # shuffle the files
    files = os.listdir(image_dir)
    random.shuffle(files)

    # Loop through each file in the image directory
    for filename in files:
        # Get the full path of the file
        filepath = os.path.join(image_dir, filename)

        # Skip directories and python files
        if os.path.isdir(filepath) or filename.endswith('.py'):
            continue

        # Rename the file with ascending index (e.g. card1.png, card2.png, card3.png, ...)
        index = 1
        while True:
            new_filepath = os.path.join(image_dir, f'Nul.{index}.png')
            if not os.path.exists(new_filepath):
                os.rename(filepath, new_filepath)
                break
            index += 1


# Call the functions
if __name__ == "__main__":
    rename_files()
