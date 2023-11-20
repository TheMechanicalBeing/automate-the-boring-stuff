def comma_code(items):  # Main function
    if len(items) == 1:
        return items[0]
    result = str(items[0])
    for item in items[1:-1]:  # Iterating through list items
        result += f", {item}"
    return result + f" and {items[-1]}"


if __name__ == '__main__':
    check_list = ["apples", "bananas", "tofu", "cats"]
    print(check_list)  # Printing initial list
    check_result = comma_code(check_list)
    print(check_result)  # Printing formatted result
