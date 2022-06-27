import random
class Bank:
    def __init__(self):


        self.existingAccounts=[]
        
        self.newAccount = []
  
    def addAccountToBank(self, firstName, lastName, social, pin):

        account = random.randint(1,5)

        
        self.account =account
        self.firstName = firstName
        self.lastName = lastName
        self.social = social
        self.pin = pin
    

        self.newAccount.append(account, firstName, lastName, social, pin)
        if len(self.existingAccounts) <100:
            self.existingAccounts.append(self.newAccount)
            print("Account Created!")
        else:
            print("No more accounts available.")
        

    def removeAccountFromBank(self,account):
    
        for i in self.existingAccounts:
            if account == self.existingAccounts[i]:
                self.existingAccounts.remove(self.existingAccounts[i])

            print("Account has been deleted")


    
    def findAccount(accountNumber):
        
        return  # be sure to change this as needed
    

    def addMonthlyInterest(percent):
    
        return 0