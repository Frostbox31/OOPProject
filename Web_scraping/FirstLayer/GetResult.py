from SecondLayer.Utilities import selectsqlcommand
from SecondLayer.Profit import data_manu
def gettotalvolumefortheday():
    totalvolume =  selectsqlcommand('SELECT Volume FROM coinvolume where name = "Total Volume"','')
    return (str(totalvolume).replace('(','').replace(')','').replace(',','').replace('[','').replace(']',''))
pass

def getcoinsname():
    return selectsqlcommand('SELECT DISTINCT name FROM coingeckodata','')
pass

def GetProfit():
    call = data_manu()    
    call.Query()
    call.weekly_Profit()
    call.monthly_Profit()
    call.yearly_Profit()
    call.Insert()

GetProfit()

 



