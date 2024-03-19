import os
from PIL import Image, ImageSequence

SQUARE_FIT_SIZE = 700
LOGO_FILENAME = "catlogo.png"

if __name__ == "__main__":
    logo_image_object = Image.open(LOGO_FILENAME)
    logo_width, logo_height = logo_image_object.size
    logo_image_object = logo_image_object.resize((logo_width, logo_height))

    os.makedirs("withLogo", exist_ok=True)
    for filename in os.listdir("."):
        if filename == LOGO_FILENAME or filename.split(".")[-1].lower() not in ["png", "jpg", "gif", "bmp"]:
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

        if logo_width * 2 > width:
            width = logo_width * 2
            height = int(height * logo_width * 2 / width)
        if logo_height * 2 > height:
            height = logo_height * 2
            width = int(width * logo_height * 2 / height)

        if filename.lower().endswith(".png") or filename.lower().endswith(".jpg"):
            print(f"Resizing image {filename} to {width}x{height}")
            image_object = image_object.resize((width, height))

            print(f"Adding logo to {filename}")
            image_object.paste(logo_image_object, (width - logo_width, height - logo_height))

            image_object.save(os.path.join("withLogo", filename))

        elif filename.lower().endswith(".gif"):
            modified_frames = []
            print(f"Resizing image {filename} to {width}x{height}")
            for frame in ImageSequence.Iterator(image_object):
                modified_frame = frame.copy().resize((width, height))
                modified_frame.paste(logo_image_object, (width - logo_width, height - logo_height))
                modified_frames.append(modified_frame)

            modified_frames[0].save(os.path.join("withLogo", filename), save_all=True,
                                    append_images=modified_frames[1:])
