import os
import requests
import json

# Read the API key from the text file
with open("newsapi_key.txt", "r") as file:
    os.environ["API_KEY"] = file.read().strip()

newsapi_key = os.environ["API_KEY"]

url = ('https://newsapi.org/v2/everything?'
       'q=Inflection AI&'
       'from=2023-06-18&'
       'sortBy=popularity&'
       f'apiKey={newsapi_key}')

response = requests.get(url)

print(response.json)

with open('newsapi_response.json', 'w') as f:
    json.dump(response.json(), f)