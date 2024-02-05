import ezsheets


if __name__ == "__main__":

    ss = ezsheets.Spreadsheet("1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg")
    sheet = ss.sheets[0]
    rows = sheet.getRows()

    for index, row in enumerate(rows[1:]):
        beans_per_jar, jars, total = row[:3]
        if beans_per_jar and jars and total and int(beans_per_jar) * int(jars) != int(total):
            print(f"The mistake was on row No.{index+2} ({beans_per_jar} * {jars} does not equal to {total})")
            break
