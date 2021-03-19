from SecondLayer.Utilities import _getRandomHeader, _commitSQLCommand
import requests
from bs4 import BeautifulSoup
import re
    

def __subRedditCommentLink(post): # Get all the Sub Link of https://www.reddit.com/r/CryptoCurrency/
  reddit_subtitle = ['hot','new','top','rising']

  output = []
  link = []
  id = '' 
  counter = 0

  while  counter < post: #each time will return six or seven post

    while len(output) == 0 :
      request = requests.get('https://www.reddit.com/r/CryptoCurrency/'+ reddit_subtitle[0]+ '/?after=' + id,headers=_getRandomHeader())
      soup = BeautifulSoup(request.content, 'html.parser')
    
      for match in soup.find_all(attrs={"data-click-id": 'comments'}): # Sub Reddit Comment Link
          if match['href'] not in output:
              output.insert(0,'reddit.com' + match['href'][:-1])
              if len(output) == 6 or len(output) ==7:
                id = 't3_' + match['href'].split("/")[4] 

      for x in range(len(output)):       # Print List 
          link.insert(len(link),output[x])
    pass
    output = []
    counter = counter + 1
  pass
  return link
pass

def __getRedditSubSubComment(post): #Get all the Comment from https://www.reddit.com/r/CryptoCurrency/......./
    link = __subRedditCommentLink(post)
    comments = []

    for x in range(len(link)):       
        request = requests.get('https://www.' + link[x] + '.json',headers=_getRandomHeader())

        subredditcomment = re.findall('"title"?.*?"link_flair_richtext?',request.text)
        subsubredditcomment = re.findall('"body".*?"edited"',request.text) 

        for x in range(len(subredditcomment)):
                comments.insert(len(comments),str(subredditcomment[x].replace('"title": "','').replace('", "link_flair_richtext','').lower()))

        for x in range(len(subsubredditcomment)):
                comments.insert(len(comments),str(subsubredditcomment[x].replace('"body": "','').replace('", "edited"','').lower()))
    
    return comments
pass

def _getRedditCoinOccur(coinsname,coinsshortform,post): #Count the occur of the CryptoCurrency coins

    comments = __getRedditSubSubComment(post)
    _commitSQLCommand("DELETE FROM redditcoinsoccurrence",'')
    for x in range(len(coinsname)):
        coinoccurrence = 0
        for i in range(len(comments)):
            if comments[i].count(str(coinsname[x]).lower()) != 0 or comments[i].count(str(coinsshortform[x]).lower()) != 0:
                coinoccurrence += 1
        _commitSQLCommand("INSERT INTO redditcoinsoccurrence VALUES (%s,%s,%s)",(x+1,coinsname[x],coinoccurrence))
pass

