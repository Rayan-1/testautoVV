import datetime
import pytest
from account import Account

# Test Unitary
def test_deposit():
    account = Account(initial_balance=100) 
    account.deposit(50) 
    assert account.balance == 150 

# Test Unitary
def test_withdraw():
    account = Account(initial_balance=100) #iniciamos com 100 reais na conta
    account.withdraw(50) #  sacamos 50$
    assert account.balance == 50  

# Integration Test
def test_deposit_and_withdraw():
    account = Account(initial_balance=100) 
    account.deposit(50)  
    account.withdraw(30) 
    assert account.balance == 120 


