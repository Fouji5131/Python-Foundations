from models import create_expense

def add_expense(expense_list):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    expense = create_expense(category, amount)
    expense_list.append(expense)

def show_expenses(expense_list):
    for i, exp in enumerate(expense_list, start=1):
        print(f"{i}. {exp['category']} - {exp['amount']}")

def calculate_total(expense_list):
    return sum(exp["amount"] for exp in expense_list)