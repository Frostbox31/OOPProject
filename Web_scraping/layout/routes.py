from layout import app
from flask import render_template

import mysql.connector

#----connect sql----#
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="F2814939p",
    database="DataProject"
)

cursor = mydb.cursor()

#----retrieve weeklyprofit to display on marquee top coin----#
def getalltrend():
    try:
        sql = 'SELECT distinct Name, price FROM weeklyprofit Order By Date DESC LIMIT 10'
        cursor.execute(sql)
        trend = cursor.fetchall()
        return trend
        mydb.close()
    except:
        print("unable to connect to the weeklyprofit database")
    mydb.close()


trends = getalltrend()

#----retrieve redditcoinoccurrence and display on dashboard chart----#
def gettopchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM redditcoinsoccurrence"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]  # take column 1 of the table
            fvol = row[2]  # take column 2 of the table
            clabels.append(fname.upper())  # set label name as all uppercase
            cvalues.append(round(fvol, 2))  # round off to 2 decimal place
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")

#----retrieve world news from google about cryptocurrency----#
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

#----Dashboard display of yearly, monthly, weekly chart----#
def getyrdashchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM baryearlyprofit"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[0]
            fvol = row[3]
            clabels.append(fname.upper())
            cvalues.append(round(fvol, 2))
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getwkdashchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM barweeklyprofit"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[0]
            fvol = row[3]
            clabels.append(fname.upper())
            cvalues.append(round(fvol, 2))
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getmdashchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM barmonthlyprofit"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[0]
            fvol = row[3]
            clabels.append(fname.upper())
            cvalues.append(round(fvol, 2))
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")
#----end----#

#----bitcoin display of yearly, monthly, weekly chart, news, comments----#
def getyrbtcchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM yearlyprofit WHERE Name like 'bitcoin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getwkbtcchart():
    clabels = []
    cvalues = []
    sql = "SELECT * FROM weeklyprofit WHERE Name like 'bitcoin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getmbtcchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM monthlyprofit WHERE Name like 'bitcoin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
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
#----end----#

#----ethereum display of yearly, monthly, weekly chart, news, comments----#
def getyrethchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM yearlyprofit WHERE Name like 'ethereum' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getwkethchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM weeklyprofit WHERE Name like 'ethereum' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getmethchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM monthlyprofit WHERE Name like 'ethereum' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
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
#----end----#

#----tether display of yearly, monthly, weekly chart, news, comments----#
def getyrtetchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM yearlyprofit WHERE Name like 'tether' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getwktetchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM weeklyprofit WHERE Name like 'tether' Order By Date DESC"

    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]

            clabels.append(fname)
            cvalues.append(round(fvol, 2))

        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getmtetchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM monthlyprofit WHERE Name like 'tether' Order By Date DESC"

    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]

            clabels.append(fname)
            cvalues.append(round(fvol, 2))

        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
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
#----end----#

#----cardano display of yearly, monthly, weekly chart, news, comments----#
def getyrcarchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM yearlyprofit WHERE Name like 'cardano' Order By Date DESC"

    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]

            clabels.append(fname)
            cvalues.append(round(fvol, 2))

        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getwkcarchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM weeklyprofit WHERE Name like 'cardano' Order By Date DESC"

    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]

            clabels.append(fname)
            cvalues.append(round(fvol, 2))

        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getmcarchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM monthlyprofit WHERE Name like 'cardano' Order By Date DESC"

    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]

            clabels.append(fname)
            cvalues.append(round(fvol, 2))

        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
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
#----end----#

#----binance coin display of yearly, monthly, weekly chart, news, comments----#
def getyrbinancechart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM yearlyprofit WHERE Name like 'binance-coin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getwkbinancechart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM weeklyprofit WHERE Name like 'binance-coin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getmbinancechart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM monthlyprofit WHERE Name like 'binance-coin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
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
#----end----#

#----polkadot display of yearly, monthly, weekly chart, news, comments----#
def getyrpolkadotchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM yearlyprofit WHERE Name like 'polkadot' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getwkpolkadotchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM weeklyprofit WHERE Name like 'polkadot' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getmpolkadotchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM monthlyprofit WHERE Name like 'polkadot' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
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
#----end----#

#----xrp display of yearly, monthly, weekly chart, news, comments----#
def getyrxrpchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM yearlyprofit WHERE Name like 'xrp' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getwkxrpchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM weeklyprofit WHERE Name like 'xrp' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getmxrpchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM monthlyprofit WHERE Name like 'xrp' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
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
#----end----#

#----uniswap display of yearly, monthly, weekly chart, news, comments----#
def getyruniswapchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM yearlyprofit WHERE Name like 'uniswap' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getwkuniswapchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM weeklyprofit WHERE Name like 'uniswap' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getmuniswapchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM monthlyprofit WHERE Name like 'uniswap' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
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
#----end----#

