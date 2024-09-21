from datetime import date

class MoneyIn:
    def __init__(self, description, amount, category, transaction_date=None):
        self.description = description
        self.amount = amount
        self.category = category
        self.transaction_date = transaction_date or date.today()

    def __repr__(self):
        return f"MoneyIn(description={self.description}, amount={self.amount}, category={self.category}, date={self.transaction_date})"

class MoneyOut:
    def __init__(self, description, amount, category, transaction_date=None):
        self.description = description
        self.amount = amount
        self.category = category
        self.transaction_date = transaction_date or date.today()

    def __repr__(self):
        return f"MoneyOut(description={self.description}, amount={self.amount}, category={self.category}, date={self.transaction_date})"
