from Account import *
from Bank import *
from CoinCollector import *

class BankManager:
    def __init__(self):
        # This is where you will implement your ‘main’ method and start
        # the program from.  The BankManager class should create an instance
        # of a Bank object when the program runs and use that instance to
        # manage the Accounts in the bank
        @staticmethod  
        
        def promptForAccountNumberAndPIN(pin):
            self.pin = pin
            getAccountNumber = input("Please input the account # and press Enter: ")
            getPin = input("Please input the pin number and press enter: ")
            

        if __name__ == "__main__":
            BankManager()


    
    active = True
    while active:
        userInput = int(input("""Input the number for your choice: 1) Open Account, 2) Get account infomration and balance, 3) Change PIN,
        4) Deposit money in account, 5) Transfer money between accounts, 6) Withdraw Money from account, 7) ATM withdrawal,
        8) Deposit Change, 9) Close an account, 10) Add monthly interests to all accounts, 11) End Program. """))
        
        if userInput == 1:
            Bank.createAccounts()
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
            active = False
            print("Program closing...")
            break
            


        
        # implement promptForAccountNumberAndPIN here
        # takes one parameter, a Bank object that represents the bank.
        # The method should prompt the user to enter an account number
        # and then try to find a matching account with that account number
        # in the bank.
        
        # be sure to change this as needed

