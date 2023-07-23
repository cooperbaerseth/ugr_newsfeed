import os
import requests
import json

# Read the API key from the text file
newsapi_path = "/Users/sethcooper-baer/Desktop/Desktop/personal_projects/user_guided_news_recommendations/newsapi_key.txt"
with open(newsapi_path, "r") as file:
    os.environ["API_KEY"] = file.read().strip()

newsapi_key = os.environ["API_KEY"]

search_date = '2023-06-23'
page_num = 2
url = ('https://newsapi.org/v2/everything?'
       'q=Inflection AI&'
       f'from={search_date}&'
       'sortBy=popularity&'
       f'page={page_num}&'
       f'apiKey={newsapi_key}')

response = requests.get(url)

print(response.json)

with open(f'newsapi_response_p{page_num}.json', 'w') as f:
    json.dump(response.json(), f)