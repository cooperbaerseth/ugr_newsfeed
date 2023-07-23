import os
import requests
import json

"""
Psuedocode:
    - Call newsapi with 5 different article requests, parsed from article_queries.json
    - Each call will have a different keyword tag
    - Take URLs from top 3 pages of each query (300 artciles each, total of 1500 article URLs)
    - For each article URL, call newspaper and take the raw text from the article. Save the following structure:
        - newsapi fields: source_name, author, title, description, url
        - newspaper field: full_text
        - misc: newsapi_related_query
    - After saving articles with full text, for each article:
        - for each tokenizer type:
            - tokenize
            - save tokens in json field
            - save num_tokens as json field
    - Plot distributions of number of tokens
"""

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