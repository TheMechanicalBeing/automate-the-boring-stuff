import random


if __name__ == "__main__":
    guesses = ["r", "p", "s"]  # List of possible value in Rock, Paper, Scissors game
    tracker = dict()

    tracker.setdefault("w", 0)  # Making each value of result tracker as 0
    tracker.setdefault("d", 0)
    tracker.setdefault("l", 0)

    while True:
        print("-" * 20)
        print(f'''Current results:
Win - {tracker["w"]} | Draw - {tracker["d"]} | Lost - {tracker["l"]}''')

        computerGuess = random.choice(guesses)  # Making random choice from guesses list
        print("Pick your choice: 'R' - Rock; 'P' - Paper; 'S' - Scissors; 'Q' - Quit")
        userGuess = input().lower()  # Making user's choice case-insensitive
        print(f"Computer's guess was {computerGuess}")

        if userGuess == 'q':  # If 'q' is user's choice the game ends and final result comes out.
            print("-" * 20)
            print(f'''Final results:
Win - {tracker["w"]} | Draw - {tracker["d"]} | Lost - {tracker["l"]}''')
            break

        """Here I made my interpretation of game's logic
        F.E. in guesses list the n-th index always loses to (n+1)%3-th index"""
        thisRound = (guesses.index(userGuess), guesses.index(computerGuess))

        if guesses[thisRound[0]] == guesses[thisRound[1]]:
            print("This round is draw")
            tracker["d"] += 1
            continue
        elif guesses[(thisRound[0]+1)%3] == guesses[thisRound[1]]:
            print("Computer has won this round")
            tracker["l"] += 1
            continue
        else:
            print("Congrats. you won this round")
            tracker["w"] += 1
            continue

