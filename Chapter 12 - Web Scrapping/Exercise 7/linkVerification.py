import re
import sys

import requests
from bs4 import BeautifulSoup


URL_COMPILER = re.compile(r"http(|s)://.+\..+\..+")

if __name__ == "__main__":
    website = input("Enter the URL where you want to seach for links: ")
    not_found = 0

    response = requests.get(website)

    if response.status_code != 200:
        print("Invalid URL")
        sys.exit()

    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a"):

        current_link = link.get("href")

        if current_link[0] == "/":
            current_link = website + current_link

        if not URL_COMPILER.search(current_link):
            continue

        response = requests.get(current_link)
        print(f"currently validating link: {current_link}")

        if response.status_code == 404:
            print(f"Webpage not found! 404 error - {current_link}")
            not_found += 1
    else:
        print(f"Searched through all the links\nTotal 404 errors: {not_found}")
