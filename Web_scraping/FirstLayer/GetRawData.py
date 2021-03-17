from SecondLayer.Google import getGoogleNew
from SecondLayer.CoinGecko import *
from GetResult import getcoinsname
import time
from decimal import Decimal
from time import sleep
import numpy as np

CalculateTime = Decimal(time.perf_counter())

#getdailyvolumeforallcoins()
gethistoricaldataforallcoin()

def _GenerateGoogleNews():
    coinsname = getcoinsname()
    coinsname.insert(0,"cryptocurrency")

    for x in range (len(coinsname)):
        delays = [6, 7, 10, 12]
        delay = np.random.choice(delays)
        sleep(delay) 
        getGoogleNew(str(coinsname[x]).replace('(','').replace(')','').replace(',','').replace("'",'').replace("-"," "))

#_GenerateGoogleNews()
CalculateTime = Decimal(time.perf_counter()) - CalculateTime
print(str(CalculateTime) + " Seconds")