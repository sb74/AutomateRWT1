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
    for file in os.scandir(orig_folder):
        if file.is_file():
            # Create image object.
            image_path = os.path.join(file)
            im = Image.open(image_path)

            # Get image name and extension from DirEntry object.
            path, image = os.path.split(file)
            image_name, ext = image.split(".")

            # Rotate, convert input image, and save in new location.
            new_path = os.path.join(new_folder, image_name + convert_type)
            im.rotate(deg).convert("RGB").resize(size).save(new_path)

    return


if __name__ == '__main__':
    origin = r"C:\Users\sbran\Desktop\Tiffs"
    new = r"C:\Users\sbran\Desktop\Tiffs\New"

    process_images(origin, new)
