import requests
import re
from textblob import TextBlob
from bs4 import BeautifulSoup

pos = []
neu = []
neg = []

##dig spy
for i in range(1,3):
    # the expanse use range 3
    url = "https://forums.digitalspy.com/discussion/2194231/the-expanse/p"
    #colony use range 7
    # url = "https://forums.digitalspy.com/discussion/2145023/colony-uk-pace/p"
    #the x-files use range 17
    #url = "https://forums.digitalspy.com/discussion/2128266/the-x-files-ch5-uk-pace/p"
    #the walking dead use range 91
    #url = "https://forums.digitalspy.com/discussion/2167431/the-walking-dead-season-7-us-sunday-uk-monday-spoilers/p"
    #dark matter use range 15
    #url = "https://forums.digitalspy.com/discussion/2082076/new-series-dark-matter-uk-pace/p"

    page = requests.get(url+str(i))

    soup = BeautifulSoup(page.content, 'html.parser')

    for i in soup.find_all('div', class_="Message"):
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


if len(pos) > 0:
    print('Sample positive post:', pos[-1].encode('utf-8'))
if len(neu) > 0:
    print('Sample neutral post:', neu[-1].encode('utf-8'))
if len(neg) > 0:
    print('Sample negative post:', neg[-1].encode('utf-8'))
