from SecondLayer.Utilities import _selectSQLCommand
#from SecondLayer.Profit import data_manu

def getTotalVolumeForTheDay(): # Return the Total number of volume cryptocurrency traded during a day.
    totalvolume =  _selectSQLCommand('SELECT Volume FROM coinvolume where name = "Total Volume"','')
    return (str(totalvolume).replace('(','').replace(')','').replace(',','').replace('[','').replace(']',''))
pass

def getCoinsName(): # Get The Top 10 Coins Name
    return _selectSQLCommand('SELECT DISTINCT name FROM coingeckodata','')
pass

def getCoinsShortForm(): # Get The Top 10 Coins ShortForm
    return _selectSQLCommand('SELECT Shortform FROM coinvolume LIMIT 10','')
pass

def GetProfit():
    call = data_manu()    
    call.Query()
    call.weekly_Profit()
    call.monthly_Profit()
    call.yearly_Profit()
    call.Insert()

#GetProfit()


