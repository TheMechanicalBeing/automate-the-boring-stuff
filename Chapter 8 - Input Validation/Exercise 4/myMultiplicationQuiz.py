import random, time

def custom_input(prompt, type):
    while True:
        tracker = 0
        to_return = input(prompt)
        try:
            if type == "int":
                to_return = int(to_return)
            return to_return
        except:
            tracker += 1
            print(f"'to_return' is not a valid response.")
        if tracker == 3:
            print("Out of tries!")
            return False


if __name__ == '__main__':
    numberOfQuestions = custom_input("How many questions?\n", "int")
    rightAnswers = 0
    response = -1

    for question in range(numberOfQuestions):
        time.sleep(1)
        question_start = time.time()
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)

        while response != num1 * num2 or not response:
            response = custom_input(f"{num1} * {num2} = ", "int")
            if response != num1 * num2:
                print(f"{response} is not right answer!")

        if not response:
            break
        elif time.time() - question_start > 8:
            print(f"Out of time!")
            break
        elif response == num1 * num2:
            rightAnswers += 1
            print("Correct!")

    print(f"Results: {rightAnswers}/{numberOfQuestions}")
