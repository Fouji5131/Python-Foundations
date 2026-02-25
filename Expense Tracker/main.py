from manager import add_expense, show_expenses, calculate_total

def main():
    expenses = []

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            print(f"Total: {calculate_total(expenses)}")
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()