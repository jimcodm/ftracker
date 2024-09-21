class Loan:
    def __init__(self, description, amount, category, date_taken, due_date):
        self.description = description
        self.amount = amount
        self.category = category
        self.date_taken = date_taken
        self.due_date = due_date
        self.repayments = []

    def add_repayment(self, amount, date):
        self.repayments.append({"amount": amount, "date": date})

    def total_repaid(self):
        return sum(repayment["amount"] for repayment in self.repayments)

    def outstanding_balance(self):
        return self.amount - self.total_repaid()
