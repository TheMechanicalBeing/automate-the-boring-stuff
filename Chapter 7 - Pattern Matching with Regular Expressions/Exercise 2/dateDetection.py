import re


def detect_date(text):
    date_complier = re.compile("(\d\d)/(\d\d)/(\d\d\d\d)")  # Regular Expression that detects date format DD/MM/YYYY in text
    return date_complier.findall(text)  # Returning each date format


def is_leap(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    return True


def validate_date(day, month, year):
    if day < 0 or month < 0 or month > 12 or year < 0 or year > 9999:   # Validating Constraints
        return False
    elif month in [4, 6, 9, 11] and day > 30:   # Checking day of month that has maximum of 30 days
        return False
    elif month == 2 and is_leap(year) and day > 29:     # Checking for February in leap year
        return False
    elif month == 2 and day > 28:   # Checking for February not in leap year
        return False
    elif day > 31:  # Checking day of month that has maximum of 31 days
        return False
    return True


if __name__ == "__main__":
    text_to_manipulate = input("Input text with dates and I will detect it and tell you if it is valid date\n")
    dates = detect_date(text_to_manipulate)

    if not dates:
        print("There is no date in given input")
    else:
        for date in dates:
            day, month, year = date
            day, month, year = int(day), int(month), int(year)

            if validate_date(day, month, year):
                print(f"Given date {day:02}/{month:02}/{year:04} is valid")
            else:
                print(f"Given date {day:02}/{month:02}/{year:04} is NOT valid")
