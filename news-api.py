import requests

top_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=16eabca179494fa391757fa32d70a9cd'

resp = requests.get(top_url).json()

articles = resp['articles']
for article in articles:
    # print(article.keys())
    print("source: {}\ntitle: {}\npublished: {}\n".format(article['source']['name']
                                                          , article['title']
                                                          , article['publishedAt']))
