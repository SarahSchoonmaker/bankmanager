
from Account import Account
from BankUtility import BankUtility

#  The bank class initializes an array to store all the existing accounts. 
class Bank:
    def __init__(self):

        self.existingAccounts=[]
#  Create count function gets user input, generates a random number for the account, and puts
#  the user account information or user object into the existing accounts array if there are less
# than 100 accounts. 
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
        
    # This method finds and returns the account details if it exists. 
    # User provides their account number to search. 
    def findAccount(self):
        getAccount = float(input("Please provide your account number: "))
        for i in range(len(self.existingAccounts)):
            
            if self.existingAccounts[i].accountNumber == int(getAccount):
                print("Success. Account number found for: ", 
                self.existingAccounts[i].accountNumber,'\n',
                "The current balance is: ",
                self.existingAccounts[i].balance,'\n', "The PIN is: ",self.existingAccounts[i].pin,'\n',
                "First name:", self.existingAccounts[i].firstName,'\n', 
                "Last name:", self.existingAccounts[i].lastName)
            
            else:
                print("Could not find the account.")
                
    # Removing the account from the existing accounts object. 
     
    def removeAccountFromBank(self):
        removeAccount = int(input("Provide the account # to remove: "))
        
        for i in range(len(self.existingAccounts)):
            
            if self.existingAccounts[i].accountNumber == int(removeAccount):
                self.existingAccounts.remove(self.existingAccounts[i])
                print("Accout successfully removed")

        
    print("Could not find the account.")   

#  Transfer money between accounts that the user specifies and returning the updated balances. 

    def transferBetweenAccounts(self):
        transferFrom = input("Provide the account number to transfer from: ")
        transferTo = input("Provide the account number to transfer to: ")
        amount = int(input("Amount transferred: "))
        
        for i in range(len(self.existingAccounts)):

            for j in range(len(self.existingAccounts)):
                if self.existingAccounts[i].accountNumber == int(transferFrom):
                    if (self.existingAccounts[j].accountNumber == int(transferTo)):
                        if (self.existingAccounts[i].balance >= amount):
                            self.existingAccounts[i].balance -= amount
                            self.existingAccounts[j].balance += amount
                            print("Transferred funds. The new balances are: ", 
                            self.existingAccounts[i].accountNumber,":",
                            self.existingAccounts[i].balance, self.existingAccounts[j].accountNumber,":", self.existingAccounts[j].balance)
                        else:
                            print("Insufficient Funds.")
                    

                        