from manager import add_expense, total_expenses, view_all_expenses, delete_expense
from utils import get_user_category, get_user_amount

def menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Delete Expense")
    print("5. Exit")


def main():
    expenses = []


    while True:
        menu()
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            category = get_user_category()
            amount = get_user_amount()
            print(add_expense(expenses, category=category, amount=amount))
            print()
        elif choice == "2":
            view_all_expenses(expenses)
        elif choice == "3":
            print(f"Total Expense: {total_expenses(expenses)}\n")
        # total_expenses()
        elif choice == "4":
            view_all_expenses(expenses)
            index = get_user_amount("Enter expense number to delete: ")
            print(delete_expense(expenses, int(index)))
            print()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()