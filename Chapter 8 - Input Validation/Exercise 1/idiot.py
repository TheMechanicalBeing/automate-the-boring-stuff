import pyinputplus as pyip

if __name__ == '__main__':
    while True:
        response = pyip.inputYesNo("Want to know how to keep an idiot busy for hours?\n")
        if response == "yes":
            continue
        print("Thank you, have a nice day.")
        break
