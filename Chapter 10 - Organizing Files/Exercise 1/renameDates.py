import os
import shutil
import re
from pathlib import Path


if __name__ == "__main__":

    datePattern = re.compile("""^(.*?)   # Text before date
    ((?:0|1)?\d-)                                 # One or two digits from the month
    ((?:0|1|2|3)?\d-)                             # One or two digits from the day
    ((?:19|20)\d\d)                               # Four digits from the year
    (.*?)$                                      # Text after date
    """, re.VERBOSE)

    base_directory = Path(__file__).parent / "files"
    files_with_date = [filename for filename in os.listdir(base_directory) if datePattern.search(filename)]

    for file in files_with_date:
        divided = datePattern.search(file).groups()
        new_filename = "".join(divided[0] + divided[2] + divided[1] + divided[3] + divided[4])
        shutil.move(base_directory / file, base_directory / new_filename)
