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
tokens = tiktoken_tokenizer.encode("string to encode")
print(len(tokens))

# LLaMa-2 tokenization
llama_tokenizer = AutoTokenizer.from_pretrained(conf["hugging_face_model_name"], use_auth_token=hugging_face_api_key)
tokens = llama_tokenizer.encode("string to encode")
print(len(tokens))