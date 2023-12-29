import re


def reStrip(text):
    stripper = re.compile(r'^\s*(\S*)\s*$')
    return stripper.search(text).groups()[0]


if __name__ == '__main__':
    text = input('Enter a string to be stripped: ')
    print(f"Original string: {text}\nStripped string: {reStrip(text)}")