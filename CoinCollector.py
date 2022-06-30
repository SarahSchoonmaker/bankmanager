
from asyncio.windows_events import NULL
from itertools import count

from prometheus_client import Counter


class CoinCollector:
    
    
    coinDict = {'P': 1,
    'N':5,
    'D':10,
    'Q':25,
    'H': 50,
    'W': 100}
    
    def parseChange(self):
        counter = 0
        getCoins = input("Provide a list of coins, Ex. PNDQHW").upper()
        print(getCoins)
        
        for j in getCoins:
            if j not in getCoins:
                print("Invaid Entry. Try again.")
                return None
            counter+=self.coinDict[j]

        return counter / 100

    
