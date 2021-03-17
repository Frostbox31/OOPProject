
#from datetime import datetime
import mysql.connector
import datetime 
from collections import defaultdict


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
        
#gethistoricaldataforallcoin()

call = data_manu()    
call.Query()
call.weekly_Profit()
call.monthly_Profit()
call.yearly_Profit()
call.Insert()