from SecondLayer.Google import *
from SecondLayer.CoinGecko import *
from GetResult import getcoinsname
import time
from decimal import Decimal
from time import sleep


CalculateTime = Decimal(time.perf_counter())

#getdailyvolumeforallcoins()
#gethistoricaldataforallcoin()

def _GenerateGoogleNews():

    coinsname = getcoinsname()

    for x in range (len(coinsname)):
        sleep(2)
        print(str(coinsname[x]).replace('(','').replace(')','').replace(',','').replace("'",''))
        #getGoogleNew(str(coinsname[x]).replace('(','').replace(')','').replace(',',''))

_GenerateGoogleNews()
CalculateTime = Decimal(time.perf_counter()) - CalculateTime
print(str(CalculateTime) + " Seconds")