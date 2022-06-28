import random
class Bank:
    def __init__(self):


        self.existingAccounts=[]
        
  
    def createAccounts(self, firstName, lastName, social, pin):
        firstName = str(input("Input your first name and press Enter: "))
        lastName = str(input("Input your last name and press Enter: "))
        social = int(input("Input your social security # and press Enter: "))
        pin = int(input("Create a 4 digit pin and press Enter: "))

        accountNumber = random.randint(1,5)
    
        self.accountNumber =accountNumber
        self.firstName = firstName
        self.lastName = lastName
        self.social = social
        self.pin = pin
    
        if (len(self.existingAccounts) <=100):
            self.existingAccounts.append([accountNumber, firstName, lastName, social, pin])

            print("Account created successfully!")
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