#----litecoin display of yearly, monthly, weekly chart, news, comments----#
def getyrlitecoinchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM yearlyprofit WHERE Name like 'litecoin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getwklitecoinchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM weeklyprofit WHERE Name like 'litecoin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getmlitecoinchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM monthlyprofit WHERE Name like 'litecoin' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
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
#----end----#

#----chainlink display of yearly, monthly, weekly chart, news, comments----#
def getyrchainlinkchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM yearlyprofit WHERE Name like 'chainlink' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getwkchainlinkchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM weeklyprofit WHERE Name like 'chainlink' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getmchainlinkchart():
    clabels = []
    cvalues = []

    sql = "SELECT * FROM monthlyprofit WHERE Name like 'chainlink' Order By Date DESC"
    cursor.execute(sql)
    chart = cursor.fetchall()
    try:
        for row in chart:
            fname = row[1]
            fvol = row[3]
            clabels.append(fname)
            cvalues.append(round(fvol, 2))
        clabels.reverse()
        cvalues.reverse()
        return clabels, cvalues
    except:
        print("Error: unable to fetch data")


def getchainlinknews():
    try:
        sql = 'SELECT * FROM googlenewschainlink Order By Time'
        cursor.execute(sql)
        news = cursor.fetchall()
        return news
        mydb.close()
    except:
        print("unable to connect to the chainlink database")
    mydb.close()


def getchainlinkcomment():
    try:
        sql = 'SELECT MIN(comment) AS comment, thumbup, thumbdown, reply FROM yahoocommentchainlink GROUP BY comment Order By thumbup DESC'
        cursor.execute(sql)
        comments = cursor.fetchall()
        return comments
        mydb.close()
    except:
        print("unable to connect to the chainlink database")
    mydb.close()
#----end----#



#----start of dashboard----#
# Yearly
@app.route('/')  # default page
@app.route('/dash')
def dash():
    line_labels, line_values = gettopchart()  # query sql top chart data
    bar_labels, bar_values = getyrdashchart()  # query sql year data
    news = gettopnews()  # query sql news data
    title = "World's"
    title2 = "Top Coin"
    title3 = "1 Year"
    wkbtc = '/wkdash'  # query sql weekly chart data
    monbtc = '/mondash'  # query sql monthly chart data
    yrbtc = '/dash'  # query sql yearly chart data
    return render_template('dash-2.html', title=title, title2=title2, title3=title3, labels=line_labels, values=line_values, news=news, trends=trends, blabels=bar_labels, bvalues=bar_values, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)

# Weekly
@app.route('/wkdash')
def wkdash():
    line_labels, line_values = gettopchart()
    bar_labels, bar_values = getwkdashchart()  # query sql weekly data
    news = gettopnews()
    title = "World's"
    title2 = "Top Coin"
    title3 = "1 Week"
    wkbtc = '/wkdash'
    monbtc = '/mondash'
    yrbtc = '/dash'
    return render_template('dash-2.html', title=title, title2=title2, title3=title3, labels=line_labels, values=line_values, news=news, trends=trends, blabels=bar_labels, bvalues=bar_values, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)

# Monthly
@app.route('/mondash')
def mondash():
    line_labels, line_values = gettopchart()
    bar_labels, bar_values = getmdashchart()  # query sql monthly data
    news = gettopnews()
    title = "World's"
    title2 = "Top Coin"
    title3 = "1 Month"
    wkbtc = '/wkdash'
    monbtc = '/mondash'
    yrbtc = '/dash'
    return render_template('dash-2.html', title=title, title2=title2, title3=title3, labels=line_labels, values=line_values, news=news, trends=trends, blabels=bar_labels, bvalues=bar_values, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)

#----start of bitcoin----#
@app.route('/bitcoin')
def bitcoin():
    line_labels, line_values = getyrbtcchart()  # query sql year data
    news = getbtcnews()
    comments = getbtccomment()
    title = "Bitcoin"
    title2 = "Yearly Data"
    wkbtc = '/wkbitcoin'
    monbtc = '/monbitcoin'
    yrbtc = '/bitcoin'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkbitcoin')
def wkbitcoin():
    line_labels, line_values = getwkbtcchart()  # query sql weekly data
    news = getbtcnews()
    comments = getbtccomment()
    title = "Bitcoin"
    title2 = "Weekly Data"
    wkbtc = '/wkbitcoin'
    monbtc = '/monbitcoin'
    yrbtc = '/bitcoin'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monbitcoin')
def monbitcoin():
    line_labels, line_values = getmbtcchart()  # query sql monthly data
    news = getbtcnews()
    comments = getbtccomment()
    title = "Bitcoin"
    title2 = "Monthly Data"
    wkbtc = '/wkbitcoin'
    monbtc = '/monbitcoin'
    yrbtc = '/bitcoin'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)

