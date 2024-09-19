def load_transactions(filename, finance_tracker):
    """Loads transaction data from a text file into a FinanceTracker object."""
    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data:
                    transaction_type, description, amount, category = data
                    amount = float(amount)
                    if transaction_type == "IN":
                        finance_tracker.add_money_in(MoneyIn(description, amount, category))
                    elif transaction_type == "OUT":
                        finance_tracker.add_money_out(MoneyOut(description, amount, category))
    except FileNotFoundError:
        print("Data file not found. Creating a new one...")

def save_transactions(filename, finance_tracker):
    """Saves transaction data from a FinanceTracker object to a text file."""
    try:
        with open(filename, "w") as file:
            for transaction in finance_tracker.money_in_transactions:
                file.write(f"IN,{transaction.description},{transaction.amount},{transaction.category}\n")
            for transaction in finance_tracker.money_out_transactions:
                file.write(f"OUT,{transaction.description},{transaction.amount},{transaction.category}\n")
    except PermissionError:
        print("Error saving data. Check file permissions.")