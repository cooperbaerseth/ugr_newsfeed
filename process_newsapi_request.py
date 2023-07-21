import json
from newspaper import Article

with open('newsapi_response.json', 'r') as f:
    data = json.load(f)

# Process the loaded JSON data
print(f"Getting text from {data['articles'][0]['url']}")
article = Article(data['articles'][0]['url'])
article.download()
article.parse()
print(article.text)
