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

def gettotalvolumefortheday():
    
    mycursor = mydb.cursor()
    sql = 'SELECT Volume FROM coinvolume where name = "Total Volume"'
    mycursor.execute(sql)  

    totalvolume =  mycursor.fetchall()

    return str(totalvolume[0]).replace('(','').replace(')','').replace(',','')
pass

def getcoinsname():
    
    mycursor = mydb.cursor()
    sql = 'SELECT DISTINCT name FROM coingeckodata'
    mycursor.execute(sql)  

    return mycursor.fetchall()
pass
