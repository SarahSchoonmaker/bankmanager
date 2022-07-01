import unittest
from Bank import *
from Account import *
from BankManager import *


class Test_Methods(unittest.TestCase):
    
# Testing the Account Class:

    def setUp(self):
        self.account = Account(0,accountNumber=12345678,firstName="Sarah",lastName="Sch",
        social=1234,pin=1234)

    def test_deposit(self): 
        self.account.deposit(500)
        getBalance = self.account.get_balance()
        self.assertEqual(getBalance, 800)
        


        #make the account
        #deposit 500
        #get the balance
        #check to make sure the balance is 500

  
#     def test_deposits2(self):
#         self.assertFalse(self.deposit(100, 500), -1)

#     def test_withdraw(self):
#        self.assertTrue(self.withdraw(1000), 500)

#     def test_withdraw2(self):
#         self.assertTrue(self.withdraw(1000), -100)

#     def test_isValidPin(self):
#         self.assertTrue(self.isValidPIN(self,getPin=0), self.test_isValidPin )

#     def test_isValidPin2(self):
#         self.assertFalse(self.isValidPIN(1234), 1111)

# #  Testing the Bank class:

#     def test_addAccountToBank(self):
#         self.assertFalse(self.createAccounts, -1)

#     def test_addAccountToBank2(self):
#         self.assertTrue(self.createAccounts)
       

#     def test_removeAccountFromBank(self):
#         self.assertEqual(self.removeAccountFromBank(self.removeAccountFromBank), 0)

#     def removeAccountFromBank(self):
#         self.assertEqual(self.removeAccountFromBank(self.removeAccountFromBank), 0)

#     def test_findAccount(self):
#         self.assertTrue(self.createAccounts, 1)

#     def test_findAccount2(self):
#         self.assertFalse(self.createAccounts, 0)

# # Testing Bank Utility

#     def test_isNumeric(self):
#         self.assertTrue(self.isNumeric(10))

#     def test_isNumberic2(self):
#         self.assertFalse(self.isNumeric("String"))

#     def test_convertFromDollarsToCents(self):
#         self.assertEqual(self.convertFromDollarsToCents(16), .16)

#     def test_convertFromDollarsToCents2(self):
#         self.assertTrue(self.convertFromDollarsToCents(16), .16)

#     def test_generateRandomInteger(self):
#         self.assertTrue(self.generateRandomInt)

#     def test_generateRandomInteger2(self):
#         self.assertTrue(self.generateRandomInt)

if __name__ == '__main__':
    unittest.main()