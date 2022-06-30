from typing_extensions import Self
from Bank import *
from BankUtility import *



class Account:
    # Account attributes that will be created with each new user and account. 
    def __init__(self, balance, accountNumber, firstName, lastName, social, pin):
        self.balance = balance
        self.accountNumber=accountNumber
        self.firstName = firstName
        self.lastName = lastName
        self.social = social
        self.pin = pin

    # Getter and Setter Methods

    def set_balance(self):
        self.balance = 0
    
    def set_accountNumber(self, generateRandomInt):
        self.accountNumber = generateRandomInt()

    def set_firstName(self, firstName):
        self.firstName = firstName

    def set_lastName(self, lastName):
        self.lastName = lastName
    
    def set_social(self, social):
        self.social = social
    
    def set_pin(self, pin):
        self.pin = pin
    
    def get_balance(self):
        return self.balance
    
    def get_accountNumber(self):
        return self.accountNumber
    
    def get_firstName(self):
        return self.firstName
    
    def get_lastName(self):
        return self.lastName
    
    def get_social(self):
        return self.social
    
    def get_pin(self):
        return self.pin

    def print_current_balance(self):
        print("Your current balance is: ", self.balance)
        
# Methods for account functions: deposit, withdraw, checking and changing PIN, and ATM withdrawal. 
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount 
        print("Deposit is successful and the new balance is ", self.balance)
       
  
    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if (self.balance >= amount):
            self.balance -= amount
            print("The withdrawal is successful and the new balance is: ", self.balance)
        else:
            print("Insufficient funds.")  
    
    #  Checking if the pin is valid
    def isValidPIN(self, getPin):
        
        if (getPin == self.pin):
             print("Your PIN is valid")
        else:
            print("Invalid PIN")
# Changing the PIN. 
    def changePin(self):
        
        getNewPin = input("Please provide a new PIN: ")
        confirmNewPin = input ("Enter your PIN again to confirm: ")

        if getNewPin == confirmNewPin:
            self.set_pin(getNewPin) 
            print("PIN successfully changed. ")
        else:
            print("Invalid PIN entry, try again")
            self.changePin()

# ATM withdrawal function 
    def ATMWithdrawal(self):
        pass
           
    
    # all objects have a toString method - this indicates you are providing
    # your own version
    def __repr__(self):
      pass

## ISSUES:
# Change pin isn't working fully anymore.
# For deposit, withdrawal, and transfer, how to look up the account the user wants to
# do something with. For transfer, how to look up the from and to accounts and update the balances. 
