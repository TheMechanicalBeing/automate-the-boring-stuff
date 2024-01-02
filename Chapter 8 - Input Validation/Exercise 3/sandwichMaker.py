import pyinputplus as pyip


PRICES = {
    "bread": {
        "wheat": 1.25,
        "white": 1.5,
        "sourdough": 2
    },
    "protein": {
        "chicken": 5,
        "turkey": 6.5,
        "ham": 5.5,
        "tofu": 7
    },
    "cheese": {
        'cheddar': 3.5,
        'swiss': 5,
        "mozzarella": 4.5
    },
    "mayo": 1,
    "mustard": 0.75,
    'lettuce': 1.25,
    "tomato": 1
}


def should_be_added(want_or_not):
    if want_or_not == "yes":
        return True
    return False


if __name__ == "__main__":

    bread_type = pyip.inputMenu(["wheat", "white", "sourdough"], "Choose bread type\n")
    protein_type = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], "Choose protein type\n")
    want_cheese = pyip.inputYesNo("Do you want cheese in sandwich?\n")
    if want_cheese == "yes":
        cheese_type = pyip.inputMenu(["cheddar", "swiss", "mozzarella"], "Choose cheese type\n")
    tomato = pyip.inputYesNo("Do you want tomato?\n")
    mustard = pyip.inputYesNo("Do you want mustard?\n")
    lettuce = pyip.inputYesNo("Do you want lettuce?\n")
    mayo = pyip.inputYesNo("Do you want mayo?\n")
    quantity = pyip.inputNum("How many sandwiches?\n", min=1)

    cost = PRICES.get("bread").get(bread_type) + PRICES.get("protein").get(protein_type)

    if should_be_added(want_cheese):
        cost += PRICES.get("cheese").get(cheese_type)

    for ingredient in ["tomato", "mustard", "lettuce", "mayo"]:
        if should_be_added(ingredient):
            cost += PRICES.get(ingredient)

    cost *= quantity

    print(f'Total price: {cost}')
