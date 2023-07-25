import os
import requests
import json
from newspaper.article import ArticleException
from newspaper import Article
from newspaper import Config

config = Config()
config.browser_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

"""
Psuedocode:
    - Call newsapi with 5 different article requests, parsed from article_queries.json
    - Each call will have a different keyword tag
    - Take URLs from top 3 pages of each query (300 artciles each, total of 1500 article URLs)
    - For each article URL, call newspaper and take the raw text from the article. Save the following structure:
        - newsapi fields: source_name, author, title, description, url
        - newspaper field: full_text
        - misc: newsapi_related_query
"""

def get_articles_info_from_query(query, num_articles, api_key):
    """
        Take a query, which defines the article topic we're searching for and other parameters, and return a json with
        the following fields per article:
            source_name, author, title, description, url, text
        
        Returns a json:
            {[
                "query": {
                    "get_url":,
                    "q":,
                    "from":,
                    "sort_by":
                },
                "articles": [{
                        "source_name":,
                        "author":,
                        "title":,
                        "description":,
                        "url":,
                        "text":
                    },
                    ...
                    ]
            },
            ...
            ]}
    """

    total_articles = 0
    page_num = 1
    total_results = float('inf')
    while total_articles < num_articles and total_articles < total_results:
        url = (f'{query["get_url"]}'
            f'q={query["q"]}&'
            f'from={query["from"]}&'
            f'sortBy={query["sort_by"]}&'
            f'page={page_num}&'
            f'apiKey={api_key}')
        response = requests.get(url).json()

        if response["status"] != "ok":
            with open(f'error_response.json', 'w') as f:
                json.dump(response, f)
            raise Exception(f"newsapi call returned an error\n call: {url}")

        total_results = response["totalResults"]
        query_ariticles = []
        for a in response["articles"]:
            try:
                article = Article(a["url"])
                article.download()
                article.parse()
                query_ariticles.append(
                    {
                        "source_name": a["source"]["name"],
                        "author": a["author"],
                        "title": a["title"],
                        "description": a["description"],
                        "url": a["url"],
                        "text": article.text
                    }
                )
                total_articles += 1
                print(f"total_articles: {total_articles} \n page_num: {page_num}")
                if total_articles >= num_articles or total_articles >= total_results:
                    break
            except ArticleException as e:
                print(f'Got {e}. Skipping url: {a["url"]}')

        page_num += 1
        
    return {
        "query": query,
        "articles": query_ariticles
        }

# load config files
query_path = 'article_queries.json'
with open(query_path, 'r') as f:
    qs = json.load(f)

conf_path = 'config.json'
with open(conf_path, 'r') as f:
    conf = json.load(f)

# Read the API key from the text file
newsapi_path = conf["news_api_key_path"]
with open(newsapi_path, "r") as file:
    os.environ["API_KEY"] = file.read().strip()

newsapi_key = os.environ["API_KEY"]

article_data = []
for q in qs["queries"]:
    data = get_articles_info_from_query(q, conf["articles_per_query"], newsapi_key)
    article_data.append(data)

with open(f'article_data.json', 'w') as f:
    json.dump(json.dumps(article_data), f)