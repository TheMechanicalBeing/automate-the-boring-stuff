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


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    border = ("+" + "-" * 7) * 2 + "+"
    empty_row = ("|" + " " * 7) * 2 + "|"

    print(border)

    for i in range(3):
        print(empty_row)
        print(empty_row)
        print(border)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    pass


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    pass


def draw_move(board):
    # The function draws the computer's move and updates the board.
    pass


print("STARTS HERE")
display_board(1)