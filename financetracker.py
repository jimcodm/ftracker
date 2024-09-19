# financetracker.py

class Transaction:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount


class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        return sum(transaction.amount for transaction in self.transactions)

    def display_transactions(self):
        for transaction in self.transactions:
            print(f"{transaction.description}: ${transaction.amount:.2f}")

    def save_to_file(self, filename="finance_data.txt"):
        with open(filename, "w") as file:
            for transaction in self.transactions:
                file.write(f"{transaction.description},{transaction.amount}\n")

    def load_from_file(self, filename="finance_data.txt"):
        try:
            with open(filename, "r") as file:
                for line in file:
                    description, amount = line.strip().split(",")
                    self.add_transaction(Transaction(description, float(amount)))
        except FileNotFoundError:
            print("No existing data found.")


# Exception for invalid input
class InvalidInputError(Exception):
    pass
