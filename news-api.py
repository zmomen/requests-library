import requests
import json

with open("config.json", "r") as jsonfile:
	data = json.load(jsonfile)
	top_url = data['NEWS_API_URL']

resp = requests.get(top_url).json()

articles = resp['articles']
for article in articles:
    # print(article.keys())
    print("source: {}\ntitle: {}\npublished: {}\n".format(article['source']['name']
                                                          , article['title']
                                                          , article['publishedAt']))
