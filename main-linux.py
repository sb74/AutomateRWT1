#!/usr/bin/env python3
import os
from PIL import Image


def process_images(orig_folder, new_folder):
    """
    Converts images to JPEG and rotates/resizes.
    """
    size = (128, 128)
    deg = -90
    convert_type = ".jpeg"

    # Iterate through directory and create Pillow JPEG image objects.
    for root, dirs, files in os.walk(orig_folder):
        for file in files:
            # Create image object.
            image_path = os.path.join(orig_folder, file)
            im = Image.open(image_path)

            # Rotate, convert input image, and save in new location.
            new_path = os.path.join(new_folder, file + convert_type)
            im.rotate(deg).convert("RGB").resize(size).save(new_path)

    return


if __name__ == '__main__':
    # Linux home directory.
    home = os.path.expanduser("~")

    origin = home + r"/images"
    new = r"/opt/icons/"

    process_images(origin, new)
