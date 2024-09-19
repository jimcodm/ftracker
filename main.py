# main.py

from financetracker import FinanceTracker, Transaction, InvalidInputError
import atexit


def get_transaction_input():
    try:
        description = input("Enter transaction description: ")
        amount = float(input("Enter transaction amount: "))
        return Transaction(description, amount)
    except ValueError:
        raise InvalidInputError("Invalid input. Amount must be a valid number.")


def main():
    finance_tracker = FinanceTracker()
    finance_tracker.load_from_file()  # Load transactions from file

    atexit.register(finance_tracker.save_to_file)  # Save transactions to file on exit

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            try:
                transaction = get_transaction_input()
                finance_tracker.add_transaction(transaction)
                print("Transaction added successfully!")
            except InvalidInputError as e:
                print(f"Error: {e}")
        elif choice == '2':
            finance_tracker.display_transactions()
            print(f"Current balance: ${finance_tracker.get_balance():.2f}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
