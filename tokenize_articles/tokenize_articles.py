import json
import tiktoken
from transformers import AutoTokenizer

"""
Psuedocode:
    - After saving articles with full text, for each article:
        - for each tokenizer type:
            - tokenize
            - save tokens in json field
            - save num_tokens as json field
    - Plot distributions of number of tokens
"""

conf_path = 'config.json'
with open(conf_path, 'r') as f:
    conf = json.load(f)

# Read the API key from the text file
hugging_face_api_key_path = conf["hugging_face_api_key_path"]
with open(hugging_face_api_key_path, "r") as file:
    hugging_face_api_key = file.read().strip()

# load article data
article_data_path = 'article_data.json'
with open(article_data_path, 'r') as f:
    article_data = json.load(f)

# tiktoken / OpenAI tokenization
tiktoken_tokenizer = tiktoken.encoding_for_model("gpt-4")

# LLaMa-2 tokenization
llama_tokenizer = AutoTokenizer.from_pretrained(conf["hugging_face_model_name"], use_auth_token=hugging_face_api_key)

# count tokens in articles
for query in article_data['article_data']:
    for article in query['articles']:
        article['tiktoken_token_count'] = len(tiktoken_tokenizer.encode(article['text']))
        article['llama_token_count'] = len(llama_tokenizer.encode(article['text']))
        print(f"url: {article['url']}")
        print(f"tiktoken_token_count: {article['tiktoken_token_count']}")
        print(f"llama_token_count: {article['llama_token_count']}\n")

with open(f'article_data.json', 'w') as f:
    json.dump(article_data, f)
