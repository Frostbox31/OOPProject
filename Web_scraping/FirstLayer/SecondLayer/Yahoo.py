from Utilities import _getrandomheader, commitsqlcommand
import requests
import re

class yahooComment:
      def __init__(user,comment,like,dislike,replies):
          user.comment = comment
          user.like = like
          user.dislike = dislike
          user.replies = replies
dataset = []

while len(dataset) < 1000:

    link = "https://sg.finance.yahoo.com/_finance_doubledown/api/resource/canvass.getMessageList;apiVersion=v1;context=finmb_BTC_CCC;count=30;lang=en-SG;namespace=yahoo_finance;oauthConsumerKey=finance.oauth.client.canvass.prod.consumerKey;oauthConsumerSecret=finance.oauth.client.canvass.prod.consumerSecret;query=namespace%20%3D%20%22yahoo_finance%22%20and%20(contextId%3D%22finmb_BTC_CCC%22%20or%20tag%3D%22BTC-USD%22);"

    request = requests.get(link,headers=_getrandomheader())
    comment = re.findall("userText?.*?tags",str(request.content))
    like    = re.findall("upVoteCount?.*?,",str(request.content))
    dislike = re.findall("downVoteCount?.*?,",str(request.content))
    numberofpeoplereply = re.findall("replyCount?.*?,",str(request.content))
    nextpage = re.findall("startIndex?.*?,",str(request.content))

    for x in range(len(comment)):
        dataset.insert(len(dataset),yahooComment(comment[x][11:-5],str(like[x]).replace('upVoteCount":','').replace(",",''),str(dislike[x]).replace('downVoteCount":','').replace(",",''),str(numberofpeoplereply[x]).replace('replyCount":','').replace("},",'')))


    count = 30;
    link ="https://sg.finance.yahoo.com/_finance_doubledown/api/resource/canvass.getMessageList;apiVersion=v1;context=finmb_BTC_CCC;count=30;" + "v%3D" + nextpage[0][15:-32] +  "%3As%3D" + nextpage[0][19:-22] + "%3Asl%3D" + nextpage[0][30:-8] +  "%3Aoff%3D" + nextpage[0][45:-2] + ";lang=en-SG;namespace=yahoo_finance;oauthConsumerKey=finance.oauth.client.canvass.prod.consumerKey;oauthConsumerSecret=finance.oauth.client.canvass.prod.consumerSecret;query=namespace%20%3D%20%22yahoo_finance%22%20and%20(contextId%3D%22finmb_BTC_CCC%22%20or%20tag%3D%22BTC-USD%22);"


for x in range(len(dataset)):
    #commitsqlcommand("INSERT INTO yahoocomment (id,comment,like,dislike,replies) VALUES (%s,%s,%s,%s,%s)",(x+1,str(dataset[x].comment),int(dataset[x].like),int(dataset[x].dislike),int(dataset[x].replies)))
    commitsqlcommand('INSERT INTO yahoocomment (Id,Comment,Like,Dislike,Replies) VALUES (%s,%s,%s,%s,%s)',(x+1,"",0,0,0))
    #print(dataset[x].like)
