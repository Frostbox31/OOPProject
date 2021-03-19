from SecondLayer.Utilities import _selectSQLCommand
from SecondLayer.Profit import data_manu
import time
from decimal import Decimal

def getTotalVolumeForTheDay(): # Return the Total number of volume cryptocurrency traded during a day.
    totalvolume =  _selectSQLCommand('SELECT Volume FROM coinvolume where name = "Total Volume"','')
    return (str(totalvolume).replace('(','').replace(')','').replace(',','').replace('[','').replace(']',''))
pass

def getCoinsName(): # Get The Top 10 Coins Name
    coinsname = _selectSQLCommand('SELECT DISTINCT name FROM coingeckodata','')
    for x in range (len(coinsname)):
        coinsname[x] = str(coinsname[x]).replace('(','').replace(')','').replace(',','').replace("'",'').replace("-"," ");        
    return coinsname
pass

def getCoinsShortForm(): # Get The Top 10 Coins ShortForm
    shortform = _selectSQLCommand('SELECT Shortform FROM coinvolume LIMIT 10','')
    for x in range (len(shortform)):
        shortform[x] = str(shortform[x]).replace('(','').replace(')','').replace(',','').replace("'",'')       
    return shortform
pass

def GetProfit():
    call = data_manu()    
    call.Query()
    call.weekly_Profit()
    call.monthly_Profit()
    call.yearly_Profit()
    call.Insert()

CalculateTime = Decimal(time.perf_counter()) #Start the Timer

GetProfit()

#getCoinsShortForm()

CalculateTime = Decimal(time.perf_counter()) - CalculateTime # Calculate the difference between the time
print(str(CalculateTime) + " Seconds") #Display the time taken for the program to run


