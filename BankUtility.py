#  import random to generate random numbers.
import random

class BankUtility:
    
    def __init__(self):
        pass
    
    # Generate a random 8 digit number that will be used as a user's account number.
    # The other methods are helper methods that can be used if needed. 

    @staticmethod   
    def generateRandomInt(self):

        secNum = int(random.SystemRandom().random()*10**8)
        return secNum


    def promptUserForString(prompt):
        getString = str(input("Input a word"))
        return getString
        

    def promptUserForPositiveNumber(prompt):
        getPositiveInteger = float(input("Input a positive number"))
        return getPositiveInteger
        

    def convertFromDollarsToCents(dollar):         
        cents = float(dollar) * 100
        return cents
        

    '''
    Checks if a given string is a number (long)
    This does NOT handle decimals.

    YOU DO NOT NEED TO CHANGE THIS METHOD
    THIS IS FREE FOR YOU TO USE AS NEEDED

    @param numberToCheck String to check
    @return true if the String is a number, false otherwise
    '''
    def isNumeric(numberToCheck):
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False
