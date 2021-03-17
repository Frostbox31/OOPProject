from SecondLayer.Utilities import commitsqlcommand
import requests
from bs4 import BeautifulSoup
from datetime import date



class Data:
      def __init__(coin,name,date,marketcap, volume,open,close):
          coin.name = name
          coin.date = date
          coin.marketcap = marketcap
          coin.volume = volume
          coin.open = open
          coin.close = close

def sublink():
    
  output = []
  enddate = date.today().strftime("%Y-%m-%d")
  startdate = "2010-01-01"
  endwith = ["compare","trending","high_volume","all","recently_added"]
    
  request = requests.get('https://coingecko.com/',headers={'User-agent': 'Super Bot Power Level Over 9000'})

  soup = BeautifulSoup(request.content, 'html.parser')
    
  for match in soup.find_all('a', href=lambda value:value and value.startswith("/en/coins") and not value.endswith(tuple(endwith))): # Comment Link
            if "https://www.coingecko.com" + match['href'] + "/historical_data/usd?end_date="+ enddate + "&start_date=" + startdate not in output:
                output.insert(0,"https://www.coingecko.com" + match['href'] + "/historical_data/usd?end_date="+ enddate + "&start_date=" + startdate)

  return output
pass

def gethistoricaldataforallcoin():

  link = sublink()
  
  dataset =  []
  temp = []
  temp2 = []

  for position in range(len(link)-90): #change this to get the number of coins,Currently 10 coins
    
      request = requests.get(link[99-position],headers={'User-agent': 'Super Bot Power Level Over 9000'})

      temp3 = link[99-position].split("/")[5]

      soup = BeautifulSoup(request.content, 'html.parser')

      match = soup.find('table')
      
      for match in soup.find_all(attrs={"scope": 'row'}): # Comment Link
          temp.insert(len(temp),match.text)

      for match in soup.find_all("td",class_='text-center'): # Comment Link
          temp2.insert(len(temp2),match.get_text(strip=True))
    
      inc =0;
      for x in range(len(temp)):
          dataset.insert(len(dataset),Data(temp3,temp[x],temp2[inc],temp2[1+inc],temp2[2+inc],temp2[3+inc]))   
          inc += 4
      temp.clear()
      temp2.clear()
  commitsqlcommand('DELETE FROM CoinGeckoData','')
  for x in range(len(dataset)):
    commitsqlcommand('INSERT INTO CoinGeckoData (Name, Date, MarketCap, Volume, Open, Close) VALUES (%s, %s, %s, %s, %s, %s)',(str(dataset[x].name),str(dataset[x].date),str(dataset[x].marketcap),str(dataset[x].volume).replace('$',''),str(dataset[x].open),str(dataset[x].close)))
pass


def getdailyvolumeforallcoins():
  
    class Volume:
      def __init__(coin,name,volume):
          coin.name = name
          coin.volume = volume

    temp = []
    num = []
    pagenumber = 1
    check = pagenumber

    while pagenumber == check:
      temp2 = []
      temp3 = []
      request = requests.get('https://www.coingecko.com/en/coins/all/show_more_coins?page=' + str(pagenumber),headers={'User-agent': 'Super Bot Power Level Over 9000'})

      soup = BeautifulSoup(request.content, 'html.parser')

      for match in soup.find_all(class_="d-none d-lg-block font-bold"):
          temp.insert(len(temp),match.get_text(strip=True))

      for match in soup.find_all(class_="td-total_volume lit text-right px-0 pl-2"):
          if match.get_text(strip=True) == "$0.00000000" or match.get_text(strip=True) == "?" :
              temp2.insert(len(temp2),"0")
          else:
              temp2.insert(len(temp2),str(match.get_text(strip=True)).replace(',','').replace('$',''))
    
      count = 0
      for match in soup.find_all(attrs={"data-target": 'price.price'}):
            if match.has_attr('data-coin-id'):
                if match.get_text(strip=True) == "$0.00000000" or match.get_text(strip=True) == "?" :
                    temp3.insert(len(temp3),"0")
                else:
                    temp3.insert(len(temp3),str(match.get_text(strip=True)).replace(',','').replace('$',''))

      for x in range (len(temp2)):
          if(temp2[x] != "0" and temp3[x] != "0"):
             num.insert(len(num),float(temp2[x])//float(temp3[x]))
          else:
             num.insert(len(num),0)

      if len(temp) % 300 == 0:
          pagenumber += 1
          check += 1
      else:
          check -= 1
    pass
    
    commitsqlcommand('DELETE FROM coinvolume','')

    totalvolume = 0

    for x in range(len(temp)):
        commitsqlcommand('INSERT INTO coinvolume (Id,Name,Volume) VALUES (%s,%s, %s)',(x+1,temp[x],(float(num[x]))))
        totalvolume += num[x]
    
    commitsqlcommand('INSERT INTO coinvolume (Id,Name,Volume) VALUES (%s,%s, %s)',(len(temp)+1,"Total Volume",float(totalvolume)))
pass



