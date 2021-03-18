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

        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fetch data")


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
    cmin = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'bitcoin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getwkbtcchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'bitcoin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getmbtcchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'bitcoin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


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


def getbtccomment():
    try:
        sql = 'SELECT MIN(comment) AS comment, thumbup, thumbdown, reply FROM yahoocommentbitcoin GROUP BY comment Order By thumbup DESC'
        cursor.execute(sql)
        comments = cursor.fetchall()
        return comments
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

        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        return clabels, cvalues, cmax
    except:
        print("Error: unable to fetch data")


def getyrethchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'ethereum' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getwkethchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'ethereum' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getmethchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'ethereum' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


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

def getethcomment():
    try:
        sql = 'SELECT MIN(comment) AS comment, thumbup, thumbdown, reply FROM yahoocommentethereum GROUP BY comment Order By thumbup DESC'
        cursor.execute(sql)
        comments = cursor.fetchall()
        return comments
        mydb.close()
    except:
        print("unable to connect to the ethereum database")
    mydb.close()

def getyrtetchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'tether' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getwktetchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'tether' Order By Date DESC"

    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]

            clabels.append(fname)
            cvalues.append(fvol)

        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getmtetchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'tether' Order By Date DESC"

    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]

            clabels.append(fname)
            cvalues.append(fvol)

        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


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

def gettetcomment():
    try:
        sql = 'SELECT MIN(comment) AS comment, thumbup, thumbdown, reply FROM yahoocommenttether GROUP BY comment Order By thumbup DESC'
        cursor.execute(sql)
        comments = cursor.fetchall()
        return comments
        mydb.close()
    except:
        print("unable to connect to the tether database")
    mydb.close()

def getyrcarchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'cardano' Order By Date DESC"

    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]

            clabels.append(fname)
            cvalues.append(fvol)

        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getwkcarchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'cardano' Order By Date DESC"

    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]

            clabels.append(fname)
            cvalues.append(fvol)

        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getmcarchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'cardano' Order By Date DESC"

    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]

            clabels.append(fname)
            cvalues.append(fvol)

        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
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

def getcarcomment():
    try:
        sql = 'SELECT MIN(comment) AS comment, thumbup, thumbdown, reply FROM yahoocommentcardano GROUP BY comment Order By thumbup DESC'
        cursor.execute(sql)
        comments = cursor.fetchall()
        return comments
        mydb.close()
    except:
        print("unable to connect to the cardano database")
    mydb.close()

def getyrbinancechart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'binance-coin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getwkbinancechart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'binance-coin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getmbinancechart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'binance-coin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
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

def getbinancecomment():
    try:
        sql = 'SELECT MIN(comment) AS comment, thumbup, thumbdown, reply FROM yahoocommentbinancecoin GROUP BY comment Order By thumbup DESC'
        cursor.execute(sql)
        comments = cursor.fetchall()
        return comments
        mydb.close()
    except:
        print("unable to connect to the binance coin database")
    mydb.close()

def getyrpolkadotchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'polkadot' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getwkpolkadotchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'polkadot' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getmpolkadotchart():
    clabels = []
    cvalues = []
    count = 0
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'polkadot' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(fvol)
        clabels.reverse()
        cvalues.reverse()
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getpolkadotnews():
    try:
        sql = 'SELECT * FROM googlenewspolkadot Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the polkadot database")
    mydb.close()

def getpolkadotcomment():
    try:
        sql = 'SELECT MIN(comment) AS comment, thumbup, thumbdown, reply FROM yahoocommentpolkadot GROUP BY comment Order By thumbup DESC'
        cursor.execute(sql)
        comments = cursor.fetchall()
        return comments
        mydb.close()
    except:
        print("unable to connect to the polkadot database")
    mydb.close()

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


@app.route('/home')
def homepage():
    return render_template('homepage.html', title='homepage')


@app.route('/')
@app.route('/bitcoin')
def bitcoin():
    line_labels, line_values, cmax, cmin = getyrbtcchart()
    news = getbtcnews()
    comments = getbtccomment()
    title = "Bitcoin"
    title2 = "Yearly Data"
    wkbtc = '/wkbitcoin'
    monbtc = '/monbitcoin'
    yrbtc = '/bitcoin'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkbitcoin')
def wkbitcoin():
    line_labels, line_values, cmax, cmin = getwkbtcchart()
    news = getbtcnews()
    comments = getbtccomment()
    title = "Bitcoin"
    title2 = "Weekly Data"
    wkbtc = '/wkbitcoin'
    monbtc = '/monbitcoin'
    yrbtc = '/bitcoin'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monbitcoin')
def monbitcoin():
    line_labels, line_values, cmax, cmin = getmbtcchart()
    news = getbtcnews()
    comments = getbtccomment()
    title = "Bitcoin"
    title2 = "Monthly Data"
    wkbtc = '/wkbitcoin'
    monbtc = '/monbitcoin'
    yrbtc = '/bitcoin'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/ethereum')
