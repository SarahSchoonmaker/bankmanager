import unittest

from Bank import Bank
from Account import *
from BankUtility import *


class Test_Methods(unittest.TestCase):
    
# Testing the Account Class:

    def setUp(self):
        self.account = Account(0,accountNumber=12345678,firstName="Sarah",lastName="Sch",
        social=1234,pin=1234)
        self.bank = Bank()
        self.bankUtility = BankUtility()
        
    def test_deposit(self): 
        self.account.deposit(500)
        getBalance = self.account.get_balance()
        self.assertEqual(getBalance, 500)
        
        #make the account
        #deposit 500
        #get the balance
        #check to make sure the balance is 500
  
    def test_deposits2(self):
        self.account.deposit(1000)
        getBalance = self.account.get_balance()
        self.assertEqual(getBalance, 1000)

    def test_withdraw(self):
        self.account.deposit(1000)
        # Enter 500 for the withdrawal amout for the test to pass
        self.account.withdraw()
        getBalance = self.account.get_balance()
        self.assertEqual(getBalance, 500)
        
    def test_withdraw2(self):
        self.account.deposit(0)
        # Enter 500 for the withdrawal input
        self.account.withdraw()
        getBalance = self.account.get_balance()
        self.assertFalse(getBalance, "Insufficient funds.")

    def test_isValidPin(self):
        self.account.isValidPIN(getPin=1234)
        currentPin = self.account.get_pin()
        self.assertTrue(currentPin, 1234)

    def test_isValidPin2(self):
        currentPin=self.account.isValidPIN(self.account.get_pin)
         
        self.assertNotEqual(currentPin, 1111)

# #  Testing the Bank class:

    def test_addAccountToBank(self):
        self.bank.createAccounts(firstName="sarah", lastName="scho", social=1234,pin=1234)

        self.assertEqual(self.account.accountNumber, self.account.get_accountNumber())


    def test_addAccountToBank2(self):
        currentAccount = self.bank.createAccounts(firstName="sarah", lastName="scho", social=1234,pin=1234)
        
        self.assertNotEqual(currentAccount, 11111111)
       

    def test_removeAccountFromBank(self):
        self.bank.removeAccountFromBank(12345678)
        getAccountNumber=self.account.get_accountNumber()
        self.assertEqual(getAccountNumber, 12345678)

    def removeAccountFromBank(self):
        self.bank.removeAccountFromBank(12345678)
        getAccountNumber=self.account.get_accountNumber()
        self.assertFalse(getAccountNumber, 0)

    def test_findAccount(self):
        self.bank.findAccount(12345678)
        findAccount = self.account.get_accountNumber()
        self.assertTrue(findAccount, 12345678)

    def test_findAccount2(self):
        self.bank.findAccount(0)
        findAccount = self.account.accountNumber
        self.assertNotEqual(findAccount, 0)

# # Testing Bank Utility

    def test_isNumeric(self):
        
        newNum = self.bankUtility.checkInt()
        
        self.assertEqual(type(newNum), int)

    def test_isNumberic2(self):
        
        newNum = self.bankUtility.checkInt()
        
        self.assertNotEqual(type(newNum), str)

    def test_convertFromDollarsToCents(self):
        converting = self.bankUtility.convertFromDollarsToCents()
        self.assertTrue(type(converting), float)

    def test_convertFromDollarsToCents2(self):
        converting = self.bankUtility.convertFromDollarsToCents()
        self.assertNotEqual(type(converting), str)

    def test_generateRandomInteger(self):
        newRandomInt = self.bankUtility.generateRandomInt(self)
        self.assertTrue(type(newRandomInt) == int)

    def test_generateRandomInteger2(self):
        newRandomInt = self.bankUtility.generateRandomInt(self)
        self.assertFalse(type(newRandomInt) == str)

if __name__ == '__main__':
    unittest.main()