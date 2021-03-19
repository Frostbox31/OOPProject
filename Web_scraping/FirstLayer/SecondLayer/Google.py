from SecondLayer.Utilities import _commitSQLCommand,checkMonth,checkYear,_getRandomHeader
import requests
from bs4 import BeautifulSoup
import re
from datetime import date
import numpy as np
from time import sleep

def _getGoogleNews(coinname): #Get Cryptocurrency and Top 10 Coins Google News
    
    url = 'https://www.google.com/search?q='+coinname+'&tbm=nws'
    title = []
    link = []
    time = []
    number = 0

    while number < 100: 

        delays = [7, 8, 10, 12]
        delay = np.random.choice(delays)
        sleep(delay)

        request = requests.get(url,headers=_getRandomHeader())
        soup = BeautifulSoup(request.content, 'html.parser')

        for match in soup.find_all('div',class_='BNeawe vvjwJb AP7Wnd'):
            title.insert(len(title),match.text)

        for match in soup.find_all('a',href=lambda value:value and value.startswith("/url")):
            if (match['href'].replace('/url?q=','').split('&sa')[0]) not in link:
                if('support.google.com' not in match['href'] and 'accounts.google.com' not in match['href']):
                    link.insert(len(link),match['href'].replace('/url?q=','').split('&sa')[0])

        #Convert the years/month/days/hours/mins into seconds
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
                convert = int(re.sub('[^0-9]','', match.text))*checkMonth(date.today().month)*24*60*60
                time.insert(len(time),convert)
            elif 'year' in match.get_text(strip=True):
                convert = int(re.sub('[^0-9]','', match.text))*checkYear(date.today().year)*24*60*60
                time.insert(len(time),convert)
        try:
            url = "https://www.google.com" + soup.find(attrs={"aria-label": 'Next page'})['href'];
            number += 1
        except: #If it fail to find the next page of the Google News, it end the loop
            number = 100
    
    _commitSQLCommand("CREATE Table IF NOT EXISTS googlenews" + str(coinname).replace(" ","") + "(id integer NOT NULL AUTO_INCREMENT,Title varchar(200) DEFAULT NULL,Link varchar(500) DEFAULT NULL,Time int DEFAULT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=281 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;",'')
    _commitSQLCommand("DELETE FROM googlenews" + str(coinname).replace(" ",""),'')

    for x in range (len(link)):
        _commitSQLCommand("INSERT INTO Googlenews" + str(coinname).replace(" ","") +" (id,Title, link, time) VALUES (%s,%s, %s, %s)",(x+1,str(title[x]),str(link[x]),str(time[x])))
pass


    



