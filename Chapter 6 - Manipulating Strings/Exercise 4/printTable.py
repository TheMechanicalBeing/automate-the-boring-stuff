def print_table(print_data):
    # Storing maximum length word by each row
    max_by_row = []
    for column in print_data:
        max_by_row.append(max([len(word) for word in column]))
    # Looping through list items by [row][column]
    for i in range(len(print_data[0])):
        for j in range(len(print_data)):
            print(print_data[j][i].rjust(max_by_row[j], " "), end=" ")
        print()


if __name__ == "__main__":
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    print_table(tableData)
