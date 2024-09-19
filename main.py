from financetracker import FinanceTracker

def main():
    finance_tracker = FinanceTracker()  # Create a FinanceTracker object

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            finance_tracker.add_transaction()  # Delegate to FinanceTracker

        elif choice == '2':
            finance_tracker.view_transactions()  # Delegate to FinanceTracker

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    # Ensure data is saved on exit
    finance_tracker.save_data()

if __name__ == "__main__":
    main()