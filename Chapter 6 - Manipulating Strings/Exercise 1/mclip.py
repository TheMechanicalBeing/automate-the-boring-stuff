import sys
import pyperclip


TEXT = {
    "agree": """Yes, I agree. That sounds fine to me.""",
    'busy': '''Sorry, can we do this later this week or next week?''',
    'upsell': '''Would you consider making this a monthly donation?'''
}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: filename.py [keyphrase]")
        sys.exit()

    keyphrase = sys.argv[1].strip().lower()

    if keyphrase not in TEXT.keys():
        print(f"There is no keyphrase named {keyphrase}.")
        sys.exit()
    else:
        pyperclip.copy(TEXT[keyphrase])
        print(f"Copied text: '{TEXT[keyphrase]}'")
