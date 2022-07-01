
class CoinCollector:
    
    
    coinDict = {'P': 1,
    'N':5,
    'D':10,
    'Q':25,
    'H': 50,
    'W': 100}
    
    def parseChange(self):
        counter = 0
        getCoins = input("""Provide a list of any of these characters: 
            PNDQHW. P=1,N=5,D=10,Q=25,H=50,W=100 Ex. pnd: """).upper()
        # print(getCoins)
        
        for j in getCoins:
            if j not in getCoins:
                print("Invaid Entry. Try again.")
                return None
            counter+=self.coinDict[j]

        return counter / 100

    
