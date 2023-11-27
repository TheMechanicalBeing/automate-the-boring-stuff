import pyperclip


# The function formats each line of text parameter into bullet format
def bullet_the_text(text):
    to_return = ""
    for line in text.split("\n"):
        to_return += f"* {line}\n"
    print(text.split("\n"))
    print(text)
    return to_return.strip()


if __name__ == "__main__":
    pyperclip.copy(bullet_the_text(pyperclip.paste()))
    print("Recopied text to bullet list")
