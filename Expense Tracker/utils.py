def get_valid_amount():
    while True:
        try:
            return float(input("Enter amount: "))
        except ValueError:
            print("Invalid number. Try again.")