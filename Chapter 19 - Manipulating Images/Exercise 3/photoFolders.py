import os

from PIL import Image, UnidentifiedImageError


if __name__ == "__main__":
    print("Photo folders\n-------------------------")
    for foldername, subfolders, filenames in os.walk("C:\\"):
        photo_quantity = 0
        not_photos_quantity = 0

        for filename in filenames:
            if not (filename.lower().endswith(".png") or filename.lower().endswith("jpg")):
                not_photos_quantity += 1
                continue

            try:
                image_object = Image.open(os.path.join(foldername, filename))
            except UnidentifiedImageError:
                continue
            except ValueError:
                continue

            width, height = image_object.size

            if width < 500 or height < 500:
                not_photos_quantity += 1
            else:
                photo_quantity += 1

        if photo_quantity > not_photos_quantity:
            print(foldername)
