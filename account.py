import datetime
import pytz  

class Account:
 def __init__(self, initial_balance=0, transaction_limit_hour=14):
        self.balance = initial_balance
        self.transaction_limit_hour = transaction_limit_hour

 def bank_policy(self):
    print("Verifying bank policy...")
    now = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
    if now.hour >= self.transaction_limit_hour:
        raise ValueError("As transações só podem ser realizadas até as {}:00".format(self.transaction_limit_hour))

 def deposit(self, amount):
    self.bank_policy()
    self.balance += amount

 def withdraw(self, amount):
    self.bank_policy()
    if amount > self.balance:
        raise ValueError("Saldo insuficiente")
    self.balance -= amount
