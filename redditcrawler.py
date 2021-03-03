import requests
from bs4 import BeautifulSoup
import mysql.connector
import sys
import re


#each time will return six commentlinks

link2 = []
output2 = []

def request_comment_link():
  reddit_subtitle = ['hot','new','top','rising']

  output = []
  link = []
  id = ''
  counter = 1
  count = 0
  
  while count < counter :
    while len(output) == 0 :

      page = requests.get('https://www.reddit.com/r/CryptoCurrency/'+ reddit_subtitle[0]+ '/?after=' + id,headers={'content-type':'text/plain'})

      soup = BeautifulSoup(page.content, 'html.parser')

      for match in soup.find_all(attrs={"data-click-id": 'comments'}): # Comment Link
          if match['href'] not in output:
              output.insert(0,'reddit.com' + match['href'][:-1])
              if len(output) == 6:
                id = 't3_' + match['href'].split("/")[4] 
                check = 1 
      
      for x in range(len(output)):       # Print List 
          link.insert(0,output[x])
    pass
    count += 1
    output = []
  pass

 # for x in range(len(link)):       
  #    print(link[x])
  return link



link2 = request_comment_link()
output2 = []
match = []

for x in range(len(link2)):       
    print(link2[x])

      
request = requests.get('https://www.' + link2[0] + '.json', headers={'User-agent': 'Super Bot Power Level Over 9000'})

#match = re.findall(r'\/r\/\w+\W?\w+\W?\w+\W?\w+\W?\w+\/',request.text) 

match = re.findall("^""body: """,request.text) 
#([A-Z].*?[\.!?])
#"body": "Exactly, I almost gave up this weekend, I just got tired of wading through them all. I want good info without meme mountain lol."
for x in range(len(match)):
    print(match[x])
      #output2.insert(0,request)


for x in range(len(output2)):       
    print("a" + output2[x])         

#with open('filename.txt', 'w') as f:
#    print(comment, file=f)

