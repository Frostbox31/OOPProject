from SecondLayer.Utilities import _getrandomheader, commitsqlcommand
import requests
import re
class yahooComment:
      def __init__(user,comment,like,dislike,replies):
          user.comment = comment
          user.like = like
          user.dislike = dislike
          user.replies = replies

def getyahoofinancecomment(coinname,coin):
    count = 30;
    dataset = []
    check = 0
    while len(dataset) < 1000 and check != 1:
        print(coin)
        link = "https://sg.finance.yahoo.com/_finance_doubledown/api/resource/canvass.getMessageList;apiVersion=v1;context=finmb_"+coin+"_CCC;count=30;lang=en-SG;namespace=yahoo_finance;oauthConsumerKey=finance.oauth.client.canvass.prod.consumerKey;oauthConsumerSecret=finance.oauth.client.canvass.prod.consumerSecret;query=namespace%20%3D%20%22yahoo_finance%22%20and%20(contextId%3D%22finmb_"+coin+"_CCC%22%20or%20tag%3D%22"+coin+"-USD%22);"
        request = requests.get(link,headers=_getrandomheader())
        comment = re.findall("userText?.*?tags",str(request.content.decode('utf8').encode('ascii', errors='ignore')))
        like    = re.findall("upVoteCount?.*?,",str(request.content.decode('utf8').encode('ascii', errors='ignore')))
        dislike = re.findall("downVoteCount?.*?,",str(request.content.decode('utf8').encode('ascii', errors='ignore')))
        numberofpeoplereply = re.findall("replyCount?.*?,",str(request.content.decode('utf8').encode('ascii', errors='ignore')))
        nextpage = re.findall("startIndex?.*?,",str(request.content.decode('utf8').encode('ascii', errors='ignore')))

        if(len(comment) == 0):
            check = 1;

        for x in range(len(comment)):
            comment[x] = re.sub('https?.*|"imageMessageDetails?.*','',str(comment[x]).replace("\\n",'').replace("\\",''))
            dataset.insert(len(dataset),yahooComment(str(comment[x])[11:-8],str(like[x]).replace('upVoteCount":','').replace(",",''),str(dislike[x]).replace('downVoteCount":','').replace(",",''),str(numberofpeoplereply[x]).replace('replyCount":','').replace("},",'')))

        link ="https://sg.finance.yahoo.com/_finance_doubledown/api/resource/canvass.getMessageList;apiVersion=v1;context=finmb_"+ coin+ "_CCC;count=30;" + "v%3D" + nextpage[0][15:-32] +  "%3As%3D" + nextpage[0][19:-22] + "%3Asl%3D" + nextpage[0][30:-8] +  "%3Aoff%3D" + str(count) + ";lang=en-SG;namespace=yahoo_finance;oauthConsumerKey=finance.oauth.client.canvass.prod.consumerKey;oauthConsumerSecret=finance.oauth.client.canvass.prod.consumerSecret;query=namespace%20%3D%20%22yahoo_finance%22%20and%20(contextId%3D%22finmb_"+coin+"_CCC%22%20or%20tag%3D%22"+coin+"-USD%22);"
        count += 30

    commitsqlcommand("CREATE Table IF NOT EXISTS yahoocomment" + str(coinname).replace(" ","") + "(id int NOT NULL AUTO_INCREMENT,comment varchar(10000) DEFAULT NULL,thumbup int DEFAULT NULL,thumbdown int DEFAULT NULL,reply int DEFAULT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=1021 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;",'')
    commitsqlcommand("DELETE FROM yahoocomment" + str(coinname).replace(" ",""),'')

    for x in range(len(dataset)):
        commitsqlcommand("INSERT INTO yahoocomment"+ str(coinname).replace(" ","") + " VALUES (%s,%s,%s,%s,%s)",(x+1,str(dataset[x].comment),int(dataset[x].like),int(dataset[x].dislike),int(dataset[x].replies)))



