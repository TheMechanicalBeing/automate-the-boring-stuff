import random  # python's built-in module


if __name__ == "__main__":
    print("Computer".center(20, "-"))
    print("I'm thinking of a number between 1 and 20\nyou have 5 chance")

    computerNumber = random.randint(1, 20)  # generating random integer between 1 and 20
    tries = 0
    guessed = False

    while tries != 5:

        print("Pick a number")
        userNumber = int(input())  # Users guess (it MUST be integer)

        # Giving hints to user using if-else code block
        if userNumber > computerNumber:
            print("Try lower.")
            tries += 1
            continue
        elif userNumber < computerNumber:
            print("Try higher.")
            tries += 1
            continue
        else:
            guessed = True
            tries += 1
            break

    if guessed:  # Checks whether user guessed the right number
        print("Congrats you guessed the number that I thought of.\n"
              f"Total tries: {tries}")
    else:
        print("Unfortunately, you did not manage to guess my number.\n"
              f"The right answer was {computerNumber}. You can try again.")
