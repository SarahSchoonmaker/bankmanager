
class Account:
    # add your attributes here
    def __init__(self, amount):
        self.amount = amount
        self.balance = 0 

    # add methods as getters and setters for attributes
       
    def print_current_balance(self):
        print("Your current balance is: ", self.balance)

    def deposit(self, funds):
        self.balance += funds
    
  
    def withdraw(self, funds):
        if funds > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= funds
  
    
    def isValidPIN(pin):
        
        # implement isValidPIN here
        
        return False  # be sure to change this
    

    
    # all objects have a toString method - this indicates you are providing
    # your own version
    def __repr__(self):
        return "" # change this as needed

