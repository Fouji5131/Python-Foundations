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