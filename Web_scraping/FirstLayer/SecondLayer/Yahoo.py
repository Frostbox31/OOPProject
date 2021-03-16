import requests
import random
from Utilities import  _getrandomproxy,_writefile,_getrandomheader
import re

link = "https://sg.finance.yahoo.com/_finance_doubledown/api/resource/canvass.getMessageList;apiVersion=v1;context=finmb_BTC_CCC;count=30;index=v%3D1%3As%3Dpopular%3Asl%3D1615823461%3Aoff%3D00;lang=en-SG;namespace=yahoo_finance;oauthConsumerKey=finance.oauth.client.canvass.prod.consumerKey;oauthConsumerSecret=finance.oauth.client.canvass.prod.consumerSecret;query=namespace%20%3D%20%22yahoo_finance%22%20and%20(contextId%3D%22finmb_BTC_CCC%22%20or%20tag%3D%22BTC-USD%22);"

#https://regex101.com/r/8vWSuG/1/

#proxy_list = _getrandomproxy();

request = requests.get(link,headers=_getrandomheader())

comment = []
like = []
dislike = []

#_writefile(request.content)

match = re.findall(r'^userText\S+|\s|\S+.}$',str(request.content))
print(match) 
    
    #comment.insert(len(comment),str(match.text).encode('UTF-8'))

#for match in soup.find_all(class_="D(ib) Va(m) Fz(12px) Mstart(6px) C(#828c93)"):
#    count = 0;
#    if count % 2 == 0:
#        like.insert(len(like),match.text)
#    else :
#        dislike.insert(len(dislike),match.text)

#for x in range(len(comment)):
#    print(str(comment[x]))

#for x in range(len(like)):
#    print(like[x])

#for x in range(len(dislike)):
#    print(dislike[x])

    