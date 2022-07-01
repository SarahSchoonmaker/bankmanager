from asyncio.windows_events import NULL
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
        
        getAccountNumber = int(input("Please input the account # and press Enter: "))
        getPin = int(input("Please input the pin number and press enter: "))

        for i in self.bank.existingAccounts:

            if ((getAccountNumber == i.accountNumber) and (getPin == i.pin)):
                print("You Account Number is: ", getAccountNumber, "found.")
                print("Your PIN is: ", i.pin)
                return i
        else:
            print("Invalid PIN or Account Number.")

        return NULL

#  The main method produces a list of options until the user types 11 to exit the program. 
# Methods are called based on which item the user selects. 

    def main(self):
        active = True
        
        while active:
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
            
            if userInput == 1:
                self.bank.createAccounts()
            if userInput == 2:
                self.bank.findAccount()
            if userInput == 3:
                i = self.promptForAccountNumberAndPIN(self)
                if i != NULL:
                    i.changePin()
            if userInput == 4:
                i = self.promptForAccountNumberAndPIN(self)
                if i != NULL:
                    amount = float(input("Enter amount to deposit: "))
                    i.deposit(amount)
                    print("Deposit is successful and the new balance is ", i.get_balance())
            if userInput == 5:
                i = self.promptForAccountNumberAndPIN(self)
                if i != NULL:
                    self.bank.transferBetweenAccounts()
            if userInput == 6:
                i = self.promptForAccountNumberAndPIN(self)
                if i != NULL:
                    i.withdraw()
            if userInput == 7:
                i = self.promptForAccountNumberAndPIN(self)
                if i != NULL:
                    i.ATMWithdrawal()
            if userInput == 8:
                i = self.promptForAccountNumberAndPIN(self)
                if i != NULL:
                    amount = self.coinCollector.parseChange()
                    if amount is not None:
                        i.deposit(amount)
            if userInput == 9:
                i = self.promptForAccountNumberAndPIN(self)
                if i != NULL:
                   self.bank.removeAccountFromBank()
            if userInput == 11:
                print("Program closing...")
            
                active=False       

# Calling the bank manager and main classes.   
     
if __name__ == "__main__":
    bank_manager = BankManager()
    bank_manager.main()  