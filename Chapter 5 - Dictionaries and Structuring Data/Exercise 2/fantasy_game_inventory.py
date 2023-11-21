def display_inventory(inventory):  # Passing dict() parameter
    print("Inventory:")
    for item, quantity in inventory.items():
        print(item, quantity, sep=" ")
    # Making sum of item quantities
    print(f'Total number of items: {sum([quantity for quantity in inventory.values()])}')


def pick_loot(inventory, loot_to_pick):  # Passing dict() and list() parameters
    for loot in loot_to_pick:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1


if __name__ == "__main__":
    current_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(current_inventory)
    pick_loot(current_inventory, ["gold coin", "gold coin", "gold coin",
                                  "torch", "gold coin", "gold coin", "arrow", "arrow"])
    print()
    display_inventory(current_inventory)
