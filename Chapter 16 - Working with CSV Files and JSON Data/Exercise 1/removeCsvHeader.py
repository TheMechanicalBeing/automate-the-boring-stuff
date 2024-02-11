import os
import csv


if __name__ == "__main__":
    os.makedirs("removed_header", exist_ok=True)

    # Looking for csv files
    for filename in os.listdir("."):
        if not filename.endswith(".csv"):
            continue

        print(f"Removing header from file: {filename}")

        # Reading csv file
        rows = []

        with open(filename) as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                if reader.line_num == 1:
                    continue
                rows.append(row)

        # Writing csv file
        with open(os.path.join("removed_header", filename), "w", newline="") as csv_file:
            writer = csv.writer(csv_file)

            for row in rows:
                writer.writerow(row)

    print("Done")
