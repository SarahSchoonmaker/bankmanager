import unittest
from Bank import *
from Account import *
from BankManager import *


class Test_Methods(unittest.TestCase):
    
# Testing the Account Class:

    def test_deposit(self): 
               
        self.assertEqual(Account.deposit(0,200), 200)
  
    def test_deposits2(self):
        self.assertFalse(Account.deposit(100, 500), -1)

    def test_withdraw(self):
       self.assertTrue(Account.withdraw(1000), 500)

    def test_withdraw2(self):
        self.assertTrue(Account.withdraw(1000), -100)

    def test_isValidPin(self):
        self.assertTrue(Account.isValidPIN(self,getPin=0), self.test_isValidPin )

    def test_isValidPin2(self):
        self.assertFalse(Account.isValidPIN(1234), 1111)

#  Testing the Bank class:

    def test_addAccountToBank(self):
        self.assertFalse(Bank.createAccounts, -1)

    def test_addAccountToBank2(self):
        self.assertTrue(Bank.createAccounts)
       

    def test_removeAccountFromBank(self):
        self.assertEqual(Bank.removeAccountFromBank(self.removeAccountFromBank), 0)

    def removeAccountFromBank(self):
        self.assertEqual(Bank.removeAccountFromBank(self.removeAccountFromBank), 0)

    def test_findAccount(self):
        self.assertTrue(Bank.findAccount)

    def test_findAccount2(self):
        self.assertFalse(Bank.createAccounts, 0)

# Testing Bank Utility

    def test_isNumeric(self):
        self.assertTrue(BankUtility.isNumeric(10))

    def test_isNumberic2(self):
        self.assertFalse(BankUtility.isNumeric("String"))

    def test_convertFromDollarsToCents(self):
        self.assertEqual(BankUtility.convertFromDollarsToCents(16), .16)

    def test_convertFromDollarsToCents2(self):
        self.assertTrue(BankUtility.convertFromDollarsToCents(16), .16)

    def test_generateRandomInteger(self):
        self.assertTrue(BankUtility.generateRandomInt)

    def test_generateRandomInteger2(self):
        self.assertTrue(BankUtility.generateRandomInt)

if __name__ == '__main__':
    unittest.main()