from PIL import Image
import os

# Define the directory where the images are stored and where the printable directory is located
image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'finalized')
image_dir = os.path.normpath(image_dir)  # Normalize the path
printable_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'printable')
printable_dir = os.path.normpath(printable_dir)  # Normalize the path


def create_printable_sheet(card_files, sheet_number):
    # Create a new blank image with the dimensions of an A4 paper (2480x3508 pixels at 300 DPI)
    a4_img = Image.new('RGB', (2480, 3508), (255, 255, 255))  # White background

    # Define the size of each card (750x1050 pixels at 300 DPI)
    card_size = (750, 1050)

    # Calculate the spacing between cards
    x_spacing = (2480 - (3 * card_size[0])) // 4
    y_spacing = (3508 - (3 * card_size[1])) // 4

    # Loop through each card file and paste it onto the new image
    for i, card_file in enumerate(card_files):
        with Image.open(os.path.join(image_dir, card_file)) as card_img:
            # Resize the card image if necessary
            card_img = card_img.resize(card_size, Image.LANCZOS)

            # Calculate the position to paste the card image
            x_position = x_spacing + (i % 3) * (card_size[0] + x_spacing)
            y_position = y_spacing + (i // 3) * (card_size[1] + y_spacing)

            # Paste the card image onto the new image
            a4_img.paste(card_img, (x_position, y_position))

    # Ensure the 'printable' sub-directory exists
    os.makedirs(printable_dir, exist_ok=True)

    # Save the new image to a file in the 'printable' sub-directory
    a4_img.save(f'{printable_dir}/cards_sheet_{sheet_number}.png')


def main():
    # Get a list of all PNG files in the image directory
    png_files = [f for f in os.listdir(image_dir) if f.endswith('.png') and os.path.isfile(os.path.join(image_dir, f))]

    # Sort the list of files to ensure consistent ordering
    png_files.sort()

    # Group the files into sets of 9 (or fewer for the last group if necessary)
    grouped_files = [png_files[i:i + 9] for i in range(0, len(png_files), 9)]

    # Create a printable sheet for each group of 9 cards
    for i, group in enumerate(grouped_files):
        create_printable_sheet(group, sheet_number=i + 1)


if __name__ == "__main__":
    main()
