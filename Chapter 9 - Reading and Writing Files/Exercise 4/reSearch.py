import re
from pathlib import Path

if __name__ == "__main__":
    pattern = input("Enter a RegEx pattern: ")
    compiler = re.compile(pattern)

    texts_directory = Path(__file__).parent / "texts"
    text_files = texts_directory.glob("*.txt")
    matches = []

    for text_file in text_files:
        with open(text_file) as f:
            for line in f.readlines():
                matches.extend(compiler.findall(line))

    print(matches)
