import os
import zipfile
from pathlib import Path


def backupToZip(folder):
    folder = os.path.abspath(folder)

    number = 1

    while True:
        zip_file_name = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zip_file_name):
            break
        number += 1

    print(f"Creating a zipfile: {zip_file_name}")

    with zipfile.ZipFile(zip_file_name, "w") as backupZip:
        for foldername, subfolders, filenames in os.walk(folder):
            print(f"Adding files in {foldername}...")
            backupZip.write(foldername)

            for filename in filenames:
                new_base = os.path.basename(folder) + "_"
                if filename.startswith(new_base) and filename.endswith(".zip"):
                    continue
                backupZip.write(Path(foldername) / filename)

    print("Done.")


if __name__ == "__main__":
    backupToZip(Path(__file__).parent / "files")
