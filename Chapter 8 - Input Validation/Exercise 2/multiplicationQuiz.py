import pyinputplus as pyip
import time, random

if __name__ == "__main__":
    numberOfQuestions = pyip.inputNum("How many questions?\n", min=1)
    rightAnswers = 0

    for question in range(numberOfQuestions):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        try:
            response = pyip.inputStr(f"{num1} * {num2} = ", allowRegexes=[f"{num1*num2}"], blockRegexes=[r".*"], timeout=8, limit=3)
        except pyip.TimeoutException:
            print("Out of time!")
            break
        except pyip.RetryLimitException:
            print("Out of tries")
            break
        print(f"Correct!")
        rightAnswers += 1

    print(f"Results: {rightAnswers}/{numberOfQuestions}")
