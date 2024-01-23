import os

import requests
import pyinputplus
from bs4 import BeautifulSoup


if __name__ == "__main__":
    print("Getting the user data...")
    search_term = input("Enter the search term for images: ")
    quantity = pyinputplus.inputNum("Enter how many pictures to download: ")

    print("Formatting the user data...")
    formatted_term = search_term.replace(" ", "%20")
    search_term = search_term.replace(" ", "_")
    website = f"https://flickr.com/search/?text={formatted_term}"

    print("Accessing the website...")
    response = requests.get(website)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    print("Finding images...")
    images = soup.find_all("img")

    if len(images) < quantity:
        quantity = len(images)

    folder_path = f"./{search_term}"

    print("Creating folder...")
    if search_term not in os.listdir("./"):
        os.mkdir(folder_path)

    maximum_index = len(os.listdir(folder_path))

    print("Downloading images...")
    for index, image in enumerate(images[:quantity]):
        if img_url := image.get("src"):

            img_url = "https:" + img_url

            response = requests.get(img_url)

            if response.status_code == 200:
                with open(f"{folder_path}/img_{index+maximum_index+1}.jpg", "wb") as f:
                    f.write(response.content)

    print(f"Downloaded {len(os.listdir(folder_path))} image successfully.")
