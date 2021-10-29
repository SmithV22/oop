

class BankAccount:
    def __init__(self, balance, interest_rate, kind):
        self.balance = 0
        self.interest_rate = .025
        self.kind = kind
        
    def deposit(self, amount):
        self.balance += amount
        print("You deposited", amount, "dollars. Your new balance is",self.balance)
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        print("You withdrew", amount, "dollars. Your new balance is", self.balance)
        return self

    def account_info(self):
        print("Your interet rate is", self.interest_rate)
        print("Your balance is", self.balance)
        return self

    def interest(self):
        self.yield_interest = self.balance * .025
        self.balance = self.balance + self.yield_interest
        print("Earned interest is", self.yield_interest)
        return self

Checking = BankAccount (2.00, .05, "Checking")
Savings = BankAccount (2.00, .05, "Savings")

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.account = BankAccount(balance=0, interest_rate=.02, kind=Checking)
                
    def withdrawal(self):
        self.account.withdrawal()
        return self

    def make_deposit(self):
        self.account.deposit()
        return self

    def display_user_balance(self):
        self.account.account_info()
        return self

bugs = User("bugs", 21)
daffy = User("daffy", 52)


bugs.account.deposit(500).withdrawal(350).interest().account_info()
   
   

    