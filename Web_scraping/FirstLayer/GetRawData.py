
from SecondLayer.Google import *
from SecondLayer.Reddit import _getRedditCoinOccur
from SecondLayer.CoinGecko import _getHistoricalDataForAllCoin,_getDailyVolumeForAllCoins
from SecondLayer.Yahoo import _getYahooFinanceComment
from GetResult import getCoinsName, getCoinsShortForm
import time
from decimal import Decimal
from time import sleep
import numpy as np


CalculateTime = Decimal(time.perf_counter()) #Start the Timer

def _generateGoogleYahooReddit(param,param2):

 if param == "Reddit" or param == "Yahoo" or param == "Google":

    if isinstance(param2,int) == True or param == "Google":

                coinsname = []
                coinsname = getCoinsName()

                if 'Reddit' == param and param2 > 0:
                    _getRedditCoinOccur(coinsname,getCoinsShortForm(),param2)
                
                elif 'Yahoo' == param and param2 % 30 == 0 and param2 > 0:
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

                elif 'Yahoo' == param and param2 % 30 != 0:
                    print("Please input the number in multiple of 30 for yahoo function")
                
                elif param2 <= 0:
                    print("Please input the parameter 2 starting from 1")
                
    else:
        print("Please input interger for parameter 2")
 else:
    print("Please Specific the function")

#_getDailyVolumeForAllCoins()           # Get Cryptocurrency Trading Volume Each Day
#_getHistoricalDataForAllCoin(1)         # Get Cryptocurrency MarketCap,Volume, Opening Price and Closing since it listed
#_generateGoogleYahooReddit('Yahoo',120)    # Get Cryptocurrency people comment from Yahoo Finance in multiple of 30
#_generateGoogleYahooReddit('Google','')   # Get Cryptocurrency and Top 10 Coins Google News according to coingecko table
#_generateGoogleYahooReddit('Reddit',1)    # Get Cryptocurrency Coins Ocurrence in Reddit  EG 1 = 6 or 7 posts
CalculateTime = Decimal(time.perf_counter()) - CalculateTime # Calculate the difference between the time
print(str(CalculateTime) + " Seconds") #Display the time taken for the program to run

