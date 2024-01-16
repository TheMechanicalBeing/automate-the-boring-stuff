import webbrowser
from sys import argv

import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    print("Looking for search results...")

    keywords = argv[1:]

    print("Searching...")

    response = requests.get("https://pypi.org/search/?q=" + " ".join(keywords))
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    linkElems = soup.select(".package-snippet")

    openNum = min(5, len(linkElems))
    for i in range(openNum):
        toOpen = "https://pypi.org" + linkElems[i].get("href")
        print(f"Opening: {toOpen}")
        webbrowser.open(toOpen)
