# Assuming this is within your shopping_list_manager.py

def display_header():
    """
    Displays the header for the shopping list manager.
    """
    print(f"Shopping List Manager")

# You can call the display_header function to display the message
display_header()

def display_menu():
    """
    Displays the menu for the shopping list manager.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    """
    Adds an item to the shopping list.
    """
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("Item name cannot be empty.")

def main():
    """
    Main function to manage the shopping list.
    """
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add an item
            add_item(shopping_list)

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' is not in the shopping list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
