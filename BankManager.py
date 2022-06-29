
from multiprocessing.managers import BaseManager
from Account import *
from Bank import *
from CoinCollector import *

class BankManager:
    def __init__(self):
        self.bank = Bank()
        
    
    @staticmethod  
    def promptForAccountNumberAndPIN(pin):
        
        getAccountNumber = input("Please input the account # and press Enter: ")
        getPin = input("Please input the pin number and press enter: ")
        
        for i in existingAccounts:
            if (getAccountNumber == getAccountNumber):
                print("Account ", account, "found.")
                pinInput = input("Please enter your pin number")
            else:
                print("Account not found")

            if (getPin == pin):
                print(existingAccounts)
            else:
                print("Invalid PIN")
                return 0

    def main(self):
        active = True
        
        while active:
            userInput = int(input("""Please enter a number to select an option:  
            1) Open Account
            2) Get account infomration and balanc3
            3) Change PIN
            4) Deposit money in account
            5) Transfer money between accounts
            6) Withdraw Money from account
            7) ATM withdrawal
            8) Deposit Change
            9) Close an account
            10) Add monthly interests to all accounts
            11) End Program  """))
            
            if userInput == 1:
                self.bank.createAccounts()
            if userInput == 2:
                Account.print_current_balance()
            if userInput == 3:
                Account.isValidPIN()
            if userInput == 4:
                Account.deposit()
            if userInput == 5:
                # Not sure how to do this yet
                pass
            if userInput == 6:
                Account.withdraw()
            if userInput == 7:
                Account.withdraw()
            if userInput == 8:
                CoinCollector.parseChange()
            if userInput == 9:
                Bank.removeAccountFromBank()
            if userInput == 10:
                Bank.addMonthlyInterest()
            if userInput == 11:
                
                print("Program closing...")
            
                active=False       
                
     
if __name__ == "__main__":
    bank_manager = BankManager()
    bank_manager.main()           
        
    # if __name__ == "__main__":
            
    #     if userInput != 11:
    #         BaseManager()
        


        
        # implement promptForAccountNumberAndPIN here
        # takes one parameter, a Bank object that represents the bank.
        # The method should prompt the user to enter an account number
        # and then try to find a matching account with that account number
        # in the bank.
        
        

