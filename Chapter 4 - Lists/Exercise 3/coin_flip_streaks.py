import random


def coin_flip():  # Returns T(ails) or H(eads)
    return random.choice(["T", "H"])


def check_six_streak():
    flip_results = []  # Storing coin flips here
    occurences = 0  # Storing six streaks here
    for _ in range(100):  # Making coin flip 100 times
        flip_result = coin_flip()
        flip_results.append(flip_result)
        print(flip_result, end=" ")
    for i in range(94):
        if len(set(flip_results[i:i+6])) == 1:  # Checking if sequence of 6 coin flips have been the same
            occurences += 1
    print()
    return occurences


if __name__ == "__main__":
    how_many = check_six_streak()
    print(f"There have been {how_many} of six streaks")
