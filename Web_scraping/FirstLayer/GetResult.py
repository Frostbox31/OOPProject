from SecondLayer.Utilities import selectsqlcommand

def gettotalvolumefortheday():
    totalvolume =  selectsqlcommand('SELECT Volume FROM coinvolume where name = "Total Volume"','')
    return (str(totalvolume).replace('(','').replace(')','').replace(',','').replace('[','').replace(']',''))
pass

def getcoinsname():
    return selectsqlcommand('SELECT DISTINCT name FROM coingeckodata','')
pass

