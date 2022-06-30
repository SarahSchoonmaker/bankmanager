
class CoinCollector:
    
    counter = 0
    coinDict = {'P': 1,
    'N':5,
    'D':10,
    'Q':25,
    'H': 50,
    'W': 100}
    
    def parseChange(self):
        getCoins = str(input("Provide a list of coins, Ex. PNDQHW").split(",")).upper()
        print(getCoins)
        
        for j in getCoins:

            for i in self.coinDict:
                if getCoins[j] in self.coinDict[i]:
                    self.counter +=1
            else:
                print("Invaid Entry. Try again.")
        # Call depsoit method on account and deposit coins into the account. Display the updated balance.


        
        
