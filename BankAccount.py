

class BankAccount:
    def __init__(self, balance, interest_rate, name):
        self.balance = 0
        self.interest_rate = .025
        self.name = name

    def deposit(self, amount):
        self.balance += amount
        print("You deposited", amount, "dollars. Your new balance is",self.balance)
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        print("You withdrew", amount, "dollars. Your new balance is", self.balance)
        return self

    def display_account_info(self):
        print("Your interet rate is", self.interest_rate)
        print("Your balance is", self.balance)
        return self

    def yield_interest(self):
        self.yield_interest = self.balance * .025
        self.balance = self.balance + self.yield_interest
        print("Earned interest is", self.yield_interest)
        return self

Checking = BankAccount (2.00, .05, "Checking")
Savings = BankAccount (2.00, .05, "Savings")


Checking.deposit(45).deposit(33).deposit(456).withdrawal(111).yield_interest().display_account_info()

Savings.deposit(345).deposit(123).withdrawal(54).withdrawal(43).withdrawal(32).withdrawal(21).yield_interest().display_account_info()

