from SecondLayer.Utilities import _getRandomHeader, _commitSQLCommand
import requests
import re
class yahooComment:
      def __init__(user,comment,like,dislike,replies):
          user.comment = comment
          user.like = like
          user.dislike = dislike
          user.replies = replies

def _getYahooFinanceComment(coinname,coin,numberofcomment): #Get Cryptocurrency people comment from Yahoo Finance
    
    numberoftimes = numberofcomment / 30
    count = 30;
    dataset = []
    check = 0
    counter = 0
    link = "https://sg.finance.yahoo.com/_finance_doubledown/api/resource/canvass.getMessageList;apiVersion=v1;context=finmb_"+coin+"_CCC;count=30;lang=en-SG;namespace=yahoo_finance;oauthConsumerKey=finance.oauth.client.canvass.prod.consumerKey;oauthConsumerSecret=finance.oauth.client.canvass.prod.consumerSecret;query=namespace%20%3D%20%22yahoo_finance%22%20and%20(contextId%3D%22finmb_"+coin+"_CCC%22%20or%20tag%3D%22"+coin+"-USD%22);"

    while counter < numberoftimes and check != 1: #Change the number to get the desired number of comments
        request = requests.get(link,headers=_getRandomHeader())

        #Find the specified sentence/number/word by using regex expressions
        comment = re.findall("userText?.*?tags",str(request.content.decode('utf8').encode('ascii', errors='ignore')))
        like    = re.findall("upVoteCount?.*?,",str(request.content.decode('utf8').encode('ascii', errors='ignore')))
        dislike = re.findall("downVoteCount?.*?,",str(request.content.decode('utf8').encode('ascii', errors='ignore')))
        reply = re.findall("replyCount?.*?,",str(request.content.decode('utf8').encode('ascii', errors='ignore')))
        nextpage = re.findall("startIndex?.*?,",str(request.content.decode('utf8').encode('ascii', errors='ignore')))

        if(len(comment) == 0): #Check if it does return any feedback else end the loop
           check = 1;

        for x in range(len(comment)):
            comment[x] = re.sub('https?.*|"imageMessageDetails?.*','',str(comment[x]).replace("\\n",'').replace("\\",'')) #Fliter the sentence/number or word
            if comment[x] != 'userText":"' and comment[x] != 'userText":"",':
                dataset.insert(len(dataset),yahooComment(str(comment[x])[11:-8],str(like[x]).replace('upVoteCount":','').replace(",",''),str(dislike[x]).replace('downVoteCount":','').replace(",",''),str(reply[x]).replace('replyCount":','').replace("},",'')))
        
        if len(nextpage) !=  0:
            link ="https://sg.finance.yahoo.com/_finance_doubledown/api/resource/canvass.getMessageList;apiVersion=v1;context=finmb_"+ coin+ "_CCC;count=30;" + "index=v%3D" + nextpage[0][15:-32] +  "%3As%3D" + nextpage[0][19:-22] + "%3Asl%3D" + nextpage[0][30:-8] +  "%3Aoff%3D" + str(count) + ";lang=en-SG;namespace=yahoo_finance;oauthConsumerKey=finance.oauth.client.canvass.prod.consumerKey;oauthConsumerSecret=finance.oauth.client.canvass.prod.consumerSecret;query=namespace%20%3D%20%22yahoo_finance%22%20and%20(contextId%3D%22finmb_"+coin+"_CCC%22%20or%20tag%3D%22"+coin+"-USD%22);"
        count += 30
        counter += 1
    pass

    _commitSQLCommand("CREATE Table IF NOT EXISTS yahoocomment" + str(coinname).replace(" ","") + "(id int NOT NULL AUTO_INCREMENT,comment varchar(10000) DEFAULT NULL,thumbup int DEFAULT NULL,thumbdown int DEFAULT NULL,reply int DEFAULT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=1021 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;",'')
    _commitSQLCommand("DELETE FROM yahoocomment" + str(coinname).replace(" ",""),'')

    for x in range(len(dataset)):
        _commitSQLCommand("INSERT INTO yahoocomment"+ str(coinname).replace(" ","") + " VALUES (%s,%s,%s,%s,%s)",(x+1,dataset[x].comment,dataset[x].like,dataset[x].dislike,dataset[x].replies))

    if len(dataset) == 0:
        _commitSQLCommand("INSERT INTO yahoocomment"+ str(coinname).replace(" ","") + " VALUES (%s,%s,%s,%s,%s)",(1,"No Data",0,0,0))



