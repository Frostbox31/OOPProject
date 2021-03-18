from layout import app
from flask import render_template

import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="F2814939p",
    database="DataProject"
)

cursor = mydb.cursor()


def gettopchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT DISCTINT FROM weeklyprofit Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            if count <= 10:
                fname = row[1]
                fvol = row[2]
                # Now print fetched result
                print("fname = %s, fvol = %d \n" %
                      (fname, fvol))
                clabels.append(fname)
                cvalues.append(fvol)
                count += 1
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fecth data")


def gettopnews():
    try:
        sql = 'SELECT * FROM googlenewsbitcoin Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the bitcoin database")
    mydb.close()


def getyrbtcchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'bitcoin' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fecth data")


def getwkbtcchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'bitcoin' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fecth data")


def getmbtcchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'bitcoin' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fecth data")


def getbtcnews():
    try:
        sql = 'SELECT * FROM googlenewsbitcoin Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the bitcoin database")
    mydb.close()


def sample():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'ethereum' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            if count <= 10:
                fname = row[1]
                fvol = row[2]
                # Now print fetched result
                print("fname = %s, fvol = %d \n" %
                      (fname, fvol))
                clabels.append(fname)
                cvalues.append(fvol)
                count += 1
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fecth data")


def getyrethchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'ethereum' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fecth data")


def getwkethchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'ethereum' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fecth data")


def getmethchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'ethereum' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fecth data")


def getethnews():
    try:
        sql = 'SELECT * FROM googlenewsethereum Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the ethereum database")
    mydb.close()


def getyrtetchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'tether' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fecth data")


def getwktetchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'tether' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fecth data")


def getmtetchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'tether' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fecth data")


def gettetnews():
    try:
        sql = 'SELECT * FROM googlenewstether Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the tether database")
    mydb.close()


def getyrcarchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'cardano' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fetch data")


def getwkcarchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'cardano' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fetch data")

def getmncarchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'cardano' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fetch data")


def getcarnews():
    try:
        sql = 'SELECT * FROM googlenewscardano Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the cardano database")
    mydb.close()


def getyrbinancechart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'binance-coin' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fetch data")


def getwkbinancechart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'binance-coin' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fetch data")


def getmbinancechart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'binance-coin' Order By Date DESC"
    #sql2 = "SELECT MAX(Price) FROM dataproject.monthlyprofit WHERE Name like 'bitcoin'"
    # sql = "SELECT * FROM coinvolume"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("fname = %s, fvol = %d \n" %
                  (fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
        print(clabels, cvalues)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fetch data")


def getbinancenews():
    try:
        sql = 'SELECT * FROM googlenewsbinancecoin Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the binance database")
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
        trend = cursor.fetchmany(size=2)
        for row in trend:
            ldate.append = row[1]
            lvalue.append = row[2]
        if lvalue[0] < lvalue[1]:
            return('%d < %d', lvalue[0], lvalue[1])
        mydb.close()
    except:
        print("unable to connect to the ethereum database")
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


@app.route('/dash')
def dash():
    line_labels, line_values, cmax = getmbtcchart()
    return render_template('index.html', title='Top 10 coins', max=cmax, labels=line_labels, values=line_values)


@app.route('/')
@app.route('/bitcoin')
def bitcoin():
    line_labels, line_values, cmax = getyrbtcchart()
    news = getbtcnews()
    wkbtc = '/wkbitcoin'
    monbtc = '/monbitcoin'
    yrbtc = '/bitcoin'
    return render_template('index.html', title='Bitcoin', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkbitcoin')
def wkbitcoin():
    line_labels, line_values, cmax, cmin = getwkbtcchart()
    news = getbtcnews()
    wkbtc = '/wkbitcoin'
    monbtc = '/monbitcoin'
    yrbtc = '/bitcoin'
    return render_template('index.html', title='Bitcoin', max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monbitcoin')
def monbitcoin():
    line_labels, line_values, cmax = getmbtcchart()
    news = getbtcnews()
    wkbtc = '/wkbitcoin'
    monbtc = '/monbitcoin'
    yrbtc = '/bitcoin'
    return render_template('index.html', title='Bitcoin', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/ethereum')
def ethereum():
    line_labels, line_values, cmax = getyrethchart()
    news = getethnews()
    wkbtc = '/wkethereum'
    monbtc = '/monethereum'
    yrbtc = '/ethereum'
    return render_template('index.html', title='Ethereum', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkethereum')
def wkethereum():
    line_labels, line_values, cmax = getwkethchart()
    news = getethnews()
    wkbtc = '/wkethereum'
    monbtc = '/monethereum'
    yrbtc = '/ethereum'
    return render_template('index.html', title='Ethereum', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monethereum')
def monethereum():
    line_labels, line_values, cmax = getmethchart()
    news = getethnews()
    wkbtc = '/wkethereum'
    monbtc = '/monethereum'
    yrbtc = '/ethereum'
    return render_template('index.html', title='Ethereum', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/tether')
def tether():
    line_labels, line_values, cmax = getyrethchart()
    news = gettetnews()
    wkbtc = '/wktether'
    monbtc = '/montether'
    yrbtc = '/tether'
    return render_template('index.html', title='Tether', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wktether')
def wktether():
    line_labels, line_values, cmax = getwkethchart()
    news = gettetnews()
    wkbtc = '/wktether'
    monbtc = '/montether'
    yrbtc = '/tether'
    return render_template('index.html', title='Tether', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/montether')
def montether():
    line_labels, line_values, cmax = getmethchart()
    news = gettetnews()
    wkbtc = '/wktether'
    monbtc = '/montether'
    yrbtc = '/tether'
    return render_template('index.html', title='Tether', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/cardano')
def cardano():
    line_labels, line_values, cmax = getyrcarchart()
    news = getcarnews()
    wkbtc = '/wkcardano'
    monbtc = '/moncardano'
    yrbtc = '/cardano'
    return render_template('index.html', title='Cardano', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkcardano')
def wkcardano():
    line_labels, line_values, cmax = getwkcarchart()
    news = getcarnews()
    wkbtc = '/wkcardano'
    monbtc = '/moncardano'
    yrbtc = '/cardano'
    return render_template('index.html', title='Cardano', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


# @app.route('/moncardano')
# def moncardano():
#     line_labels, line_values, cmax = getmncarchart()
#     news = getcarnews()
#     wkbtc = '/wkcardano'
#     monbtc = '/moncardano'
#     yrbtc = '/cardano'
#     return render_template('index.html', title='Cardano', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/binance')
def binance():
    line_labels, line_values, cmax = getyrbinancechart()
    news = getbinancenews()
    wkbtc = '/wkbinance'
    monbtc = '/monbinance'
    yrbtc = '/binance'
    return render_template('index.html', title='Binance', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkbinance')
def wkbinance():
    line_labels, line_values, cmax = getwkbinancechart()
    news = getbinancenews()
    wkbtc = '/wkbinance'
    monbtc = '/monbinance'
    yrbtc = '/binance'
    return render_template('index.html', title='Binance', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monbinance')
def moncardano():
    line_labels, line_values, cmax = getmbinancechart()
    news = getbinancenews()
    wkbtc = '/wkbinance'
    monbtc = '/monbinance'
    yrbtc = '/binance'
    return render_template('index.html', title='Binance', max=cmax, labels=line_labels, values=line_values, news=news, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/home')
def homepage():
    return render_template('homepage.html', title='homepage')
