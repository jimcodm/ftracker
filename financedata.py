from financetracker import MoneyIn, MoneyOut

def save_to_file(finance_tracker, filename="finance_data.txt"):
    with open(filename, "w") as file:
        for transaction in finance_tracker.money_in_transactions:
            file.write(f"IN,{transaction.description},{transaction.amount},{transaction.category}\n")
        for transaction in finance_tracker.money_out_transactions:
            file.write(f"OUT,{transaction.description},{transaction.amount},{transaction.category}\n")

def load_from_file(finance_tracker, filename="finance_data.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == "IN":
                    finance_tracker.add_money_in(MoneyIn(data[1], float(data[2]), data[3]))
                elif data[0] == "OUT":
                    finance_tracker.add_money_out(MoneyOut(data[1], float(data[2]), data[3]))
    except FileNotFoundError:
        print("No existing data found.")