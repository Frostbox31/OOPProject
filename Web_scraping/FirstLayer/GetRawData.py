from SecondLayer.Google import getGoogleNew
from SecondLayer.Yahoo import getyahoofinancecomment
from SecondLayer.CoinGecko import *
from GetResult import getcoinsname, getcoinsshortform
import time
from decimal import Decimal
from time import sleep
import numpy as np

CalculateTime = Decimal(time.perf_counter())

#getdailyvolumeforallcoins()
#gethistoricaldataforallcoin()

def _GenerateGoogleNews():
    coinsname = getcoinsname()
    coinsname.insert(0,"cryptocurrency")

    for x in range (len(coinsname)):
        delays = [6, 7, 10, 12]
        delay = np.random.choice(delays)
        sleep(delay) 
        getGoogleNew(str(coinsname[x]).replace('(','').replace(')','').replace(',','').replace("'",'').replace("-"," "))

def _GenerateYahooFinanceTopComment():
    coinsname = getcoinsname()
    coinshortform = getcoinsshortform()

    for x in range (len(coinsname)):   
        getyahoofinancecomment(str(coinsname[x]).replace('(','').replace(')','').replace(',','').replace("'",'').replace("-"," "),str(coinshortform[x]).replace('(','').replace(')','').replace(',','').replace("'",'').replace("DOT",'DOT1'))

#_GenerateGoogleNews()
_GenerateYahooFinanceTopComment()
CalculateTime = Decimal(time.perf_counter()) - CalculateTime
print(str(CalculateTime) + " Seconds")

