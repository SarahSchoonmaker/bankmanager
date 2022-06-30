from Account import *
from BankUtility import *


class Bank:
    def __init__(self):

        self.existingAccounts=[]

    def createAccounts(self):
        firstName = str(input("Input your first name and press Enter: "))
        lastName = str(input("Input your last name and press Enter: "))
        social = int(input("Input your social security # and press Enter: "))
        pin = int(input("Create a 4 digit pin and press Enter: "))

        accountNumber = BankUtility.generateRandomInt(self)
        print("Your new account number is: " +str(accountNumber))
        
        account = Account(0, accountNumber, firstName, lastName, social, pin)
    
        if (len(self.existingAccounts) < 100):
            self.existingAccounts.append(account)

            print("Account created successfully!")
        else:
            print("No more accounts available.")
        
    
    def findAccount(self):
        getAccount = float(input("Please provide your account number: "))
        for i in range(len(self.existingAccounts)):
            # print(self.existingAccounts[i].firstName)
            # print(self.existingAccounts[i].accountNumber)
            if self.existingAccounts[i].accountNumber == int(getAccount):
                print("Success. Account number found for: ", 
                self.existingAccounts[i].accountNumber,'\n',
                "The current balance is:",
                self.existingAccounts[i].balance,'\n', "The PIN is: ",self.existingAccounts[i].pin,'\n',
                "First name:", self.existingAccounts[i].firstName,'\n', 
                "Last name:", self.existingAccounts[i].lastName)
            else:
                print("Account number not found for account ", self.existingAccounts[i].accountNumber)
                
    
    def removeAccountFromBank(self):
        removeAccount = input("Provide the account # to remove: ")
        for i in range(len(self.existingAccounts)):
            if self.existingAccounts[i].accountNumber == int(removeAccount):
                self.existingAccounts.remove(self.existingAccounts[i])
                print("Accout successfully removed")

            else:
                print("Could not find the account your are looking for")

    def transferBetweenAccounts(self):
        transferFrom = input("Provide the account number to transfer from")
        transferTo = input("Provide the account number to transfer to")
        amount = input("Amount transferred: ")
        for i in range(len(self.existingAccounts)):
            if self.existingAccounts[i].balance > amount:
                self.existingAccounts[i] - amount
                self.existingAccounts[i].balance + amount
                print("Transfer complete. The new balances of the accounts are: ")
            else:
                print("""The transfer cannot be completed. Check the account balances to ensure
                there are enough funds.""")