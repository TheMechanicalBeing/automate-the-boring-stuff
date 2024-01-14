import random


if __name__ == "__main__":
    guess = ''

    # This print should not be repeated, so I moved it out of the while loop block
    print("Guess the coin toss! Enter heads or tails:")

    # Changed breakpoint
    while True:
        guess = input()

        # Changed the indentation
        # Changed conditions from number to two words
        toss = random.choice(("heads", "tails"))

        # Optimized if-else block
        if toss == guess:
            print("You got it!")
            # Breakpoint of while loop is here
            break
        else:
            print("Nope! Guess again!")
