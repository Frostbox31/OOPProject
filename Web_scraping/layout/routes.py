from layout import app
from flask import render_template

import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="F2814939p",
    database="DataProject"
)

def getbtcnews():
    try:
        print("db connected")
        cursor = mydb.cursor()
        sql = 'SELECT * FROM googlenewsbitcoin Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the bitcoin database")
    mydb.close()


def getethnews():
    try:
        print("db connected")
        cursor = mydb.cursor()
        sql = 'SELECT * FROM googlenewsethereum Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the ethereum database")
    mydb.close()

# testing trendcheck
def trendcheck():
    ldate = []
    lvalue = []
    try:
        cursor = mydb.cursor()
        # sql = 'SELECT * FROM coingeckodata WHERE Name like "bitcoin" Order By Date DESC'
        # sql = 'SELECT * FROM dataproject.coingeckodata AS t1 WHERE EXISTS(SELECT * FROM dataproject.coingeckodata AS t2 WHERE  t2.Name=t1.NameAND t2.Open > t1.Open) Order By Date DESC'
        sql = 'SELECT * FROM coingeckodata ORDER BY Date DESC'
        cursor.execute(sql)
        trend = cursor.fetchmany(size = 2)
        for row in trend:
            ldate.append = row[1]
            lvalue.append = row[2]
        if lvalue[0] < lvalue[1]:
            return('%d < %d', lvalue[0], lvalue[1])
        mydb.close()
    except:
        print ("unable to connect to the ethereum database")
    mydb.close()
    
blabels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

bvalues = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

tvalues = [
    1090.03, 2104.09, 2430.75, 2030.11,
    5370.85, 6160.51, 6180.27, 6540.93,
    8890.16, 11700.89, 13120.04, 15600.09
]

tlabels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]


colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


@app.route('/')
@app.route('/dash')
def dash():
    line_labels = blabels
    line_values = bvalues
    return render_template('index.html', title='Dashboard', max=99999999, labels=line_labels, values=line_values)


@app.route('/bitcoin')
def bitcoin():
    line_labels = blabels
    line_values = bvalues
    news = getbtcnews()
    #trendcheck()
    trend = 'trending-down'
    return render_template('index.html', title='Bitcoin', max=17000, labels=line_labels, values=line_values, news = news, trend = trend)


@app.route('/ethereum')
def ethereum():
    line_labels = tlabels
    line_values = tvalues
    news = getethnews()
    return render_template('index.html', title='Ethereum', max=17000, labels=line_labels, values=line_values, news = news)


@app.route('/home')
def homepage():
    return render_template('homepage.html', title='homepage')
