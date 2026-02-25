expenses = []


def add_expense():
    category = str(input("Enter the Expense Category: ").strip())

    try:
        amount = float(input("Wnter the Expense Amount: "))
        if amount <=0:
            raise ValueError("Amount must be positive.")
    except ValueError as e:
        print(f"Invalid amount: {e}\n")
        return
    
    expense = {
        "category": category,
        "amount": amount
    }
    
    expenses.append(expense)
    print("Expense added successfully!\n")

def view_all_expenses():
    if not expenses:
        print("No expenses record.\n")
        return
    
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - {expense['amount']}")
    print()

def total_expenses():
    try:
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total Expenses: {total}\n")
    except Exception as e:
        print(f"Unexpected error: {e}\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_all_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")