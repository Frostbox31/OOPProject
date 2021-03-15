
import requests
from bs4 import BeautifulSoup

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
    proxies_req = requests.get('https://www.sslproxies.org/')
    soup = BeautifulSoup(proxies_req.content, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

    for row in proxies_table.tbody.find_all('tr'):
        proxieslist.append({
        'http': 'http://'+row.find_all('td')[0].string + ":"+ row.find_all('td')[1].string,
        #'https': 'https://'+row.find_all('td')[0].string + ":"+ row.find_all('td')[1].string
    })
    