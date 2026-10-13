class BankAccount:
    def __init__(self,balance = 0):
        self. balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if amount> self.balance:
            raise ValueError ("Insufficient Balance")
        self.balance -= amount

acct = BankAccount(100)
try:
    acct.withdrawal(500)
except ValueError as error:
    print (f"Couldn't perform withdraw: {error}")


        
