import os
import shutil


CWD = os.getcwd()


if __name__ == "__main__":
    files_to_find = input("Input which extension do you want to use: .")

    if "copied" not in os.listdir(CWD):
        os.mkdir("copied")

    for foldername, subfolders, filenames in os.walk(CWD):
        to_copy = [filename for filename in filenames if filename.endswith(f".{files_to_find}")]

        for file_to_copy in to_copy:
            shutil.copy(os.path.join(foldername, file_to_copy), os.path.join(CWD, "copied"))
