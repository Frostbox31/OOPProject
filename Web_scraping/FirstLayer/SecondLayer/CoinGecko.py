import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
import mysql.connector
import datetime 
from collections import defaultdict

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="F2814939p",
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
         
  mycursor = mydb.cursor()
  sql = 'DELETE FROM CoinGeckoData'
  mycursor.execute(sql,'')  
  for x in range(len(dataset)):
    sql = 'INSERT INTO CoinGeckoData (Name, Date, MarketCap, Volume, Open, Close) VALUES (%s, %s, %s, %s, %s, %s)'
    val = (str(dataset[x].name),str(dataset[x].date),str(dataset[x].marketcap),str(dataset[x].volume).replace('$',''),str(dataset[x].open),str(dataset[x].close))
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


class data_manu:
     
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
         password="F2814939p",
        #password="",
        database="Dataproject"
        )


    def Query(self): 
        cur = self.mydb.cursor() 
        #cur.execute("select Name,Date,Close from coingeckodata WHERE year(date) = (select max(year(date)) from coingeckodata)")
        #self.result1 = cur.fetchall()        
        #for name in self.result1:
            #print(name)
        

    def Insert(self):
        cur = self.mydb.cursor()
        cur.execute('DELETE FROM weeklyprofit')
        cur.execute('DELETE FROM monthlyprofit')
        cur.execute('DELETE FROM yearlyprofit')
        for x in range(len(self.dates_week_list)):
            sql = "INSERT INTO weeklyprofit (Name,Date,Price,Profit) VALUES (%s,%s,%s,%s)"
            val = (self.name_week[x],self.dates_week_list[x],self.week_price[x],self.weekly_profit_list[x])
            cur.execute(sql, val)
        self.mydb.commit()
        for x in range(len(self.dates_month_list)):
            sql = "INSERT INTO monthlyprofit (Name,Date,Price,Profit) VALUES (%s,%s,%s,%s)"
            val = (self.name_month[x],self.dates_month_list[x],self.month_price[x],self.monthly_profit_list[x])
            cur.execute(sql, val)
        self.mydb.commit()
        for x in range(len(self.dates_year_list)):
            sql = "INSERT INTO yearlyprofit (Name,Date,Price,Profit) VALUES (%s,%s,%s,%s)"
            val = (self.name_year[x],self.dates_year_list[x],self.year_price[x],self.yearly_profit_list[x])
            cur.execute(sql, val)
        self.mydb.commit()
          

    def yearly_Profit(self):
        year_delta = datetime.timedelta(days=365)
        day_delta = datetime.timedelta(days=1)
        year_end_date = datetime.date.today() - day_delta #yesterday date as today's closing is not available yet
        year_start_date = year_end_date - year_delta
        cur = self.mydb.cursor()
        cur.execute("SELECT Name,Date,Close from coingeckodata WHERE Date BETWEEN %s AND %s", [year_start_date,year_end_date]) 
        self.year_result = cur.fetchall()        
        #for name in self.year_result:
            #print(name)
        year_arr = list(item for item in self.year_result)
        #print(month_arr)
        year_dict = defaultdict(list)
        self.year_price=[]
        self.dates_year_list=[]
        self.name_year =[]
        self.yearly_profit_list=[]
        for k,*v in year_arr:
            year_dict[k].append(v)
        #print(dict(month_dict))
        for key,value in year_dict.items():
            #print(key,week_dict[key])
            #today_price_list.append(value[0][1])
            for item in year_dict[key]:
                item[1] = item[1][1:] #remove '$'
                item[1] = item[1].replace(',', '')
                #print(value[0][1],key)
                today_price = value[0][1]
                #print(today_price)
                profit = ((float(today_price) - float(item[1])) /float(today_price)) *100
                #print(profit)
                self.yearly_profit_list.append(profit)
                #print(key, item[0], item[1])
                self.year_price.append(item[1])
                self.dates_year_list.append(item[0])
                self.name_year.append(key)

        #print(self.year_price)  
        #print(self.yearly_profit_list)      
        #print(self.dates_year_list)
        #print(self.name_year)



    def monthly_Profit(self): #past 30 days
        month_delta = datetime.timedelta(weeks=4)
        day_delta = datetime.timedelta(days=1)
        month_end_date = datetime.date.today() - day_delta #yesterday date as today's closing is not available yet
        month_start_date = month_end_date - month_delta 
        cur = self.mydb.cursor()
        cur.execute("SELECT Name,Date,Close from coingeckodata WHERE Date BETWEEN %s AND %s", [month_start_date,month_end_date]) 
        self.month_result = cur.fetchall()        
        #for name in self.month_result:
            #print(name)

        month_arr = list(item for item in self.month_result)
        #print(month_arr)
        month_dict = defaultdict(list)
        self.month_price=[]
        self.dates_month_list=[]
        self.name_month =[]
        self.monthly_profit_list=[]
        for k,*v in month_arr:
            month_dict[k].append(v)
        #print(dict(month_dict))
        for key,value in month_dict.items():
            #print(key,week_dict[key])
            #today_price_list.append(value[0][1])
            for item in month_dict[key]:
                item[1] = item[1][1:] #remove '$'
                item[1] = item[1].replace(',', '')
                #print(value[0][1],key)
                today_price = value[0][1]
                #print(today_price)
                profit = ((float(today_price) - float(item[1])) /float(today_price)) *100
                #print(profit)
                self.monthly_profit_list.append(profit)
                #print(key, item[0], item[1])
                self.month_price.append(item[1])
                self.dates_month_list.append(item[0])
                self.name_month.append(key)

        #print(self.month_price)  
        #print(self.monthly_profit_list)      
        #print(self.dates_month_list)
        #print(self.name_month)

    

    def weekly_Profit(self):
        week_delta = datetime.timedelta(weeks=1)
        day_delta = datetime.timedelta(days=1)
        week_end_date = datetime.date.today() - day_delta #yesterday date as today's closing is not available yet
        week_start_date = week_end_date - week_delta
        #self.week_start_date = week_start_date.strftime("%Y-%m-%d")
        #self.week_end_date = week_end_date.strftime("%Y-%m-%d")  
        cur = self.mydb.cursor()
        cur.execute("SELECT Name,Date,Close from coingeckodata WHERE Date BETWEEN %s AND %s", [week_start_date,week_end_date]) 
        self.week_result = cur.fetchall()        
        #for name in self.week_result:
            #print(name)
        week_arr = list(item for item in self.week_result)
        #print(week_arr)
        week_dict = defaultdict(list)
        self.week_price=[]
        self.dates_week_list=[]
        self.name_week =[]
        self.weekly_profit_list=[]
        for k,*v in week_arr:
            week_dict[k].append(v)
        #print(dict(week_dict))
        for key,value in week_dict.items():
            #print(key,week_dict[key])
            #today_price_list.append(value[0][1])
            for item in week_dict[key]:
                item[1] = item[1][1:] #remove '$'
                item[1] = item[1].replace(',', '')
                #print(value[0][1],key)
                today_price = value[0][1]
                #print(today_price)
                profit = ((float(today_price) - float(item[1])) /float(today_price)) *100
                #print(profit)
                self.weekly_profit_list.append(profit)
                #print(key, item[0], item[1])
                self.week_price.append(item[1])
                self.dates_week_list.append(item[0])
                self.name_week.append(key)
    
        #print(self.week_price)  
        #print(self.weekly_profit_list)      
        #print(self.dates_week_list)
        #print(self.name_week)
        

#call = data_manu()    
#call.Query()
#call.weekly_Profit()
#call.monthly_Profit()
#call.yearly_Profit()
#call.Insert()