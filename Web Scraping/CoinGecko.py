import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
import mysql.connector
import time
from decimal import Decimal
import sys
import datetime 


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


class data_manu:
     
    
    def __init__(self):
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="Dataproject"
        )
    def Query(self): 
        cur = mydb.cursor() 
        cur.execute("select Name,Date,Close from coingeckodata WHERE year(date) = (select max(year(date)) from coingeckodata)")
        self.result1 = cur.fetchall()        
        #for name in self.result1:
            #print(name)
    
    def yearly_Profit(self):
        year_delta = datetime.timedelta(days=365)
        start_date = self.end_date - year_delta
        dates_year_list =[]
        year_list =[]
        new_list3=[]
        profit_year_list=[] 
        for item in self.result1[1:]: # skip 1st element as closing price not available yet, hence N/A
            if item[1] >= str(start_date): 
                year_list.append(item[2])
                dates_year_list.append(item[1])
            else:
                break
        for item in year_list:
            item = item[2:] #remove 's' & '$'
            item = item.replace(',', '') 
            new_list3.append(item)    # might have to change this to avoid create new list

        today_price = new_list3[0]
        for price in new_list3[1:]: 
                profit = ((int(today_price) - int(price)) /int(today_price)) *100
                profit_year_list.append(profit)


        print(dates_year_list)
        print(year_list)
        print(profit_year_list)

    def monthly_Profit(self):
        pass

    def weekly_Profit(self):
        week_delta = datetime.timedelta(weeks=1)
        day_delta = datetime.timedelta(days=1)
        self.end_date = datetime.date.today() - day_delta #yesterday date as today's closing is not available yet
        start_date = self.end_date - week_delta
        #self.start_date = start_date.strftime("%Y-%m-%d")
        #self.end_date = end_date.strftime("%Y-%m-%d") 
        dates_week_list=[]
        week_list=[]
        new_list2=[]
        profit_list=[]  
        for item in self.result1[1:]: # skip 1st element as closing price not available yet, hence N/A
            if item[1] >= str(start_date): 
                week_list.append(item[2])
                dates_week_list.append(item[1])
            else:
                break
        for item in week_list:
            item = item[2:] #remove 's' & '$'
            item = item.replace(',', '') 
            new_list2.append(item)    # might have to change this to avoid create new list

        today_price = new_list2[0]
        for price in new_list2[1:]: 
                profit = ((int(today_price) - int(price)) /int(today_price)) *100
                profit_list.append(profit)

        print(profit_list)        
        print(start_date)
        print (self.end_date)
        print (day_delta)
        #print(new_list2)
        #print(dates_week_list)
        

call = data_manu()    
call.Query()
call.weekly_Profit()
call.yearly_Profit()
