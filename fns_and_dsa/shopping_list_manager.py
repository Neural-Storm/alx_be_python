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
        try:
            choice = input("Enter your choice: ")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            item = input("Which item would you like to add?")
            shopping_list.append(item)
        elif choice == '2':
            item = input("Which item would you like to remove?")
            if item in shopping_list:
                shopping_list.remove(item)
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()