def ethereum():
    line_labels, line_values, cmax, cmin = getyrethchart()
    news = getethnews()
    comments = getethcomment()
    title = "Ethereum"
    title2 = "Yearly Data"
    wkbtc = '/wkethereum'
    monbtc = '/monethereum'
    yrbtc = '/ethereum'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkethereum')
def wkethereum():
    line_labels, line_values, cmax, cmin = getwkethchart()
    news = getethnews()
    comments = getethcomment()
    title = "Ethereum"
    title2 = "Weekly Data"
    wkbtc = '/wkethereum'
    monbtc = '/monethereum'
    yrbtc = '/ethereum'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monethereum')
def monethereum():
    line_labels, line_values, cmax, cmin = getmethchart()
    news = getethnews()
    comments = getethcomment()
    title = "Ethereum"
    title2 = "Monthly Data"
    wkbtc = '/wkethereum'
    monbtc = '/monethereum'
    yrbtc = '/ethereum'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/tether')
def tether():
    line_labels, line_values, cmax, cmin = getyrethchart()
    news = gettetnews()
    comments = gettetcomment()
    title = "Tether"
    title2 = "Yearly Data"
    wkbtc = '/wktether'
    monbtc = '/montether'
    yrbtc = '/tether'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wktether')
def wktether():
    line_labels, line_values, cmax, cmin = getwkethchart()
    news = gettetnews()
    comments = gettetcomment()
    title = "Tether"
    title2 = "Weekly Data"
    wkbtc = '/wktether'
    monbtc = '/montether'
    yrbtc = '/tether'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/montether')
def montether():
    line_labels, line_values, cmax, cmin = getmethchart()
    news = gettetnews()
    comments = gettetcomment()
    title = "Tether"
    title2 = "Monthly Data"
    wkbtc = '/wktether'
    monbtc = '/montether'
    yrbtc = '/tether'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/cardano')
def cardano():
    line_labels, line_values, cmax, cmin = getyrcarchart()
    news = getcarnews()
    comments = getcarcomment()
    title = "Cardano"
    title2 = "Yearly Data"
    wkbtc = '/wkcardano'
    monbtc = '/moncardano2'
    yrbtc = '/cardano'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkcardano')
def wkcardano():
    line_labels, line_values, cmax, cmin = getwkcarchart()
    news = getcarnews()
    comments = getcarcomment()
    title = "Cardano"
    title2 = "Weekly Data"
    wkbtc = '/wkcardano'
    monbtc = '/moncardano2'
    yrbtc = '/cardano'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/moncardano2')
def moncardano2():
    line_labels, line_values, cmax, cmin = getmcarchart()
    news = getcarnews()
    comments = getcarcomment()
    title = "Cardano"
    title2 = "Monthly Data"
    wkbtc = '/wkcardano'
    monbtc = '/moncardano2'
    yrbtc = '/cardano'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/binance')
def binance():
    line_labels, line_values, cmax, cmin = getyrbinancechart()
    news = getbinancenews()
    comments = getbinancecomment()
    title = "Binance Coin"
    title2 = "Yearly Data"
    wkbtc = '/wkbinance'
    monbtc = '/monbinance'
    yrbtc = '/binance'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkbinance')
def wkbinance():
    line_labels, line_values, cmax, cmin = getwkbinancechart()
    news = getbinancenews()
    comments = getbinancecomment()
    title = "Binance Coin"
    title2 = "Weekly Data"
    wkbtc = '/wkbinance'
    monbtc = '/monbinance'
    yrbtc = '/binance'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monbinance')
def moncardano():
    line_labels, line_values, cmax, cmin = getmbinancechart()
    news = getbinancenews()
    comments = getbinancecomment()
    title = "Binance Coin"
    title2 = "Monthly Data"
    wkbtc = '/wkbinance'
    monbtc = '/monbinance'
    yrbtc = '/binance'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/polkadot')
def polkadot():
    line_labels, line_values, cmax, cmin = getyrpolkadotchart()
    news = getpolkadotnews()
    comments = getpolkadotcomment()
    title = "Polkadot"
    title2 = "Yearly Data"
    wkbtc = '/wkpolkadot'
    monbtc = '/monpolkadot'
    yrbtc = '/polkadot'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkpolkadot')
def wkpolkadot():
    line_labels, line_values, cmax, cmin = getwkpolkadotchart()
    news = getpolkadotnews()
    comments = getpolkadotcomment()
    title = "Polkadot"
    title2 = "Weekly Data"
    wkbtc = '/wkpolkadot'
    monbtc = '/monpolkadot'
    yrbtc = '/polkadot'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monpolkadot')
def monpolkadot():
    line_labels, line_values, cmax, cmin = getmpolkadotchart()
    news = getpolkadotnews()
    comments = getpolkadotcomment()
    title = "Polkadot"
    title2 = "Monthly Data"
    wkbtc = '/wkpolkadot'
    monbtc = '/monpolkadot'
    yrbtc = '/polkadot'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)
