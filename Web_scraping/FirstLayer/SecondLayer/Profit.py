
#from datetime import datetime
import mysql.connector
import datetime 
from collections import defaultdict
from dateutil.relativedelta import relativedelta



class data_manu:
     
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        #password="F2814939p",
        password="",
        database="Dataproject"
        )


    def Insert(self):
        cur = self.mydb.cursor()
        cur.execute('DELETE FROM weeklyprofit')
        cur.execute('DELETE FROM monthlyprofit')
        cur.execute('DELETE FROM yearlyprofit')
        for x in range(len(self.dates_weekly_list)):
            sql = "INSERT INTO weeklyprofit (Name,Date,Price,Profit) VALUES (%s,%s,%s,%s)"
            val = (self.name_weekly[x],self.dates_weekly_list[x],self.weekly_price[x],self.weekly_profit_list[x])
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
       
    
    def InsertBarProfit(self):
        cur = self.mydb.cursor()
        cur.execute('DELETE FROM barweeklyprofit')
        cur.execute('DELETE FROM barmonthlyprofit')
        cur.execute('DELETE FROM baryearlyprofit')
        for x in range(len(self.week_profit_avg)):
            sql = "INSERT INTO barweeklyprofit (Name,StartD,EndD,Profit) VALUES (%s,%s,%s,%s)"
            val = (self.week_coins[x],self.week_start_date,self.week_end_date,self.week_profit_avg[x])
            cur.execute(sql, val)
        self.mydb.commit()
        for x in range(len(self.month_profit_avg)):
            sql = "INSERT INTO barmonthlyprofit (Name,StartD,EndD,Profit) VALUES (%s,%s,%s,%s)"
            val = (self.month_coins[x],self.month_start_date,self.month_end_date,self.month_profit_avg[x])
            cur.execute(sql, val)
        self.mydb.commit()
        for x in range(len(self.year_profit_avg)):
            sql = "INSERT INTO baryearlyprofit (Name,StartD,EndD,Profit) VALUES (%s,%s,%s,%s)"
            val = (self.year_coins[x],self.year_start_date,self.year_end_date,self.year_profit_avg[x])
            cur.execute(sql, val)
        self.mydb.commit()

        # print(self.year_profit_avg)
        # print(self.year_coins)

    def yearly_Profit(self):
        #year_delta = datetime.timedelta(days=365)
        year_delta = relativedelta(years=1)    #now only compare 1 years
        day_delta = datetime.timedelta(days=2)
        year_end_date = datetime.date.today() - day_delta #yesterday date as today's closing is not available yet
        year_start_date = year_end_date - year_delta
        cur = self.mydb.cursor()
        cur.execute("SELECT Name,Date,Close from coingeckodata WHERE Date BETWEEN %s AND %s", [year_start_date,year_end_date]) 
        self.year_result = cur.fetchall()   
        self.year_list = self.cal_profit_dict(self.year_result)
        self.yearly_profit_list,self.year_price,self.dates_year_list,self.name_year = self.year_list     
        #for name in self.year_result:
            #print(name)
        #print(self.year_price)  
        #print(self.yearly_profit_list)      
        #print(self.dates_year_list)
        #print(self.name_year)
        #print(self.year_list)

    def avg_year_profit(self):
        year_delta = relativedelta(years=1)    #now only compare 1 years
        day_delta = datetime.timedelta(days=2)
        self.year_end_date = datetime.date.today() - day_delta #yesterday date as today's closing is not available yet
        self.year_start_date = self.year_end_date - year_delta
        # print(year_end_date.year)
        # print(year_start_date.year)
        cur = self.mydb.cursor()
        cur.execute("SELECT Name,Date,Profit from yearlyprofit WHERE Date BETWEEN %s AND %s", [self.year_start_date,self.year_end_date]) 
        self.year_profit = cur.fetchall()
        self.year__avgplist = self.avg_dict(self.year_profit)
        # for name in self.year_result:
        #       print(name)
        self.year_profit_avg,self.year_coins = self.year__avgplist
        
        # print(self.year_profit_avg)
        # print(self.year_coins)


    def avg_dict(self,arr):
        avg_arr = list(item for item in arr)
        #print(avg_arr)
        avg_dict = defaultdict(list)
        sum =0
        coins_profit_list = []
        total_profit_list =[]
        for k,*v in avg_arr:
            avg_dict[k].append(v)
        #print(dict(avg_dict))
        self.keys_list =[key for key in avg_dict.keys()] # getting types of keys/coins
        #print(self.keys_list)   # insert into new avg_year_profit table
        # total =[item for item in avg_dict.values()]
        # print(total)
        # no_of_coins = (len(avg_dict.keys()))
        for key,value in avg_dict.items(): # iterating each key
            #print(key,avg_dict[key])
            num_days =(len(avg_dict[key])) # finding number of days each coin has
            #print(num_days)
            for item in avg_dict[key]:
                #print(item[1])
                coins_profit_list.append(item[1]) # append each profit to new list for summation
            count =0 
            while count<num_days:                #summating profit for each key/coin
                for profit in coins_profit_list:
                        sum = profit+ sum
                        count=count+1
            total_profit_list.append(sum)
        self.avg_profit =list((round(x/num_days),2)for x in total_profit_list) # getting avg profit for each summation
        #print(self.avg_profit)     # insert into new avg_year_profit table
            
         
        #print(self.week_price)  
        #print(self.weekly_profit_list)      
        #print(self.dates_week_list)
        #print(profit_list)

        #print(total_profit_list)
        return self.avg_profit,self.keys_list



    def monthly_Profit(self): #past 30 days
        month_delta = datetime.timedelta(weeks=4)
        day_delta = datetime.timedelta(days=2)
        month_end_date = datetime.date.today() - day_delta #yesterday date as today's closing is not available yet
        month_start_date = month_end_date - month_delta 
        cur = self.mydb.cursor()
        cur.execute("SELECT Name,Date,Close from coingeckodata WHERE Date BETWEEN %s AND %s", [month_start_date,month_end_date]) 
        self.month_result = cur.fetchall() 
        self.month_list = self.cal_profit_dict(self.month_result)
        self.monthly_profit_list,self.month_price,self.dates_month_list,self.name_month = self.month_list        
        #print(self.month_price)  
        #print(self.monthly_profit_list)      
        #print(self.dates_month_list)
        #print(self.name_month)

    def avg_month_profit(self):
        month_delta = relativedelta(months=1)    #now only compare 1 month
        day_delta = datetime.timedelta(days=2)
        self.month_end_date = datetime.date.today() - day_delta #yesterday date as today's closing is not available yet
        self.month_start_date = self.month_end_date - month_delta
        #print(month_end_date.month)
        #print(month_start_date.month)
        cur = self.mydb.cursor()
        cur.execute("SELECT Name,Date,Profit from monthlyprofit WHERE Date BETWEEN %s AND %s", [self.month_start_date,self.month_end_date]) 
        self.month_profit = cur.fetchall()
        self.month__avgplist = self.avg_dict(self.month_profit)
        # for name in self.month_result:
        #       print(name) 
        self.month_profit_avg,self.month_coins = self.month__avgplist
        # print(self.month_profit_avg)
        # print(self.month_coins)

    def weekly_Profit(self): #past 30 days
        week_delta = datetime.timedelta(weeks=1)
        day_delta = datetime.timedelta(days=2)
        week_end_date = datetime.date.today() - day_delta #yesterday date as today's closing is not available yet
        week_start_date = week_end_date - week_delta 
        cur = self.mydb.cursor()
        cur.execute("SELECT Name,Date,Close from coingeckodata WHERE Date BETWEEN %s AND %s", [week_start_date,week_end_date]) 
        self.week_result = cur.fetchall() 
        self.weekly_list = self.cal_profit_dict(self.week_result)
        self.weekly_profit_list,self.weekly_price,self.dates_weekly_list,self.name_weekly = self.weekly_list        
        # print(self.weekly_price)  
        # print(self.weekly_profit_list)      
        # print(self.dates_weekly_list)
        # print(self.name_weekly)


    def avg_week_profit(self):
        week_delta = relativedelta(weeks=1)    #now only compare 1 week
        day_delta = datetime.timedelta(days=2)
        self.week_end_date = datetime.date.today() - day_delta #yesterday date as today's closing is not available yet
        self.week_start_date = self.week_end_date - week_delta
        #print(week_end_date.day)
        #print(week_start_date.day)
        cur = self.mydb.cursor()
        cur.execute("SELECT Name,Date,Profit from weeklyprofit WHERE Date BETWEEN %s AND %s", [self.week_start_date,self.week_end_date]) 
        self.week_profit = cur.fetchall()
        self.week__avgplist = self.avg_dict(self.week_profit)
        # for name in self.month_result:
        #       print(name) 
        self.week_profit_avg,self.week_coins = self.week__avgplist
        print(self.week_profit_avg)
        print(self.week_coins)    

    



    def cal_profit_dict(self,arr):
        test_arr = list(item for item in arr)
        #print(week_arr)
        test_dict = defaultdict(list)
        self.test_price=[]
        self.test_date_list=[]
        self.test_name =[]
        self.test_profit_list=[]
        for k,*v in test_arr:
            test_dict[k].append(v)
        #print(dict(test_dict))
        for key,value in test_dict.items():
            #print(key,test_dict[key])
            #today_price_list.append(value[0][1])
            for item in test_dict[key]:
                item[1] = item[1][1:] #remove '$'
                item[1] = item[1].replace(',', '')
                #print(value[0][1],key)
                today_price = value[0][1]
                #print(today_price)
                profit = round((((float(today_price) - float(item[1])) /float(today_price)) *100),2)
                #print(profit)
                self.test_profit_list.append(profit)
                #print(key, item[0], item[1])
                self.test_price.append(item[1])
                self.test_date_list.append(item[0])
                self.test_name.append(key)
        
        #print(self.test_price)  
        #print(self.test_profit_list)      
        #print(self.test_date_list)
        # print(self.test_name)
        return self.test_profit_list,self.test_price,self.test_date_list,self.test_name
    
    
    


 
#gethistoricaldataforallcoin()

call = data_manu()    
call.weekly_Profit()
call.monthly_Profit()
call.yearly_Profit()
call.Insert()
call.avg_year_profit()
call.avg_month_profit()
call.avg_week_profit()
call.InsertBarProfit()