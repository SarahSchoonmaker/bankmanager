from Bank import Bank
from Account import Account
from CoinCollector import CoinCollector


# Bank manager initializes objects for bank, account, and coin collector. 
class BankManager:
    def __init__(self):
        self.bank = Bank()
        self.account = Account(0,accountNumber=0,firstName=0,lastName=0,social=0,pin=0)
        self.coinCollector = CoinCollector()

    # Checking if the bank account and pin exist. 
    @staticmethod  
    def promptForAccountNumberAndPIN(self):
        
        getAccountNumber = int(input("Please input the account # to log into the bank and press Enter: "))
        getPin = int(input("Please input your pin number and press Enter: "))

        for i in self.bank.existingAccounts:

            if ((getAccountNumber == i.accountNumber) and (getPin == i.pin)):
                print("You Account Number is: ", getAccountNumber, "found.")
                print("Your PIN is: ", i.pin)
                return i
            else:
                print("Invalid PIN or Account Number.")

        return 0

#  The main method produces a list of options until the user types 11 to exit the program. 
# Methods are called based on which item the user selects and the user must sign in successfully 
# to the account to execute most options. 

    def main(self):
        active = True
        
        while active:
            print("Welcome to the Bank!")
            userInput = int(input("""Please enter a number to select an option:  
            1) Open Account
            2) Get account information and balance
            3) Change PIN
            4) Deposit money in account
            5) Transfer money between accounts
            6) Withdraw money from account
            7) ATM withdrawal
            8) Deposit Change
            9) Close an account
            11) Exit the bank """))
        
            if  userInput == 1:
                firstName = str(input("Input your first name and press Enter: "))
                lastName = str(input("Input your last name and press Enter: "))
                social = int(input("Input your social security # and press Enter: "))
                pin = int(input("Create a 4 digit pin and press Enter: "))
                self.bank.createAccounts(firstName, lastName, social, pin)
            if userInput == 2:
                getAccount = float(input("Please provide your the account number to find: "))
                self.bank.findAccount(getAccount)
            if userInput == 3:
                i = self.promptForAccountNumberAndPIN(self)
                if i != 0:
                    i.changePin()
            if userInput == 4:
                i = self.promptForAccountNumberAndPIN(self)
                if i != None:
                    amount = float(input("Enter amount to deposit: "))
                    i.deposit(amount)
                    print("Deposit is successful and the new balance is ", i.balance)
            if userInput == 5:
                i = self.promptForAccountNumberAndPIN(self)
                if i != None:
                    transferFrom = input("Provide the account number to transfer from: ")
                    transferTo = input("Provide the account number to transfer to: ")
                    amount = input("Provide the amount to transfer: ")
                    self.bank.transferBetweenAccounts(transferFrom, transferTo, amount)
                    
            if userInput == 6:
                i = self.promptForAccountNumberAndPIN(self)
                if i != None:
                    i.withdraw()
            if userInput == 7:
                i = self.promptForAccountNumberAndPIN(self)
                if i != None:
                    amount = float(input("Enter the amount to withdraw from the ATM: "))
                    i.ATMWithdrawal(amount)
            if userInput == 8:
                i = self.promptForAccountNumberAndPIN(self)
                if i != None:
                    amount = self.coinCollector.parseChange(amount)
                    if amount is not None:
                        i.deposit(amount)
            if userInput == 9:
                i = self.promptForAccountNumberAndPIN(self)
                if i != None:
                   removeAccount = int(input("Provide the account # to remove: "))
                   self.bank.removeAccountFromBank(removeAccount)
            if userInput == 11:
                print("Program closing...")
            
                active=False       

# Calling the bank manager and main classes.   
     
if __name__ == "__main__":
    
    bank_manager = BankManager()
    bank_manager.main()  