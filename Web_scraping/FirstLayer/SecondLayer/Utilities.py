
import random
import sys
import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="F2814939p",
  #password="",
  database="DataProject"
)

proxieslist = [] # Will contain proxies [ip, port]

def checkMonth(month): #Check the days in the month
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 30
    else :
        return 31
pass

def checkYear(year): # Check for leap year
    if year % 4 == 0 :
        return 366
    else :
        return 365
pass

#def _getRandomProxy(): #Provide free Proxies for Web Scrapping to prevent detection from the parties

#    Hypertext = ["http"]
#    request = requests.get('https://www.sslproxies.org/')
#    soup = BeautifulSoup(request.content, 'html.parser')
#    proxies_table = soup.find(id='proxylisttable')

#    for row in proxies_table.tbody.find_all('tr'):
#        proxy = random.choice(Hypertext);
#        proxieslist.append({proxy: proxy+'://'+row.find_all('td')[0].string + ":"+ row.find_all('td')[1].string,})

#    return proxieslist
#pass

def _getRandomHeader(): #Provide Headers for Web Scrapping to prevent detection from the parties

    #User-Agent                 = 
    #DNT                        =   0 allow to be track by the target site, 1 does not allow to be track by the target site,
    #Accept                     =   It specific what type of content to be accept
    #Accept - Language          =   State the language that allow the application to understand while request
    #Accept - Encoding          =   It compression the algorithm and allow to understand
    #Referer                    =   It stated the website that previously visit before the request
    #Connection                 =   It stated whether the network should be closed or open
    #Upgrade-Insecure-Requests  =   It Encrypted and authenticated the response
    

    headers_list = [
    # Firefox 77 Mac
     {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Referer": "https://www.google.com.sg/",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1"
    },
    # Firefox 77 Windows
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Referer": "https://www.google.com.my/",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1"
    },
    # Chrome 83 Mac
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Referer": "https://www.google.com.tw/",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",

    },
    # Chrome 83 Windows 
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Referer": "https://www.google.com.jp/",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
    }
    ]
    return random.choice(headers_list)
pass

def _writeFile(file): #Write into a Text File
    with open('test.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(file)
pass

def _commitSQLCommand(sqlParam,valParam): #Insert,Delete,Update SQL 
    cursor = db.cursor()
    sql = sqlParam
    val = valParam
    cursor.execute(sql,val)  
    db.commit();
pass

def _selectSQLCommand(sqlparam,valParam): #Retrieve data from SQL
    cursor = db.cursor()
    sql = sqlparam
    val = valParam
    cursor.execute(sql,val)  
    return  cursor.fetchall()
pass




    