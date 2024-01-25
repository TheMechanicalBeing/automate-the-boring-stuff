import pprint

import openpyxl


if __name__ == "__main__":

    print("Loading workbook...")
    wb = openpyxl.load_workbook("censuspopdata.xlsx")
    sheet = wb["Population by Census Tract"]

    country_data = dict()

    print("Reading and saving sheets data...")
    for row in range(2, sheet.max_row+1):
        state = sheet["B" + str(row)].value
        country = sheet["C" + str(row)].value
        population = sheet["D" + str(row)].value

        country_data.setdefault(state, {})
        country_data[state].setdefault(country, {"tracts": 0, "population": 0})

        country_data[state][country]["tracts"] += 1
        country_data[state][country]["population"] += int(population)

    print("Writing results...")
    with open("census2010.py", "w") as result_file:
        result_file.write("country_data = " + pprint.pformat(country_data))

    print("Done.")
