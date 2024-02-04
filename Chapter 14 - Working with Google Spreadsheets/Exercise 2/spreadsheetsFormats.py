import ezsheets

if __name__ == "__main__":
    ss_id = input("Enter the spreadsheet ID:\n")
    ss = ezsheets.Spreadsheet(ss_id)

    ss_format = input("Enter the number to choose format:\n1. CSV\n2. TSV\n3. Excel\n4. PDF\n5. OpenOffice\n6. Zip\n")

    download = True

    match ss_format:
        case "1":
            ss.downloadAsCSV()
        case "2":
            ss.downloadAsTSV()
        case "3":
            ss.downloadAsExcel()
        case "4":
            ss.downloadAsPDF()
        case "5":
            ss.downloadAsODS()
        case "6":
            ss.downloadAsHTML()
        case _:
            download = not download

    if download:
        print("Downloaded file in given format successfully.")
    else:
        print("Invalid input.")
