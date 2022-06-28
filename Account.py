
class Account:
    # add your attributes here
    def __init__(self, amount):
        self.amount = amount
        self.balance = 0 

    

    # add methods as getters and setters for attributes
       
    def print_current_balance(self):
        print("Your current balance is: ", self.balance)
        

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += self.balance + amount 
        print("Deposit is successful and the new balance is ", self.balance)
       
  
    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print("The withdrawal is successful and the new balance is: ", self.balance)
            
    
    def isValidPIN(pin):
        
        # implement isValidPIN here
        
        return False  # be sure to change this
    

    
    # all objects have a toString method - this indicates you are providing
    # your own version
    def __repr__(self):
        return "" # change this as needed

