import ezsheets


if __name__ == "__main__":

    ss = ezsheets.Spreadsheet('1iDFlcLWCdkwLHh7ZQz2p2MpDR3-lO9jRucLi7EYemas')
    sheet = ss["Form Responses 1"]

    rows = sheet.getRows()

    for row in rows[1:]:
        name, surname, age = row[1:4]
        if name and surname and age:
            print(f"{surname}, {name} ({age} years old)")
