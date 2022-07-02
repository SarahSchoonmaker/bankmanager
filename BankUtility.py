#  import random to generate random numbers.
import random


class BankUtility:
    
    def __init__(self):
        pass
    
    # Generate a random 8 digit number that will be used as a user's account number.
    # The other methods are helper methods that can be used if needed. 

    @staticmethod   
    def generateRandomInt(self):

        self.secNum = int(random.SystemRandom().random()*10**8)
        return self.secNum


    def promptUserForString(prompt):
        getString = str(input("Input a word"))
        return getString
        

    def promptUserForPositiveNumber(prompt):
        getPositiveInteger = float(input("Input a positive number"))
        return getPositiveInteger
        

    def convertFromDollarsToCents(self):  
        self.dollar = 100.50       
        cents = self.dollar / 100
        return cents
        

    '''
    Checks if a given string is a number (long)
    This does NOT handle decimals.

    YOU DO NOT NEED TO CHANGE THIS METHOD
    THIS IS FREE FOR YOU TO USE AS NEEDED

    @param numberToCheck String to check
    @return true if the String is a number, false otherwise
    '''
    def checkInt(self):
        self.inputNum = input("Enter a value to see if it is an integer")
        if type(self.inputNum) == type(self.inputNum):
            print("Input is an number.")

        return -1
            
