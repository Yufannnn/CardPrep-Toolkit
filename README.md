# Card Image Processing Toolkit

This project provides a set of tools for card enthusiasts to prepare card images for printing. Users can resize card images to standard poker card dimensions, rename files for easier management, arrange multiple cards on a single printable sheet, and trim unwanted white margins from card images. The tools use Python and leverage libraries such as Pillow and OpenCV for image processing tasks. Whether you are looking to print custom game cards or organize a collection of card images, this toolkit can simplify the preparation process.

## Features

- **Resizing**: Resize card images to standard poker card dimensions.
- **Renaming**: Rename files for easier management and organization.
- **Arranging**: Arrange multiple card images on a single sheet for easy printing.
- **Cropping**: Trim unwanted white margins from card images.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Pillow library for basic image processing tasks.
- OpenCV library for more advanced image processing tasks.

Install the necessary libraries using pip:

```bash
pip install Pillow opencv-python-headless
```

### Usage

1. Clone the repository to your local machine:
```bash
https://github.com/Yufannnn/CardPrep-Toolkit.git
cd card-image-processing-toolkit
```

2. Place your card images in the `raw` directory.

3. Run the scripts provided in the `processor` directory to process your images:
```bash
cd processor
python renamer.py
python cropper.py
python resizer.py
python concatenator.py
```

4. Check the `finalized` and `printable` directories for the processed images and printable sheets.

## Contributing

Feel free to fork the project, open issues, and submit pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
