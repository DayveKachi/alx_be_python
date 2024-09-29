# a simple shopping list manager that allows users to add items, view the current list, and remove items.


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice.isnumeric():
            if choice == "1":
                # Prompt for and add an item
                item = input("Enter the item to add: ")
                if item.isalpha():
                    shopping_list.append(item)
                    print(f"{item} has been successfully added to your shopping list.")
                else:
                    print("Please a number cannot be an item on a shopping list.")
            elif choice == "2":
                # Prompt for and remove an item
                item = input("Enter the item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(
                        f"{item} has been successfully removed from your shopping list."
                    )
                else:
                    print(f"{item} is not in your shopping list.")
            elif choice == "3":
                # Display the shopping list
                print("***Shopping list***")
                for item in shopping_list:
                    print(item)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("invalid choice. please enter a corresponding number.")


if __name__ == "__main__":
    main()
