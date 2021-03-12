import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
import mysql.connector
import time
from decimal import Decimal
import sys
import datetime 

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  #password="F2814939p",
 
  database="DataProject"
)
class Data:
      def __init__(coin,name,date,marketcap, volume,open,close):
          coin.name = name
          coin.date = date
          coin.marketcap = marketcap
          coin.volume = volume
          coin.open = open
          coin.close = close

CalculateTime = Decimal(time.perf_counter())

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

  for position in range(len(link)-97): #change this to get the number of coins,Currently 10 coins
    
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
          dataset.insert(len(dataset),Data(temp3,temp[x],temp2[inc],temp2[1+inc][2:],temp2[2+inc],temp2[3+inc]))   
          inc += 4
      
      temp.clear()
      temp2.clear()
         
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
              temp2.insert(len(temp2),str(match.get_text(strip=True)[1:]).replace(',',''))
    
      count = 0
      for match in soup.find_all(attrs={"data-target": 'price.price'}):
            if match.has_attr('data-coin-id'):
                if match.get_text(strip=True) == "$0.00000000" or match.get_text(strip=True) == "?" :
                    temp3.insert(len(temp3),"0")
                else:
                    temp3.insert(len(temp3),str(match.get_text(strip=True)[1:]).replace(',',''))

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
    
    mycursor = mydb.cursor()
    sql = 'DELETE FROM coinvolume'
    mycursor.execute(sql,'')  

    totalvolume = 0

    for x in range(len(temp)):
        sql = 'INSERT INTO coinvolume (Id,Name,Volume) VALUES (%s,%s, %s)'
        val = (x+1,temp[x],(float(num[x])))
        mycursor.execute(sql, val)
        totalvolume += num[x]
    
    sql = 'INSERT INTO coinvolume (Id,Name,Volume) VALUES (%s,%s, %s)'
    val = (len(temp)+1,"Total Volume",float(totalvolume))
    mycursor.execute(sql, val)
    mydb.commit()
pass

def gettotalvolumefortheday():
    
    mycursor = mydb.cursor()
    sql = 'SELECT Volume FROM coinvolume where name = "Total Volume"'
    mycursor.execute(sql)  

    totalvolume =  mycursor.fetchall()

    return str(totalvolume[0]).replace('(','').replace(')','').replace(',','')
pass


#totalvolume = gettotalvolumefortheday() example 
#getdailyvolumeforallcoins()
gethistoricaldataforallcoin()
CalculateTime = Decimal(time.perf_counter()) - CalculateTime
print(str(CalculateTime) + " Seconds")


class data_manu:
     
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        # password="F2814939p",
        password="",
        database="Dataproject"
        )

    

    def Query(self): 
        cur = self.mydb.cursor() 
        cur.execute("select Name,Date,Close from coingeckodata WHERE year(date) = (select max(year(date)) from coingeckodata)")
        self.result1 = cur.fetchall()        
        for name in self.result1:
            print(name)

    def Insert(self):
        cur = self.mydb.cursor()
        cur2 = self.mydb.cursor()
        cur.execute('DELETE FROM weeklyprofit')
        #cur2.execute('DELETE FROM yearlyprofit')
        for x in range(len(self.dates_week_list)):
            sql = "INSERT INTO weeklyprofit (Name,Date,Price,Profit) VALUES (%s,%s,%s,%s)"
            val = (self.name_week[x],self.dates_week_list[x],self.new_list2[x],self.profit_list[x])
            cur.execute(sql, val)
        self.mydb.commit()
        #for x in range(len(self.dates_year_list)):
            #sql = "INSERT INTO yearlyprofit (Name,Date,Price,Profit) VALUES (%s,%s,%s,%s)"
            #val = (self.name_year[x],self.dates_year_list[x],self.new_list3[x],self.profit_year_list[x])
            #cur2.execute(sql, val)
        #self.mydb.commit()

    def yearly_Profit(self):
        year_delta = datetime.timedelta(days=365)
        day_delta = datetime.timedelta(days=1)
        self.end_date = datetime.date.today() - day_delta #yesterday date as today's closing is not available yet
        start_date = self.end_date - year_delta
        self.dates_year_list =[]
        year_list =[]
        self.new_list3=[]
        self.profit_year_list=[] 
        self.name_year =[]
        for item in self.result1[1:]: # skip 1st element as closing price not available yet, hence N/A
            if item[1] >= str(start_date): 
                    year_list.append(item[2])
                    self.dates_year_list.append(item[1])
                    self.name_year.append(item[0])
            else:
                break
        for item in year_list:
            item = item[2:] #remove 's' & '$'
            item = item.replace(',', '') 
            self.new_list3.append(item)    # might have to change this to avoid create new list

        today_price = self.new_list3[0]
        for price in self.new_list3: 
                profit = ((int(today_price) - int(price)) /int(today_price)) *100
                self.profit_year_list.append(profit)


        print(self.dates_year_list)
        print(year_list)
        #print(self.profit_year_list)

    def monthly_Profit(self):
        pass

    def weekly_Profit(self):
        week_delta = datetime.timedelta(weeks=1)
        day_delta = datetime.timedelta(days=1)
        self.end_date = datetime.date.today() - day_delta #yesterday date as today's closing is not available yet
        start_date = self.end_date - week_delta
        #self.start_date = start_date.strftime("%Y-%m-%d")
        #self.end_date = end_date.strftime("%Y-%m-%d") 
        self.dates_week_list=[]
        week_list=[]
        self.new_list2=[]
        self.profit_list=[]  
        self.name_week =[]
        for item in self.result1[1:]: # skip 1st element as closing price not available yet, hence N/A
            if item[1] >= str(start_date): 
                week_list.append(item[2])
                self.dates_week_list.append(item[1])
                self.name_week.append(item[0])
            else:
                break
        for item in week_list:
            item = item[2:] #remove 's' & '$'
            item = item.replace(',', '') 
            self.new_list2.append(item)    # might have to change this to avoid create new list

        today_price = self.new_list2[0]
        for price in self.new_list2: 
                profit = ((int(today_price) - int(price)) /int(today_price)) *100
                self.profit_list.append(profit)

        print(self.profit_list)        
        print(start_date)
        print (self.end_date)
        print (day_delta)
        #print(new_list2)
        #print(dates_week_list)
        

call = data_manu()    
call.Query()
call.weekly_Profit()
#call.yearly_Profit()
call.Insert()