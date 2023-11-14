import time  # Importing required modules
import sys


def draw_zigzag_line(ind, figure):  # Drawing function
    print(ind * " " + figure)


if __name__ == "__main__":
    indent = 1
    grow = True  # Grow defines wheter should indent grow or shrink
    while True:
        try:
            draw_zigzag_line(indent, "*" * 5)

            if grow:  # Growing or shrinking indentation for next iteration
                indent += 1
            else:
                indent -= 1

            if indent == 0:  # Checking whether grow should change direction
                grow = True
            elif indent == 20:
                grow = False

            time.sleep(0.1)  # For user experience drawing line per 0.1 second
        except KeyboardInterrupt:
            print("User stopped the program")
            sys.exit()
