import random
import time
import sys


def print_box(b, h, w):  # Iterating through values of box to print whole list
    for row in range(h):
        for column in range(w):
            print(b[row][column], end="")
        print()


def change_box(b, h, w):  # Implementing main logic of conway
    for row in range(h):  # Iterating through values of list
        for column in range(w):

            neighbors = ((row-1, column-1), (row, column-1), (row+1, column-1),  # Defining neighbour values
                         (row-1, column), (row+1, column),
                         (row-1, column+1), (row, column+1), (row+1, column+1))

            tracker = 0
            for neighbor in neighbors:
                try:
                    if neighbor[0] < 0 or neighbor[1] < 0:  # The negative indexes must be filtered
                        continue
                    if box[neighbor[0]][neighbor[1]] == "#":  # Checking if neighbor is alive
                        tracker += 1
                    if tracker > 3:
                        break
                except IndexError:  # IndexError will happen when you deal with edge-indexed values
                    pass

            if b[row][column] == " " and tracker == 3:  # If 3 neighbors are alive and value is not alive it must become alive
                b[row][column] = "#"
            if b[row][column] == "#" and tracker not in [2, 3]:  # If 2 or 3 neighbors are alive and value is alive it must still be alive
                b[row][column] = " "
    return b


if __name__ == "__main__":
    HEIGHT = int(input("Height: "))  # Making code dynamic for better user experience
    WIDTH = int(input("Width: "))

    box = [[]] * HEIGHT
    for row in range(HEIGHT):  # Filling box with dead or alive values
        box[row] = [" "] * WIDTH
        for column in range(WIDTH):
            if random.randint(0, 1) == 1:
                box[row][column] = "#"

    while True:
        try:
            print_box(box, HEIGHT, WIDTH)

            box = change_box(box, HEIGHT, WIDTH)

            print("\n\n")
            time.sleep(1)
        except KeyboardInterrupt:  # Press "Ctrl" + "c" To implement KeyboardInterrupt and stop the program
            print("The program is stopped")
            sys.exit()
