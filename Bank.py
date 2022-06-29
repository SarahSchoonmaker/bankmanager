from BankUtility import *
from Account import Account

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
        
    def removeAccountFromBank(self, account):
    
        for i in self.existingAccounts:
            if (account == self.existingAccounts[i]):
                self.existingAccounts.remove(self.existingAccounts[i])

            print("Account has been deleted")
           
    
    def findAccount(self, account):
        for pos,inner_ar in enumerate(account):
            if len(inner_ar)==1:
                for i,inner_ar2 in enumerate(account):
                    if i!=pos and any(c for c in inner_ar2 for c in inner_ar):
               


        for i in self.existingAccounts:
            if (account == self.existingAccounts[i]): 
                print("Your account details are: ", account)
        else:
            print("Could not find your account. Please create an account and try again.")

    def addMonthlyInterest(percent):
    
        pass