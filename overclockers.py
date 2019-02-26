import requests
import re
from textblob import TextBlob
from bs4 import BeautifulSoup

pos = []
neu = []
neg = []

for i in range(1,16):

    #the expanse. use range 16
    url = "https://forums.overclockers.co.uk/threads/the-expanse-please-use-spoiler-tags-for-reveals-with-tv-show-or-books.18703876/page-"
    #the x-files. use range 6
    #url = "https://forums.overclockers.co.uk/threads/the-x-files-season-10.18714980/page-"
    #the walking dead use range 53
    #url = "https://forums.overclockers.co.uk/threads/the-walking-dead-season-7-contains-spoilers-no-future-content-to-be-discussed.18752668/page-"
    #colony use range 3
    #url = "https://forums.overclockers.co.uk/threads/new-series-colony.18697834/page-"
    #dark matter use range 12
    #url = "https://forums.overclockers.co.uk/threads/dark-matter-may-contain-spoilers.18676285/page-"
    
    page = requests.get(url+str(i))

    soup = BeautifulSoup(page.content, 'html.parser')

    ##responses = []
    ##for res in soup.find_all('blockquote'):
    ##    responses.append(res)

    #print(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) \
    #                                    |(\w+:\/\/\S+)", " ", str(responses[0])))
    #print(soup.prettify())
    # print([type(i) for i in (soup.children)])
    html = list(soup.children)[2]
    body = list(html.children)[3]

    for i in body.find_all('blockquote'):
        quote = i.get_text()
        analysis = TextBlob(quote)
        
        if analysis.sentiment.polarity > 0:
            pos.append(quote)
        elif analysis.sentiment.polarity == 0:
            neu.append(quote)
        else:
            neg.append(quote)

total = len(pos) + len(neu) + len(neg)
print('Total Posts:', total)
print('Positive Posts: ', len(pos),' Percentage: ', (len(pos)/total)*100, '%', sep='')
print('Neutral Posts: ', len(neu),' Percentage: ', (len(neu)/total)*100, '%', sep='')
print('Negative Posts: ', len(neg),' Percentage: ', (len(neg)/total)*100, '%', sep='')

print('Sample positive post:', pos[-1].encode('utf-8'))
print('Sample neutral post:', neu[-1].encode('utf-8'))
print('Sample negative post:', neg[-1].encode('utf-8'))
