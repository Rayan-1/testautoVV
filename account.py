import datetime
import pytz  

class Account:
<<<<<<< HEAD
 def __init__(self, initial_balance=0, transaction_limit_hour=12):
=======
 def __init__(self, initial_balance=0, transaction_limit_hour=13):
>>>>>>> 16bdc6b776b89e38c9e2f1b59df1f12e6ea5f77e
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
<<<<<<< HEAD
    self.balance -= amount
=======
    self.balance -= amount
>>>>>>> 16bdc6b776b89e38c9e2f1b59df1f12e6ea5f77e
