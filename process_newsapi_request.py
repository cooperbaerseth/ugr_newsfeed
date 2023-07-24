import json
from newspaper import Article

data_path = 'newsapi_response_p1.json'
# data_path = 'newsapi_response_p2.json'
with open(data_path, 'r') as f:
    data = json.load(f)

# Process the loaded JSON data
print(f"data['totalResults']: {data['totalResults']}")
print(f"len(data['articles']): {len(data['articles'])}")
print(f"Getting text from {data['articles'][0]['url']}")
article = Article(data['articles'][0]['url'])
article.download()
article.parse()
print(article.text)
