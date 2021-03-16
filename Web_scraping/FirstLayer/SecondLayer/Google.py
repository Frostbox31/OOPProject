from SecondLayer.Utilities import checkmonth, checkyear, _getrandomheader
from numpy.random import random_integers
import requests
from bs4 import BeautifulSoup
import mysql.connector
import re
from datetime import date
import numpy as np
from time import sleep
import random


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="F2814939p",
  database="DataProject"
)

def getGoogleNew(topic):
    
    url = 'https://www.google.com/search?q='+topic+'&tbm=nws'
    title = []
    link = []
    time = []
    number = 0

    while number < 100: 

        delays = [7, 8, 10, 12]
        delay = np.random.choice(delays)
        sleep(delay)

        request = requests.get(url)
        soup = BeautifulSoup(request.content, 'html.parser')

        for match in soup.find_all('div',class_='BNeawe vvjwJb AP7Wnd'):
            title.insert(len(title),match.text)

        for match in soup.find_all('a',href=lambda value:value and value.startswith("/url")):
            if (match['href'].replace('/url?q=','').split('&sa')[0]) not in link:
                if('support.google.com' not in match['href'] and 'accounts.google.com' not in match['href']):
                    link.insert(len(link),match['href'].replace('/url?q=','').split('&sa')[0])

        for match in soup.find_all('span',class_='r0bn4c rQMQod'):
            if 'sec' in match.get_text(strip=True):
                convert = int(re.sub('[^0-9]','', match.text))
                time.insert(len(time),convert)
            elif 'min' in match.get_text(strip=True):
                convert = int(re.sub('[^0-9]','', match.text))*60
                time.insert(len(time),convert)
            elif 'hour' in match.get_text(strip=True):
                convert = int(re.sub('[^0-9]','', match.text))*60*60
                time.insert(len(time),convert)
            elif 'day' in match.get_text(strip=True):
                convert = int(re.sub('[^0-9]','', match.text))*24*60*60
                time.insert(len(time),convert)
            elif 'week' in match.get_text(strip=True):
                convert = int(re.sub('[^0-9]','', match.text))*7*24*60*60
                time.insert(len(time),convert)
            elif 'month' in match.get_text(strip=True):
                convert = int(re.sub('[^0-9]','', match.text))*checkmonth(date.today().month)*24*60*60
                time.insert(len(time),convert)
            elif 'year' in match.get_text(strip=True):
                convert = int(re.sub('[^0-9]','', match.text))*checkyear(date.today().year)*24*60*60
                time.insert(len(time),convert)
        try:
            url = "https://www.google.com" + soup.find(attrs={"aria-label": 'Next page'})['href'];
            number += 1
        except:
            number = 100
    
    print(str(topic).replace(" ",""))

    mycursor = mydb.cursor()
    sql = "CREATE Table IF NOT EXISTS googlenews" + str(topic).replace(" ","") + "(id integer NOT NULL AUTO_INCREMENT,Title varchar(200) DEFAULT NULL,Link varchar(500) DEFAULT NULL,Time int DEFAULT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=281 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
    mycursor.execute(sql,'')
    sql = "DELETE FROM googlenews" + str(topic).replace(" ","")
    mycursor.execute(sql,'')  
    for x in range (len(link)):
        sql = "INSERT INTO Googlenews" + str(topic).replace(" ","") +" (id,Title, link, time) VALUES (%s,%s, %s, %s)"
        val = (x+1,str(title[x]),str(link[x]),str(time[x]))
        mycursor.execute(sql, val)

    mydb.commit()
pass


    



