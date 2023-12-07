import re

import pyperclip

def phoneRegex(text):
    phone = re.compile(r"""
    ((\d{3}|\(\d{3}\))?                     # Area Code
    (\s|-|\.)                               # Separator
    (\d{3}|\(\d{3}\))                       # First 3 digits
    (\s|-|\.)                               # Separator
    (\d{4}|\(\d{4}\))                       # Last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?)           # Extension
    """, re.VERBOSE)
    return phone.findall(text)


def emailRegex(text):
    email = re.compile(r"(([a-zA-Z0-9!#$%&'*+/=?^_`{}|~.-])+@([a-zA-Z0-9-])+(\.[a-zA-Z0-9]+)+)")
    return email.findall(text)


if __name__ == "__main__":
    text_to_manipulate = pyperclip.paste()          # Getting text from clipboard
    phone_numbers = phoneRegex(text_to_manipulate)
    emails = emailRegex(text_to_manipulate)
    result = ["Phone Numbers: ", "Emails: "]

    if not phone_numbers and not emails:
        print("There was no phone number or email address in given text")
    else:

        print("Copied to clipboard:")
        for phone_number in phone_numbers:
            result[0] += f"{phone_number[0]} "  # Saving phone number from clipboard
            print(phone_number[0])

        for email in emails:
            result[1] += f"{email[0]} "         # Saving emails from clipboard
            print(email[0])

        pyperclip.copy("\n".join(result))       # Setting text to clipboard
