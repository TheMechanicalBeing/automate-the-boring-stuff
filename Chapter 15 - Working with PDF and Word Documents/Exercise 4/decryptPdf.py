import sys

import PyPDF2

WORDS = []

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decryptPdf.py <filename.pdf>")
        exit()

    # Collect the words
    with open("dictionary.txt") as f:
        for word in f:
            WORDS.append(word.strip())

    filename = sys.argv[1]

    # Checking if file exists
    try:
        with open(filename, "rb") as f:
            reader = PyPDF2.PdfReader(f)
    except FileNotFoundError:
        print(f"Could not find specified file: {filename}")
        exit()

    # Checking encryption
    # Brute-force attack implementation
    if reader.is_encrypted:
        for word in WORDS:
            if reader.decrypt(word) or reader.decrypt(word.lower()):
                print(f"Decryption password was: {word}")
                break
        else:
            print("Decryption failed.")

    else:
        print("File is not encrypted.")
