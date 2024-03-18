import os
from PIL import Image


SQUARE_FIT_SIZE = 700
LOGO_FILENAME = "catlogo.png"


if __name__ == "__main__":
    logo_image_object = Image.open(LOGO_FILENAME)
    logo_width, logo_height = logo_image_object.size
    logo_image_object = logo_image_object.resize((logo_width, logo_height))

    os.makedirs("withLogo", exist_ok=True)
    for filename in os.listdir("."):
        if not (filename.endswith(".png") or filename.endswith(".jpg")) or filename == LOGO_FILENAME:
            continue

        image_object = Image.open(filename)
        width, height = image_object.size

        if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
            if width > height:
                height = int((SQUARE_FIT_SIZE / width) * height)
                width = SQUARE_FIT_SIZE
            else:
                width = int((SQUARE_FIT_SIZE / height) * width)
                height = SQUARE_FIT_SIZE

        print(f"Resizing image {filename} to {width}x{height}")
        image_object = image_object.resize((width, height))

        print(f"Adding logo to {filename}")
        image_object.paste(logo_image_object, (width - logo_width, height - logo_height))

        image_object.save(os.path.join("withLogo", filename))