#----start of ethereum----#
@app.route('/ethereum')
def ethereum():
    line_labels, line_values = getyrethchart()
    news = getethnews()
    comments = getethcomment()
    title = "Ethereum"
    title2 = "Yearly Data"
    wkbtc = '/wkethereum'
    monbtc = '/monethereum'
    yrbtc = '/ethereum'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkethereum')
def wkethereum():
    line_labels, line_values = getwkethchart()
    news = getethnews()
    comments = getethcomment()
    title = "Ethereum"
    title2 = "Weekly Data"
    wkbtc = '/wkethereum'
    monbtc = '/monethereum'
    yrbtc = '/ethereum'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monethereum')
def monethereum():
    line_labels, line_values = getmethchart()
    news = getethnews()
    comments = getethcomment()
    title = "Ethereum"
    title2 = "Monthly Data"
    wkbtc = '/wkethereum'
    monbtc = '/monethereum'
    yrbtc = '/ethereum'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)

#----start of tether----#
@app.route('/tether')
def tether():
    line_labels, line_values = getyrethchart()
    news = gettetnews()
    comments = gettetcomment()
    title = "Tether"
    title2 = "Yearly Data"
    wkbtc = '/wktether'
    monbtc = '/montether'
    yrbtc = '/tether'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wktether')
def wktether():
    line_labels, line_values = getwkethchart()
    news = gettetnews()
    comments = gettetcomment()
    title = "Tether"
    title2 = "Weekly Data"
    wkbtc = '/wktether'
    monbtc = '/montether'
    yrbtc = '/tether'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/montether')
def montether():
    line_labels, line_values = getmethchart()
    news = gettetnews()
    comments = gettetcomment()
    title = "Tether"
    title2 = "Monthly Data"
    wkbtc = '/wktether'
    monbtc = '/montether'
    yrbtc = '/tether'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)

#----start of cardano----#
@app.route('/cardano')
def cardano():
    line_labels, line_values = getyrcarchart()
    news = getcarnews()
    comments = getcarcomment()
    title = "Cardano"
    title2 = "Yearly Data"
    wkbtc = '/wkcardano'
    monbtc = '/moncardano2'
    yrbtc = '/cardano'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkcardano')
def wkcardano():
    line_labels, line_values = getwkcarchart()
    news = getcarnews()
    comments = getcarcomment()
    title = "Cardano"
    title2 = "Weekly Data"
    wkbtc = '/wkcardano'
    monbtc = '/moncardano2'
    yrbtc = '/cardano'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/moncardano2')
def moncardano2():
    line_labels, line_values = getmcarchart()
    news = getcarnews()
    comments = getcarcomment()
    title = "Cardano"
    title2 = "Monthly Data"
    wkbtc = '/wkcardano'
    monbtc = '/moncardano2'
    yrbtc = '/cardano'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)

#----start of binance----#
@app.route('/binance')
def binance():
    line_labels, line_values = getyrbinancechart()
    news = getbinancenews()
    comments = getbinancecomment()
    title = "Binance Coin"
    title2 = "Yearly Data"
    wkbtc = '/wkbinance'
    monbtc = '/monbinance'
    yrbtc = '/binance'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkbinance')
def wkbinance():
    line_labels, line_values = getwkbinancechart()
    news = getbinancenews()
    comments = getbinancecomment()
    title = "Binance Coin"
    title2 = "Weekly Data"
    wkbtc = '/wkbinance'
    monbtc = '/monbinance'
    yrbtc = '/binance'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monbinance')
def moncardano():
    line_labels, line_values = getmbinancechart()
    news = getbinancenews()
    comments = getbinancecomment()
    title = "Binance Coin"
    title2 = "Monthly Data"
    wkbtc = '/wkbinance'
    monbtc = '/monbinance'
    yrbtc = '/binance'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)

#----start of polkadot----#
@app.route('/polkadot')
def polkadot():
    line_labels, line_values = getyrpolkadotchart()
    news = getpolkadotnews()
    comments = getpolkadotcomment()
    title = "Polkadot"
    title2 = "Yearly Data"
    wkbtc = '/wkpolkadot'
    monbtc = '/monpolkadot'
    yrbtc = '/polkadot'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkpolkadot')
def wkpolkadot():
    line_labels, line_values = getwkpolkadotchart()
    news = getpolkadotnews()
    comments = getpolkadotcomment()
    title = "Polkadot"
    title2 = "Weekly Data"
    wkbtc = '/wkpolkadot'
    monbtc = '/monpolkadot'
    yrbtc = '/polkadot'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monpolkadot')
