import time


def collatz(number):  # Main logic of this exercise
    if number % 2 == 1:  # Checking whether number is even or odd
        return number * 3 + 1
    else:
        return number // 2


if __name__ == "__main__":
    while True:  # Validating user's input
        try:
            print("Enter number to do collatz function")
            num = int(input())
            break
        except ValueError:
            print("You must input the integer value")
    while num != 1:  # When num is 1 program should stop because it's last sequence number of Collatz Sequence
        num = collatz(num)
        print(num)
        time.sleep(0.1)
