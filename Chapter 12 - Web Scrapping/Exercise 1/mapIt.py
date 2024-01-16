import webbrowser
from sys import argv

import pyperclip


if __name__ == '__main__':

    if len(argv) > 1:
        address = " ".join(argv[1:])
    else:
        address = pyperclip.paste()

    webbrowser.open(f"https://www.google.com/maps/place/{address}")
