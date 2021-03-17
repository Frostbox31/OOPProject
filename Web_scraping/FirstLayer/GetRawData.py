from SecondLayer.Google import getGoogleNews
from SecondLayer.Yahoo import getYahooFinanceComment
from SecondLayer.CoinGecko import _getHistoricalDataForAllCoin,_getDailyVolumeForAllCoins
from GetResult import getCoinsName, getCoinsShortForm
import time
from decimal import Decimal
from time import sleep
import numpy as np

CalculateTime = Decimal(time.perf_counter()) #Start the Timer

def _generateGoogleNews():
    coinsname = getCoinsName()
    coinsname.insert(0,"cryptocurrency")

    for x in range (len(coinsname)):
        delays = [6, 7, 10, 12]
        delay = np.random.choice(delays)
        sleep(delay) 
        getGoogleNews(str(coinsname[x]).replace('(','').replace(')','').replace(',','').replace("'",'').replace("-"," "))

def _generateYahooFinanceTopComment():
    coinsname = getCoinsName()
    coinshortform = getCoinsShortForm()

    for x in range (len(coinsname)):   
        getYahooFinanceComment(str(coinsname[x]).replace('(','').replace(')','').replace(',','').replace("'",'').replace("-"," "),str(coinshortform[x]).replace('(','').replace(')','').replace(',','').replace("'",'').replace("DOT",'DOT1'))

#_getDailyVolumeForAllCoins() #Get Cryptocurrency Trading Volume Each Day
_getHistoricalDataForAllCoin() #Get Cryptocurrency MarketCap,Volume, Opening Price and Closing since it listed
#_generateGoogleNews() #Get Cryptocurrency and Top 10 Coins Google News
#_generateYahooFinanceTopComment() # Get Cryptocurrency people comment from Yahoo Finance

CalculateTime = Decimal(time.perf_counter()) - CalculateTime # Calculate the difference between the time
print(str(CalculateTime) + " Seconds") #Display the time taken for the program to run

