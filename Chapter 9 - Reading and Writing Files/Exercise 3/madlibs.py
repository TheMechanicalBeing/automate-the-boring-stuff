import os
import re
from pathlib import Path

import pyinputplus

if __name__ == "__main__":
    user_input = pyinputplus.inputChoice(["Create", "Generate"],
                                         "Do you want to generate or create text? Note: type Create or Generate\n")

    original_path = Path(__file__).parent / "original"
    generated_path = Path(__file__).parent / "generated"
    original_texts_count = len(os.listdir(original_path))       # How many .txt files are in original directory
    generated_texts_count = len(os.listdir(generated_path))     # How mant .txt files are in generated directory

    if user_input == "Create":
        print("Remember MadLibs Keywords are: ADJECTIVE, NOUN, VERB, ADVERB")
        text_to_write = input("Enter text to be written in MadLibs:\n")
        with open(original_path / f"text{original_texts_count + 1}.txt", "w") as f:
            f.write(text_to_write)
    else:
        # Asking user on which text to manipulate
        text_choice = pyinputplus.inputNum(
            f"Choose which text you want to choose by number in range of 1..{original_texts_count} - ", greaterThan=0,
            lessThan=original_texts_count + 1)

        # Reading text that has to be manipulated
        print("This is the text that you have to input some values:\n")
        with open(original_path / f"text{text_choice}.txt") as f:
            text_to_generate = f.read()
        print(text_to_generate, end="\n\n")

        # Using RegEx to implement replacing
        compiler = re.compile("(^|\s)(VERB|ADVERB|ADJECTIVE|NOUN)(\W)")
        matches = compiler.finditer(text_to_generate)  # Storing all occurences into variable

        # Iterating through each match
        for match in matches:
            match_type = match.group(2)
            to_replace = input(f"Enter {match_type.lower()}:\n")  # Getting user data to replace occurence
            # Using count=1 to substitute only first occurence
            text_to_generate = compiler.sub(r"\g<1>{}\g<3>".format(to_replace), text_to_generate, count=1)

        text_to_generate = " ".join(text_to_generate)  # Joining list to make it as whole string
        generated_name = f"text{generated_texts_count + 1}.txt"  # The filename of generated text

        # Storing generated text into .txt file
        with open(generated_path / generated_name, "w") as f:
            f.write(text_to_generate)
        print(f"Successfully generated your text which is located into ./generated/{generated_name}")
