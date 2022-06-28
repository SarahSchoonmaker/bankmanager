from BankUtility import *


class Account:
    # add your attributes here
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

    # add methods as getters and setters for attributes
       
    def print_current_balance(self):
        print("Your current balance is: ", self.balance)
        

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += self.balance + amount 
        print("Deposit is successful and the new balance is ", self.balance)
       
  
    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print("The withdrawal is successful and the new balance is: ", self.balance)
            
    
    def isValidPIN(pin):
        
        # implement isValidPIN here
        
        return False  # be sure to change this
    

    
    # all objects have a toString method - this indicates you are providing
    # your own version
    def __repr__(self):
        return "" # change this as needed

