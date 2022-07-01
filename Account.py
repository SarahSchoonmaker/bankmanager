

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
    def deposit(self, amount):
    
        self.balance += amount 

  
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
        
        getNewPin = int(input("Please provide a new PIN: "))
        confirmNewPin = int(input ("Enter your PIN again to confirm: "))

        if getNewPin == confirmNewPin:
            self.set_pin(getNewPin)
            self.pin = getNewPin
            print("PIN successfully changed. ")
        else:
            print("Invalid PIN entry, try again")
            self.changePin()

    # ATM withdrawal function. Counts how many 20, 10, and 5 dollar bills divide into the amount
    # and subtracts that amount from the amount given. Then returns the updated balance. 
     
    def ATMWithdrawal(self):
        amount = float(input("Enter the amount to withdraw from the ATM: "))
        if self.balance < amount:
            print("Insufficient funds")
            return

        if (amount < 5 or amount > 1000) or (amount % 5 !=0):
            twentyDollarBill = amount // 20
            tenDollarBills = amount // 10
            fiveDollarBills = amount // 5

            print("20 dollar bills: ", twentyDollarBill, "10 dollar bills:", 
            tenDollarBills, "5 dollar bills: ", fiveDollarBills)
            
            multiple1 = twentyDollarBill * 20 
            multiple2 = tenDollarBills *10
            multiple3 = fiveDollarBills * 5
            
            self.balance = amount - multiple1 
            self.balance = amount - multiple2
            self.balance = amount - multiple3

            print("ATM withdrawal successful. The new balance is: ", self.balance)
        else:
            print("Invalid entry. Try again. Provide a number greater than 5 and less than 1000 that is divisible by 5.")
    
    
