from BankUtility import *
from Account import *

class Bank:
    def __init__(self):

        self.existingAccounts=[]

    def createAccounts(self):
        firstName = str(input("Input your first name and press Enter: "))
        lastName = str(input("Input your last name and press Enter: "))
        social = int(input("Input your social security # and press Enter: "))
        pin = int(input("Create a 4 digit pin and press Enter: "))

        accountNumber = BankUtility.generateRandomInt(self)
    
        account = Account(0, accountNumber, firstName, lastName, social, pin)
    
        if (len(self.existingAccounts) < 100):
            self.existingAccounts.append(account)

            print("Account created successfully!")
        else:
            print("No more accounts available.")
        
    def removeAccountFromBank(self):
    
        # for i in self.existingAccounts:
        #     if (account == self.exc:\Users\srsch\AppData\Local\Programs\Microsoft VS Code\resources\app\out\vs\code\electron-browser\workbench\workbench.htmlistingAccounts[i]):
        #         self.existingAccounts.remove(self.existingAccounts[i])

        #     print("Account has been deleted")
        pass  
    
    def findAccount(self):
        getAccount = float(input("Please provide your account number: "))
        for i in range(len(self.existingAccounts)):
                
                print("i", i)
                print(type(getAccount))
                print(type(self.existingAccounts[i][1]))
            
                if (Account.get_accountNumber == getAccount):
                    print("success")

    def addMonthlyInterest(percent):
    
        pass