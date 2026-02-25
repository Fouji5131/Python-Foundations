expenses = []

def create_expense(category: str, amount: float = 0.0):
    return {
        "category": category,
        "amount": amount
    }

def get_user_category(prompt="Enter category: "):
    while True:
        try:
            return str(input(prompt))
        except Exception:
            print("Invalid category. Try again.")

def get_user_amount(prompt="Enter amount: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

def add_expense(expense_list: list, *, category: str, amount: float):
    expense = create_expense(category, amount)
    expense_list.append(expense)
    return "Expense added successfully!"

    # category = str(input("Enter the Expense Category: ").strip())
    # try:
    #     amount = float(input("Wnter the Expense Amount: "))
    #     if amount <=0:
    #         raise ValueError("Amount must be positive.")
    # except ValueError as e:
    #     print(f"Invalid amount: {e}\n")
    #     return
    # expense = {
    #     "category": category,
    #     "amount": amount
    # }
    # expenses.append(expense)
    # print("Expense added successfully!\n")

def total_expenses(expenses_list: list):
    try:
        total = sum(expense['amount'] for expense in expenses_list)
        return total
    except Exception as e:
        print(f"Unexpected error: {e}\n")

def view_all_expenses(expenses_list: list):
    if not expenses_list:
        print("No expenses record.\n")
        return
    
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - {expense['amount']}")
    print()

def delete_expense(expense_list: list, index: int):
    try:
        removed = expense_list.pop(index - 1)
        return f"Deleted {removed['category']} expense."
    except IndexError:
        return "Invalid expense number."
    
def menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Delete Expense")
    print("5. Exit")


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