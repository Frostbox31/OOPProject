from SecondLayer.Google import _getGoogleNews
from SecondLayer.Yahoo import _getYahooFinanceComment
from SecondLayer.Reddit import _getRedditCoinOccur
from SecondLayer.CoinGecko import _getHistoricalDataForAllCoin,_getDailyVolumeForAllCoins
from GetResult import getCoinsName, getCoinsShortForm
import time
from decimal import Decimal
from time import sleep
import numpy as np

CalculateTime = Decimal(time.perf_counter()) #Start the Timer

def _generateGoogleYahooReddit(param,param2):
    coinsname = getCoinsName()

    if 'Reddit' == param:
        _getRedditCoinOccur(coinsname,getCoinsShortForm(),param2)
    
    elif 'Yahoo' == param:
        coinshortform = getCoinsShortForm()
        for x in range (len(coinsname)):   
            _getYahooFinanceComment(coinsname[x],str(coinshortform[x]).replace("DOT",'DOT1'),param2)

    elif 'Google' == param:
        coinsname.insert(0,"cryptocurrency")
        for x in range (len(coinsname)):
            delays = [6, 7, 10, 12]
            delay = np.random.choice(delays)
            sleep(delay) 
            _getGoogleNews(coinsname[x])


#_getDailyVolumeForAllCoins()           # Get Cryptocurrency Trading Volume Each Day
_getHistoricalDataForAllCoin(1)         # Get Cryptocurrency MarketCap,Volume, Opening Price and Closing since it listed
#_generateGoogleYahooReddit('Yahoo',150)    # Get Cryptocurrency people comment from Yahoo Finance in multiple of 30
#_generateGoogleYahooReddit('Google','')   # Get Cryptocurrency and Top 10 Coins Google News
#_generateGoogleYahooReddit('Reddit',1)    # Get Cryptocurrency Coins Ocurrence in Reddit  EG 1 = 6 or 7 posts
CalculateTime = Decimal(time.perf_counter()) - CalculateTime # Calculate the difference between the time
print(str(CalculateTime) + " Seconds") #Display the time taken for the program to run

