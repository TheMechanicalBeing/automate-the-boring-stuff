import sys
import time

from selenium import webdriver


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python commandLineEmailer.py <email> *<text>")
        sys.exit()

    email_to_send = sys.argv[1]
    text_to_send = sys.argv[2:]

    with webdriver.Chrome() as browser:
        browser.get("https://mail.google.com")
        time.sleep(5)
