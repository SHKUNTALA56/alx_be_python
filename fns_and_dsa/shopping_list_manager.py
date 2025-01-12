def display_menu():
    """
    Display the menu for the shopping list manager.
    """
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

def shopping_list_manager():
    """
    A simple shopping list manager that allows users to add, remove, and view items.
    """
    shopping_list = []

    while True:
        display_menu()

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item cannot be empty.")

        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == '3':
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is currently empty.")

        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    shopping_list_manager()
