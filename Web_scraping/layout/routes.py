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


def getalltrend():
    try:
        sql = 'SELECT distinct Name, price FROM weeklyprofit Order By Date DESC'
        cursor.execute(sql)
        trend = cursor.fetchall()
        return trend
        mydb.close()
    except:
        print("unable to connect to the weeklyprofit database")
    mydb.close()


trends = getalltrend()


def gettopchart():
    clabels = []
    cvalues = []
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM redditcoinsoccurrence"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[2]
            clabels.append(fname.upper())
            cvalues.append(fvol)
        cmax = max(cvalues)
        if min(cvalues) < 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def gettopnews():
    try:
        sql = 'SELECT * FROM googlenewscryptocurrency Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the googlenewscryptocurrency database")
    mydb.close()


def getyrbtcchart():
    clabels = []
    cvalues = []
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


def getyrethchart():
    clabels = []
    cvalues = []

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


def getyrxrpchart():
    clabels = []
    cvalues = []
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'xrp' Order By Date DESC"
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


def getwkxrpchart():
    clabels = []
    cvalues = []
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'xrp' Order By Date DESC"
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


def getmxrpchart():
    clabels = []
    cvalues = []
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'xrp' Order By Date DESC"
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


def getxrpnews():
    try:
        sql = 'SELECT * FROM googlenewsxrp Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the xrp database")
    mydb.close()


def getxrpcomment():
    try:
        sql = 'SELECT MIN(comment) AS comment, thumbup, thumbdown, reply FROM yahoocommentxrp GROUP BY comment Order By thumbup DESC'
        cursor.execute(sql)
        comments = cursor.fetchall()
        return comments
        mydb.close()
    except:
        print("unable to connect to the xrp database")
    mydb.close()


def getyruniswapchart():
    clabels = []
    cvalues = []
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'uniswap' Order By Date DESC"
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


def getwkuniswapchart():
    clabels = []
    cvalues = []
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'uniswap' Order By Date DESC"
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
        if min(cvalues) <= 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getmuniswapchart():
    clabels = []
    cvalues = []
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'uniswap' Order By Date DESC"
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


def getuniswapnews():
    try:
        sql = 'SELECT * FROM googlenewsuniswap Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the uniswap database")
    mydb.close()


def getuniswapcomment():
    try:
        sql = 'SELECT MIN(comment) AS comment, thumbup, thumbdown, reply FROM yahoocommentuniswap GROUP BY comment Order By thumbup DESC'
        cursor.execute(sql)
        comments = cursor.fetchall()
        return comments
        mydb.close()
    except:
        print("unable to connect to the uniswap database")
    mydb.close()

def getyrlitecoinchart():
    clabels = []
    cvalues = []
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM yearlyprofit WHERE Name like 'litecoin' Order By Date DESC"
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


def getwklitecoinchart():
    clabels = []
    cvalues = []
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'litecoin' Order By Date DESC"
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
        if min(cvalues) <= 0:
            cmin = min(cvalues)
        return clabels, cvalues, cmax, cmin
    except:
        print("Error: unable to fetch data")


def getmlitecoinchart():
    clabels = []
    cvalues = []
    cmax = 0
    cmin = 0
    sql = "SELECT * FROM monthlyprofit WHERE Name like 'litecoin' Order By Date DESC"
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


def getlitecoinnews():
    try:
        sql = 'SELECT * FROM googlenewslitecoin Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the litecoin database")
    mydb.close()


def getlitecoincomment():
    try:
        sql = 'SELECT MIN(comment) AS comment, thumbup, thumbdown, reply FROM yahoocommentlitecoin GROUP BY comment Order By thumbup DESC'
        cursor.execute(sql)
        comments = cursor.fetchall()
        return comments
        mydb.close()
    except:
        print("unable to connect to the litecoin database")
    mydb.close()


@app.route('/dash2')
def dash2():
    line_labels, line_values, cmax, cmin = gettopchart()
    news = gettopnews()
    title = "dash 2"
    title2 = "test only"
    return render_template('testindex.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, trends=trends)


@app.route('/')
@app.route('/dash')
def dash():
    line_labels, line_values, cmax, cmin = gettopchart()
    news = gettopnews()
    title = "World's"
    title2 = "Top Coin"
    return render_template('dash-2.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, trends=trends)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


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
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/xrp')
def xrp():
    line_labels, line_values, cmax, cmin = getyrxrpchart()
    news = getxrpnews()
    comments = getxrpcomment()
    title = "XRP"
    title2 = "Yearly Data"
    wkbtc = '/wkxrp'
    monbtc = '/monxrp'
    yrbtc = '/xrp'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkxrp')
def wkxrp():
    line_labels, line_values, cmax, cmin = getwkxrpchart()
    news = getxrpnews()
    comments = getxrpcomment()
    title = "XRP"
    title2 = "Weekly Data"
    wkbtc = '/wkxrp'
    monbtc = '/monxrp'
    yrbtc = '/xrp'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monxrp')
def monxrp():
    line_labels, line_values, cmax, cmin = getmxrpchart()
    news = getpolkadotnews()
    comments = getpolkadotcomment()
    title = "XRP"
    title2 = "Monthly Data"
    wkbtc = '/wkxrp'
    monbtc = '/monxrp'
    yrbtc = '/xrp'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/uniswap')
def uniswap():
    line_labels, line_values, cmax, cmin = getyruniswapchart()
    news = getuniswapnews()
    comments = getuniswapcomment()
    title = "Uniswap"
    title2 = "Yearly Data"
    wkbtc = '/wkuniswap'
    monbtc = '/monuniswap'
    yrbtc = '/uniswap'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkuniswap')
def wkuniswap():
    line_labels, line_values, cmax, cmin = getwkuniswapchart()
    news = getuniswapnews()
    comments = getuniswapcomment()
    title = "Uniswap"
    title2 = "Weekly Data"
    wkbtc = '/wkuniswap'
    monbtc = '/monuniswap'
    yrbtc = '/uniswap'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monuniswap')
def monuniswap():
    line_labels, line_values, cmax, cmin = getmuniswapchart()
    news = getuniswapnews()
    comments = getuniswapcomment()
    title = "Uniswap"
    title2 = "Monthly Data"
    wkbtc = '/wkuniswap'
    monbtc = '/monuniswap'
    yrbtc = '/uniswap'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/litecoin')
def litecoin():
    line_labels, line_values, cmax, cmin = getyrlitecoinchart()
    news = getlitecoinnews()
    comments = getlitecoincomment()
    title = "litecoin"
    title2 = "Yearly Data"
    wkbtc = '/wklitecoin'
    monbtc = '/monlitecoin'
    yrbtc = '/litecoin'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wklitecoin')
def wklitecoin():
    line_labels, line_values, cmax, cmin = getwklitecoinchart()
    news = getlitecoinnews()
    comments = getlitecoincomment()
    title = "litecoin"
    title2 = "Weekly Data"
    wkbtc = '/wklitecoin'
    monbtc = '/monlitecoin'
    yrbtc = '/litecoin'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monlitecoin')
def monlitecoin():
    line_labels, line_values, cmax, cmin = getmlitecoinchart()
    news = getlitecoinnews()
    comments = getlitecoincomment()
    title = "litecoin"
    title2 = "Monthly Data"
    wkbtc = '/wklitecoin'
    monbtc = '/monlitecoin'
    yrbtc = '/litecoin'
    return render_template('index.html', title=title, title2=title2, max=cmax, min=cmin, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)
