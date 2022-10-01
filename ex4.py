"""
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method  which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.
"""

class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def Withdrawal(self, amount):
        self.balance -= amount
    
    def bank_fees(self):
        self.balance -= self.balance * 5 / 100
        
    def display(self):
        print(f"Account Number: {self.account_number}\nName = {self.name}\nBalance = {self.balance}")

        