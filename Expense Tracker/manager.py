from models import create_expense

def save_expenses(expense_list, filename="expenses.txt"):
    with open(filename, "w") as file:
        for exp in expense_list:
            file.write(f"{exp['category']},{exp['amount']}\n")

def load_expenses(filename="expenses.txt"):
    expenses = []
    try:
        with open(filename, "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                expenses.append({
                    "category": category,
                    "amount": float(amount)
                })
    except FileNotFoundError:
        pass  # If file doesn't exist, start empty
    
    return expenses

def add_expense(expense_list: list, *, category: str, amount: float):
    expense = create_expense(category, amount)
    expense_list.append(expense)
    return "Expense added successfully!"

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
    
    for i, expense in enumerate(expenses_list, start=1):
        print(f"{i}. {expense['category']} - {expense['amount']}")
    print()

def delete_expense(expense_list: list, index: int):
    try:
        removed = expense_list.pop(index - 1)
        return f"Deleted {removed['category']} expense."
    except IndexError:
        return "Invalid expense number."
    