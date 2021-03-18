from SecondLayer.Utilities import _commitSQLCommand, _getRandomHeader, _getRandomProxy
import requests
from bs4 import BeautifulSoup
from datetime import date
import random

class Data:
      def __init__(coin,name,date,marketcap, volume,open,close):
          coin.name = name
          coin.date = date
          coin.marketcap = marketcap
          coin.volume = volume
          coin.open = open
          coin.close = close

def __sublink(): #Get Cryptocurrency Link
    
  output = []
  enddate = date.today().strftime("%Y-%m-%d")
  startdate = "2010-01-01"
  endwith = ["compare","trending","high_volume","all","recently_added"]
  proxy = _getRandomProxy()
  
  request = requests.get('https://coingecko.com/',proxies=random.choice(proxy),headers=_getRandomHeader())

  soup = BeautifulSoup(request.content, 'html.parser')
    
  for match in soup.find_all('a', href=lambda value:value and value.startswith("/en/coins") and not value.endswith(tuple(endwith))): # Comment Link
            if "https://www.coingecko.com" + match['href'] + "/historical_data/usd?end_date="+ enddate + "&start_date=" + startdate not in output:
                output.insert(0,"https://www.coingecko.com" + match['href'] + "/historical_data/usd?end_date="+ enddate + "&start_date=" + startdate)
  return output
pass

def _getHistoricalDataForAllCoin(): # Get Cryptocurrency MarketCap,Volume, Opening Price and Closing since it listed

  link = __sublink()
  dataset =  []
  date = []
  coindata = []

  proxy = _getRandomProxy()

  for position in range(len(link)-90): #change this to get the number of coins, For EG: 99 = 1 Coin, 98 = 2 Coin
    
      request = requests.get(link[99-position],proxies=random.choice(proxy),headers=_getRandomHeader())

      coinname = link[99-position].split("/")[5]

      soup = BeautifulSoup(request.content, 'html.parser')

      match = soup.find('table')
      
      for match in soup.find_all(attrs={"scope": 'row'}):
          date.insert(len(date),match.text)

      for match in soup.find_all("td",class_='text-center'):
          coindata.insert(len(coindata),match.get_text(strip=True))
    
      inc =0;
      for x in range(len(date)):
          dataset.insert(len(dataset),Data(coinname,date[x],coindata[inc],coindata[1+inc],coindata[2+inc],coindata[3+inc]))   
          inc += 4
    
  _commitSQLCommand('DELETE FROM CoinGeckoData','')
  for x in range(len(dataset)):
    _commitSQLCommand('INSERT INTO CoinGeckoData VALUES (%s, %s, %s, %s, %s, %s)',(dataset[x].name,dataset[x].date,dataset[x].marketcap,str(dataset[x].volume).replace('$',''),dataset[x].open,dataset[x].close))
pass

def _getDailyVolumeForAllCoins(): # Get Cryptocurrency Trading Volume Each Day
  
    coinname = []
    coinshortform = []
    volume = []
    pagenumber = 1
    check = pagenumber

    proxy = _getRandomProxy()

    while pagenumber == check:
      coinvolumeprice = []
      coinprice = []
      request = requests.get('https://www.coingecko.com/en/coins/all/show_more_coins?page=' + str(pagenumber),proxies=random.choice(proxy),headers=_getRandomHeader())

      soup = BeautifulSoup(request.content, 'html.parser')

      for match in soup.find_all(class_="d-none d-lg-block font-bold"):
          coinname.insert(len(coinname),match.get_text(strip=True))
      
      for match in soup.find_all(class_="d-none d-lg-inline font-normal text-3xs mt-1"):
          coinshortform.insert(len(coinshortform),str(match.get_text(strip=True)).encode('cp1252', errors='ignore'))

      for match in soup.find_all(class_="td-total_volume lit text-right px-0 pl-2"):
          if match.get_text(strip=True) == "$0.00000000" or match.get_text(strip=True) == "?" :
              coinvolumeprice.insert(len(coinvolumeprice),"0")
          else:
              coinvolumeprice.insert(len(coinvolumeprice),str(match.get_text(strip=True)).replace(',','').replace('$',''))
    
      for match in soup.find_all(attrs={"data-target": 'price.price'}):
            if match.has_attr('data-coin-id'):
                if match.get_text(strip=True) == "$0.00000000" or match.get_text(strip=True) == "?" :
                    coinprice.insert(len(coinprice),"0")
                else:
                    coinprice.insert(len(coinprice),str(match.get_text(strip=True)).replace(',','').replace('$',''))
          
      #Divide the total Cryptocurrency with its Price(According to the each Crypto)
      for x in range (len(coinvolumeprice)):
          if(coinvolumeprice[x] != "0" and coinprice[x] != "0"):
             volume.insert(len(volume),float(coinvolumeprice[x])//float(coinprice[x]))
          else:
             volume.insert(len(volume),0)

      if len(coinname) % 300 == 0:
          pagenumber += 1
          check += 1
      else:
          check -= 1
    pass
    
    _commitSQLCommand('DELETE FROM coinvolume','')
    totalvolume = 0

    for x in range(len(coinname)):
        _commitSQLCommand('INSERT INTO coinvolume VALUES (%s,%s, %s, %s)',(x+1,coinname[x],volume[x],coinshortform[x]))
        totalvolume += volume[x]
    
    _commitSQLCommand('INSERT INTO coinvolume VALUES (%s,%s, %s,%s)',(len(coinname)+1,"Total Volume",totalvolume,'C'))
pass



