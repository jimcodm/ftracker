from transaction import MoneyIn, MoneyOut
from datahandling import save_transactions  # Import only save functionality
from datetime import date
from Loan import Loan

class FinanceTracker:
    """Provides methods for managing financial transactions."""

    def __init__(self, filename="finance_data.txt"):
        self.filename = filename
        self.money_in_transactions = []
        self.money_out_transactions = []
        self.loans = []
        self.load_data()  # Load existing data when initializing
        
    def load_data(self):
        """Loads transactions and loans from a text file."""
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    
                    if data[0] == "IN":
                        self.money_in_transactions.append(MoneyIn(data[1], float(data[2]), data[3], data[4]))
                    elif data[0] == "OUT":
                        self.money_out_transactions.append(MoneyOut(data[1], float(data[2]), data[3], data[4]))
                    elif data[0] == "LOAN":
                        loan = Loan(data[1], float(data[2]), data[3], data[4], data[5])
                        total_repaid = float(data[6])
                        loan.repayments.append({"amount": total_repaid, "date": "Loaded"})  # Simulate repayment loading
                        self.loans.append(loan)
        except FileNotFoundError:
            print("No existing data found.")
        except ValueError as e:
            print(f"Error loading data: {e}")


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
            transaction_date = input("Enter transaction date (YYYY-MM-DD) or leave blank for today: ")
            if transaction_date:
                transaction_date = date.fromisoformat(transaction_date)
            else:
                transaction_date = date.today()
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
            transaction_date = input("Enter transaction date (YYYY-MM-DD) or leave blank for today: ")
            if transaction_date:
                transaction_date = date.fromisoformat(transaction_date)
            else:
                transaction_date = date.today()
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
            print(f"{transaction.transaction_date} - {transaction.description} ({transaction.category}): ₱{transaction.amount:.2f}")

        print("\nMoney Out:")
        for transaction in self.money_out_transactions:
            print(f"{transaction.transaction_date} - {transaction.description} ({transaction.category}): ₱{transaction.amount:.2f}")

        print(f"\nCurrent balance: ₱{self.get_balance():.2f}")


    def get_balance(self):
        """Calculates the current balance."""
        total_money_in = sum(transaction.amount for transaction in self.money_in_transactions)
        total_money_out = sum(transaction.amount for transaction in self.money_out_transactions)
        return total_money_in - total_money_out

    def save_data(self):
        """Saves all transactions and loans to a text file."""
        with open(self.filename, "w") as file:
            for transaction in self.money_in_transactions:
                file.write(f"IN,{transaction.description},{transaction.amount},{transaction.category},{transaction.transaction_date}\n")
            for transaction in self.money_out_transactions:
                file.write(f"OUT,{transaction.description},{transaction.amount},{transaction.category},{transaction.transaction_date}\n")
            for loan in self.loans:
                file.write(f"LOAN,{loan.description},{loan.amount},{loan.category},{loan.date_taken},{loan.due_date},{loan.total_repaid()}\n")
        print("Data saved successfully.")


    def add_loan(self):
            """Adds a new loan."""
            description = input("Enter loan description: ")
            amount = float(input("Enter loan amount: "))
            category = input("Enter category: ")
            date_taken = input("Enter date taken (YYYY-MM-DD): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            loan = Loan(description, amount, category, date_taken, due_date)
            self.loans.append(loan)
            print("Loan added successfully!")

    def view_loans(self):
        """Displays all loans."""
        if not self.loans:
            print("No loans to display.")
            return

        print("\nLoans:")
        for loan in self.loans:
            print(f"{loan.description}: ₱{loan.amount:.2f}, Due: {loan.due_date}, Repaid: ₱{loan.total_repaid():.2f}, Outstanding: ₱{loan.outstanding_balance():.2f}")

    def make_repayment(self):
        """Records a repayment for a loan."""
        loan_description = input("Enter the loan description to repay: ")
        for loan in self.loans:
            if loan.description == loan_description:
                amount = float(input("Enter repayment amount: "))
                date = input("Enter repayment date (YYYY-MM-DD): ")
                loan.add_repayment(amount, date)
                print("Repayment recorded successfully!")
                return
        print("Loan not found.")
        
    def clear_data(self):
        """Clears all transactions and loans."""
        self.money_in_transactions = []
        self.money_out_transactions = []
        self.loans = []
        print("All data has been cleared.")