def monpolkadot():
    line_labels, line_values = getmpolkadotchart()
    news = getpolkadotnews()
    comments = getpolkadotcomment()
    title = "Polkadot"
    title2 = "Monthly Data"
    wkbtc = '/wkpolkadot'
    monbtc = '/monpolkadot'
    yrbtc = '/polkadot'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)

#----start of xrp----#
@app.route('/xrp')
def xrp():
    line_labels, line_values = getyrxrpchart()
    news = getxrpnews()
    comments = getxrpcomment()
    title = "XRP"
    title2 = "Yearly Data"
    wkbtc = '/wkxrp'
    monbtc = '/monxrp'
    yrbtc = '/xrp'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkxrp')
def wkxrp():
    line_labels, line_values = getwkxrpchart()
    news = getxrpnews()
    comments = getxrpcomment()
    title = "XRP"
    title2 = "Weekly Data"
    wkbtc = '/wkxrp'
    monbtc = '/monxrp'
    yrbtc = '/xrp'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monxrp')
def monxrp():
    line_labels, line_values = getmxrpchart()
    news = getpolkadotnews()
    comments = getpolkadotcomment()
    title = "XRP"
    title2 = "Monthly Data"
    wkbtc = '/wkxrp'
    monbtc = '/monxrp'
    yrbtc = '/xrp'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)

#----start of uniswap----#
@app.route('/uniswap')
def uniswap():
    line_labels, line_values = getyruniswapchart()
    news = getuniswapnews()
    comments = getuniswapcomment()
    title = "Uniswap"
    title2 = "Yearly Data"
    wkbtc = '/wkuniswap'
    monbtc = '/monuniswap'
    yrbtc = '/uniswap'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkuniswap')
def wkuniswap():
    line_labels, line_values = getwkuniswapchart()
    news = getuniswapnews()
    comments = getuniswapcomment()
    title = "Uniswap"
    title2 = "Weekly Data"
    wkbtc = '/wkuniswap'
    monbtc = '/monuniswap'
    yrbtc = '/uniswap'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monuniswap')
def monuniswap():
    line_labels, line_values = getmuniswapchart()
    news = getuniswapnews()
    comments = getuniswapcomment()
    title = "Uniswap"
    title2 = "Monthly Data"
    wkbtc = '/wkuniswap'
    monbtc = '/monuniswap'
    yrbtc = '/uniswap'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)

#----start of litecoin----#
@app.route('/litecoin')
def litecoin():
    line_labels, line_values = getyrlitecoinchart()
    news = getlitecoinnews()
    comments = getlitecoincomment()
    title = "Litecoin"
    title2 = "Yearly Data"
    wkbtc = '/wklitecoin'
    monbtc = '/monlitecoin'
    yrbtc = '/litecoin'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wklitecoin')
def wklitecoin():
    line_labels, line_values = getwklitecoinchart()
    news = getlitecoinnews()
    comments = getlitecoincomment()
    title = "Litecoin"
    title2 = "Weekly Data"
    wkbtc = '/wklitecoin'
    monbtc = '/monlitecoin'
    yrbtc = '/litecoin'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monlitecoin')
def monlitecoin():
    line_labels, line_values = getmlitecoinchart()
    news = getlitecoinnews()
    comments = getlitecoincomment()
    title = "Litecoin"
    title2 = "Monthly Data"
    wkbtc = '/wklitecoin'
    monbtc = '/monlitecoin'
    yrbtc = '/litecoin'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)

#----start of chainlink----#
@app.route('/chainlink')
def chainlink():
    line_labels, line_values = getyrchainlinkchart()
    news = getchainlinknews()
    comments = getchainlinkcomment()
    title = "Chainlink"
    title2 = "Yearly Data"
    wkbtc = '/wkchainlink'
    monbtc = '/monchainlink'
    yrbtc = '/chainlink'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/wkchainlink')
def wkchainlink():
    line_labels, line_values = getwkchainlinkchart()
    news = getchainlinknews()
    comments = getchainlinkcomment()
    title = "Chainlink"
    title2 = "Weekly Data"
    wkbtc = '/wkchainlink'
    monbtc = '/monchainlink'
    yrbtc = '/chainlink'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)


@app.route('/monchainlink')
def monchainlink():
    line_labels, line_values = getmlitecoinchart()
    news = getchainlinknews()
    comments = getchainlinkcomment()
    title = "Chainlink"
    title2 = "Monthly Data"
    wkbtc = '/wkchainlink'
    monbtc = '/monchainlink'
    yrbtc = '/chainlink'
    return render_template('index.html', title=title, title2=title2, labels=line_labels, values=line_values, news=news, comments=comments, trends=trends, wkbtc=wkbtc, monbtc=monbtc, yrbtc=yrbtc)
