import re


def check(password):
    if not re.search(r'.*[0-9].*', password):
        return "Strong password must have at least one digit !!!"
    elif not re.search(r'.*[A-Z].*', password):
        return "Strong password must have at least one uppercase character !!!"
    elif not re.search(r'.*[a-z].*', password):
        return "Strong password must have at least one lowercase character !!!"
    elif len(password) < 8:
        return "Strong password must have at least 8 characters !!!"
    return "You have strong password"


if __name__ == '__main__':
    password = input("Enter password to validate its strength:")
    print(check(password))
