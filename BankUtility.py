
import random

class BankUtility:
    
    def __init__(self):
        pass
    
    @staticmethod   
    def generateRandomInt(self):

        secNum = random.SystemRandom().random()
        print("You Accuont Number is: ", secNum)


    def promptUserForString(prompt):
        # implement promptUserForString here
        
        return 0

    def promptUserForPositiveNumber(prompt):
        
        # implement promptUserForPositiveNumber here
        
        return 0.0 # be sure to change this
        

    def convertFromDollarsToCents(amount):        
        # implement convertFromDollarsToCents here     
        
        return 0 # be sure to change as needed

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
