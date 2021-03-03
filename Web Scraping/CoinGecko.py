import requests
from bs4 import BeautifulSoup
import sys
import re
from datetime import date
import mysql.connector


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
  password="F2814939p",
  database="DataProject"
)


link = []
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

#def gethistoricaldataforallcoin():test

link = sublink()
temp = []
temp2 = []
temp3 = []
dataset =  []

for position in range(len(link)-90):

    request = requests.get(link[position],headers={'User-agent': 'Super Bot Power Level Over 9000'})

    temp3.insert(0,link[position].split("/")[5])

    soup = BeautifulSoup(request.content, 'html.parser')

    match = soup.find('table')
    
    for match in soup.find_all(attrs={"scope": 'row'}): # Comment Link
        temp.insert(0,match.text)

    for match in soup.find_all("td",class_='text-center'): # Comment Link
        abc = match.get_text(strip=True)
        temp2.insert(0,abc)

    inc =0;
    for x in range(len(temp)):
        dataset.insert(0,Data(temp3[0],temp[x],temp2[x+3+inc],temp2[x+2+inc],temp2[x+1+inc],temp2[x+inc]))   
        inc += 3
  
#for x in range(len(dataset)):
#      print(dataset[x].name)
#      print(dataset[x].date)
#      print(dataset[x].marketcap)
#      print(dataset[x].volume)
#      print(dataset[x].open)
#      print(dataset[x].close)

mycursor = mydb.cursor()
for x in range(len(dataset)):
  sql = 'INSERT INTO CoinGeckoData (Name, Date, MarketCap, Volume, Open, Close) VALUES (%s, %s, %s, %s, %s, %s)'
  val = (str(dataset[x].name),str(dataset[x].date),str(dataset[x].marketcap),str(dataset[x].volume),str(dataset[x].open),str(dataset[x].close))
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")

