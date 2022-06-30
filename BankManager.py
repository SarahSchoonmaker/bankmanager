from asyncio.windows_events import NULL
from Bank import Bank
from Account import Account
from CoinCollector import CoinCollector

class BankManager:
    def __init__(self):
        self.bank = Bank()
        self.account = Account(0,accountNumber=0,firstName=0,lastName=0,social=0,pin=0)
        self.coinCollector = CoinCollector()

    
    @staticmethod  
    def promptForAccountNumberAndPIN(self):
        
        getAccountNumber = int(input("Please input the account # and press Enter: "))
        getPin = input("Please input the pin number and press enter: ")

        
        
        for i in self.bank.existingAccounts:
            if ((getAccountNumber == i.accountNumber) and (getPin == i.pin)):
                print("You Account Number is: ", getAccountNumber, "found.")
                print("Your PIN is: ", i.pin)
                return i
            else:
                print("Invalid PIN or Account Number.")
    
        return NULL
                
       

    def main(self):
        active = True
        
        while active:
            userInput = int(input("""Please enter a number to select an option:  
            1) Open Account
            2) Get account information and balance
            3) Change PIN
            4) Deposit money in account
            5) Transfer money between accounts
            6) Withdraw Money from account
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
                self.account.deposit()
            if userInput == 5:
                self.bank.transferBetweenAccounts()
            if userInput == 6:
                self.account.withdraw()
            if userInput == 7:
                self.account.ATMWithdrawal()
            if userInput == 8:
                self.coinCollector.parseChange()
            if userInput == 9:
                self.bank.removeAccountFromBank()
            if userInput == 11:
                print("Program closing...")
            
                active=False       
                
     
if __name__ == "__main__":
    bank_manager = BankManager()
    bank_manager.main()  