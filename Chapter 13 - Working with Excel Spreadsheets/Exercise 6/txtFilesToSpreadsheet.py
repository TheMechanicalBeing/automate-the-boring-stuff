import sys

import openpyxl


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python txtFilesToSpreadsheet.py <filename>.txt*")
        sys.exit()

    wb = openpyxl.Workbook()
    sheet = wb.active
    filenames = sys.argv[1:]

    column = 1
    for filename in filenames:
        try:
            with open(filename) as file:
                for index, line in enumerate(file):
                    sheet.cell(row=index+1, column=column).value = line

            column += 1

        except FileNotFoundError:
            print(f"Could not find file: {filename}")

    wb.save("txtFilesToSpreadsheet.xlsx")
    print("Done.")
