
from Account import Account
from BankUtility import BankUtility

#  The bank class initializes an array to store all the existing accounts. 
class Bank:
    def __init__(self):

        self.existingAccounts=[]
#  Create count function gets user input, generates a random number for the account, and puts
#  the user account information or user object into the existing accounts array if there are less
# than 100 accounts. 
    def createAccounts(self, firstName, lastName, social, pin):
        
        
        
        accountNumber = BankUtility.generateRandomInt(self)
        account = Account(0, accountNumber, firstName, lastName, social, pin)
        print("Your new account number is: " +str(accountNumber))
        if (len(self.existingAccounts) < 100):
            self.existingAccounts.append(account)

            print("Account created successfully!")
        else:
            print("No more accounts available.")
        
    # This method finds and returns the account details if it exists. 
    # User provides their account number to search. 
    def findAccount(self, getAccount):
        
        for i in range(len(self.existingAccounts)):
            
            if self.existingAccounts[i].accountNumber != int(getAccount):
                print("Cannot find that account number.")
            
            if self.existingAccounts[i].accountNumber == int(getAccount):
                print("Success. Account number found for: ", 
                self.existingAccounts[i].accountNumber,'\n',
                "The current balance is: ",
                self.existingAccounts[i].balance,'\n', "The PIN is: ",self.existingAccounts[i].pin,'\n',
                "First name:", self.existingAccounts[i].firstName,'\n', 
                "Last name:", self.existingAccounts[i].lastName)
            
                
    # Removing the account from the existing accounts object. 
     
    def removeAccountFromBank(self, removeAccount):

        for i in range(len(self.existingAccounts)):
            if self.existingAccounts[i].accountNumber != int(removeAccount):
                print("Could not find the account you are looking to remove.")

            if self.existingAccounts[i].accountNumber == int(removeAccount):
                self.existingAccounts.remove(self.existingAccounts[i])
                print("Accout successfully removed")

               

#  Transfer money between accounts that the user specifies and returning the updated balances. 

    def transferBetweenAccounts(self, transferFrom, transferTo, amount):
        
        for i in range(len(self.existingAccounts)):
            for j in range(len(self.existingAccounts)):
                if self.existingAccounts[i].accountNumber == transferFrom:
                    if self.existingAccounts[j].accountNumber == transferTo:
                        if self.existingAccounts[i].balance >= amount:
                            print(self.existingAccounts[i].balance)
                            self.existingAccounts[i].balance -= amount
                            self.existingAccounts[j].balance += amount
                            print("Transferred funds. The new balances are: ", 
                            self.existingAccounts[i].accountNumber,":",
                            self.existingAccounts[i].balance, self.existingAccounts[j].accountNumber,":", 
                            self.existingAccounts[j].balance)   
                        else:
                            print("Insufficient Funds. Deposit more funds in the account and try again.")
                    


                        