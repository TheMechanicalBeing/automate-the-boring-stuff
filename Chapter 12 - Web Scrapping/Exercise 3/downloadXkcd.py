import os

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://xkcd.com"

    os.makedirs("xkcd", exist_ok=True)
    while not url.endswith("#"):
        print("Downloading page...")
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        comicElem = soup.select("#comic img")
        if not comicElem:
            print("Could not find comic image.")
        else:
            comicUrl = "https:" + comicElem[0].get("src")
            print(f"Downloading image {comicUrl}")
            response = requests.get(comicUrl)
            response.raise_for_status()

            with open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb") as imageFile:
                for chunk in response.iter_content(100000):
                    imageFile.write(chunk)

        prevLink = soup.select("a[rel=prev]")[0]
        url = "https://xkcd.com" + prevLink.get("href")

    print("Done.")
