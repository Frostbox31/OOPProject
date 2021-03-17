
import requests
from bs4 import BeautifulSoup
import random
import sys
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  #password="F2814939p",
  password="",
  database="DataProject"
)

proxieslist = [] # Will contain proxies [ip, port]

def checkmonth(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 30
    else :
        return 31

def checkyear(year):
    if year % 4 == 0 :
        return 366
    else :
        return 365

def _getrandomproxy():

    Hypertext = ["https"]

    proxies_req = requests.get('https://www.sslproxies.org/')
    soup = BeautifulSoup(proxies_req.content, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

    for row in proxies_table.tbody.find_all('tr'):
        proxy = random.choice(Hypertext);
        proxieslist.append({
        proxy: proxy+'://'+row.find_all('td')[0].string + ":"+ row.find_all('td')[1].string,
    })

    return proxieslist
pass

def _getrandomheader():

    headers_list = [
    # Firefox 77 Mac
     {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    },
    # Firefox 77 Windows
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    },
    # Chrome 83 Mac
    {
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    },
    # Chrome 83 Windows 
    {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }
    ]
    return random.choice(headers_list)

def _writefile(file):
    with open('test.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(file)

def commitsqlcommand(sqlparam,valparam):

    mycursor = mydb.cursor()
    sql = sqlparam
    val = valparam
    mycursor.execute(sql,val)  
    
    mydb.commit();
pass

def selectsqlcommand(sqlparam,valparam):

    mycursor = mydb.cursor()
    sql = sqlparam
    val = valparam
    mycursor.execute(sql,val)  
    return  mycursor.fetchall()
pass




    