from financetracker import FinanceTracker

def main():
    finance_tracker = FinanceTracker()  # Create a FinanceTracker object

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Add Loan")
        print("4. View Loans")
        print("5. Make Repayment")
        print("6. Clear Data")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            finance_tracker.add_transaction()
        elif choice == '2':
            finance_tracker.view_transactions()
        elif choice == '3':
            finance_tracker.add_loan()
        elif choice == '4':
            finance_tracker.view_loans()
        elif choice == '5':
            finance_tracker.make_repayment()
        elif choice == '6':
            finance_tracker.clear_data()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please select a valid option.")

    # Ensure data is saved on exit
    finance_tracker.save_data()

if __name__ == "__main__":
    main()
