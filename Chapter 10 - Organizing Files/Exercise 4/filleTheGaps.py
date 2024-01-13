import os
import re
import shutil


if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), "files")

    prefix = input("Input the prefix to fill in the gaps: ")

    generate_numeration = re.compile("(.*)(\d+)(|\..*)$")
    numerations = []
    key_part = []

    filenames = os.listdir(file_path)

    with_prefix = [filename for filename in filenames if filename.startswith(prefix)]

    for file_with_prefix in with_prefix:
        numerations.append(int(generate_numeration.search(file_with_prefix).groups()[1]))
        key_part.append(generate_numeration.search(file_with_prefix).groups())

    minimum = min(numerations)
    maximum = minimum + len(numerations)

    for i in range(minimum, maximum):
        new_filename = key_part[i-minimum][0] + f"{i}" + key_part[i-minimum][2]
        shutil.move(os.path.join(file_path, with_prefix[i-minimum]), os.path.join(file_path, new_filename))
