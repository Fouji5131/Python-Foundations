from models import create_expense

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
    