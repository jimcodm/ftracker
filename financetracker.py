from transaction import MoneyIn, MoneyOut
from datahandling import save_transactions  # Import only save functionality

class FinanceTracker:
    """Provides methods for managing financial transactions."""

    def __init__(self, filename="finance_data.txt"):
        self.filename = filename
        self.money_in_transactions = []
        self.money_out_transactions = []

    def add_transaction(self):
        """Adds a new transaction (delegates to specific MoneyIn or MoneyOut methods)."""
        transaction_type = input("Enter transaction type (IN/OUT): ")
        if transaction_type.upper() == "IN":
            self.add_money_in()
        elif transaction_type.upper() == "OUT":
            self.add_money_out()
        else:
            print("Invalid transaction type. Please enter IN or OUT.")

    def add_money_in(self):
        """Adds a money-in transaction."""
        try:
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            self.money_in_transactions.append(MoneyIn(description, amount, category))
            print("Money in transaction added successfully!")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def add_money_out(self):
        """Adds a money-out transaction."""
        try:
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            self.money_out_transactions.append(MoneyOut(description, amount, category))
            print("Money out transaction added successfully!")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def view_transactions(self):
        """Displays all transactions."""
        if not self.money_in_transactions and not self.money_out_transactions:
            print("No transactions to display.")
            return

        print("\nTransactions:")
        print("Money In:")
        for transaction in self.money_in_transactions:
            print(f"{transaction.description} ({transaction.category}): ₱{transaction.amount:.2f}")

        print("\nMoney Out:")
        for transaction in self.money_out_transactions:
            print(f"{transaction.description} ({transaction.category}): ₱{transaction.amount:.2f}")

        print(f"\nCurrent balance: ₱{self.get_balance():.2f}")

    def get_balance(self):
        """Calculates the current balance."""
        total_money_in = sum(transaction.amount for transaction in self.money_in_transactions)
        total_money_out = sum(transaction.amount for transaction in self.money_out_transactions)
        return total_money_in - total_money_out

    def save_data(self):
        """Delegates saving transactions to datahandling.py."""
        save_transactions(self.filename, self)  # Call the save function