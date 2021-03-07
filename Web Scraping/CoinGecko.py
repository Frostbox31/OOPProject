import requests
from bs4 import BeautifulSoup
from datetime import date
import mysql.connector
import time
from decimal import Decimal
import sys


class Data:
      def __init__(coin,name,date,marketcap, volume,open,close):
          coin.name = name
          coin.date = date
          coin.marketcap = marketcap
          coin.volume = volume
          coin.open = open
          coin.close = close

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="DataProject"
)

CalculateTime = Decimal(time.perf_counter())

def sublink():
    
  output = []
  enddate = date.today().strftime("%Y-%m-%d")
  startdate = "2010-01-01"
  endwith = ["compare","trending","high_volume","all","recently_added"]
    
  request = requests.get('https://coingecko.com/',headers={'User-agent': 'Super Bot Power Level Over 9000'})

  soup = BeautifulSoup(request.content, 'html.parser')

  for match in soup.find_all('a', href=lambda value:value and value.startswith("/en/coins") and not value.endswith(tuple(endwith))): # Comment Link
            if "https://www.coingecko.com" + match['href'] + "/historical_data/sgd?end_date="+ enddate + "&start_date=" + startdate not in output:
                output.insert(0,"https://www.coingecko.com" + match['href'] + "/historical_data/sgd?end_date="+ enddate + "&start_date=" + startdate)

  return output
pass

def gethistoricaldataforallcoin():

  link = sublink()
  temp = []
  temp2 = []
  temp3 = []
  dataset =  []

  for position in range(len(link)-99): #change this to get the number of coins,Currently 10 coins
    
      request = requests.get(link[99-position],headers={'User-agent': 'Super Bot Power Level Over 9000'})

      temp3.insert(0,link[99-position].split("/")[5])

      soup = BeautifulSoup(request.content, 'html.parser')

      match = soup.find('table')
      
      for match in soup.find_all(attrs={"scope": 'row'}): # Comment Link
          temp.insert(len(temp),match.text)

      for match in soup.find_all("td",class_='text-center'): # Comment Link
          temp2.insert(len(temp2),match.get_text(strip=True))
    
      inc =0;
      for x in range(len(temp)):
          dataset.insert(len(temp),Data(temp3[0],temp[x],temp2[inc],temp2[1+inc][2:],temp2[2+inc],temp2[3+inc]))   
          inc += 4
         
  mycursor = mydb.cursor()
  sql = 'DELETE FROM CoinGeckoData'
  mycursor.execute(sql,'')  
  for x in range(len(dataset)):
    sql = 'INSERT INTO CoinGeckoData (Name, Date, MarketCap, Volume, Open, Close) VALUES (%s, %s, %s, %s, %s, %s)'
    val = (str(dataset[x].name),str(dataset[x].date),str(dataset[x].marketcap),str(dataset[x].volume),str(dataset[x].open),str(dataset[x].close))
    mycursor.execute(sql, val)

    mydb.commit()
pass

def getdailyvolumeforallcoins():
  
    class Volume:
      def __init__(coin,name,volume):
          coin.name = name
          coin.volume = volume

    temp = []
    temp2 = []
    pagenumber = 22
    check = pagenumber

    while pagenumber == check:
      request = requests.get('https://www.coingecko.com/en/coins/all/show_more_coins?page=' + str(pagenumber),headers={'User-agent': 'Super Bot Power Level Over 9000'})

      soup = BeautifulSoup(request.content, 'html.parser')

      for match in soup.find_all(class_="d-none d-lg-block font-bold"):
          temp.insert(len(temp),match.get_text(strip=True))

      for match in soup.find_all(class_="td-total_volume lit text-right px-0 pl-2"):
          if match.get_text(strip=True) == "?":
              temp2.insert(len(temp),"0")
          else:
              temp2.insert(len(temp),match.get_text(strip=True)[1:])

      if len(temp) % 300 == 0:
          pagenumber += 1
          check += 1
      else:
          check -= 1
    pass
    
    mycursor = mydb.cursor()
    sql = 'DELETE FROM coinvolume'
    mycursor.execute(sql,'')  

    for x in range(len(temp)):
        sql = 'INSERT INTO coinvolume (Name,Volume) VALUES (%s, %s)'
        print(temp[x])
        print(temp2[x])
        val = (temp[x],temp2[x])
        mycursor.execute(sql, val)

pass

#getdailyvolumeforallcoins still debugging

gethistoricaldataforallcoin()
CalculateTime = Decimal(time.perf_counter()) - CalculateTime
print(str(CalculateTime) + " Seconds")