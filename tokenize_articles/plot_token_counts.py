import json
import numpy as np
import matplotlib.pyplot as plt

# load article data
article_data_path = 'article_data.json'
with open(article_data_path, 'r') as f:
    article_data = json.load(f)

tiktoken_counts = []
llama_token_counts = []
for query in article_data['article_data']:
    for article in query['articles']:
        tiktoken_counts.append(article['tiktoken_token_count'])
        llama_token_counts.append(article['llama_token_count'])

print(tiktoken_counts)
print(len(tiktoken_counts))
print(llama_token_counts)
print(len(llama_token_counts))

# plot token counts
plt.hist(tiktoken_counts, bins=50, alpha=0.5, label='Tiktoken Counts')
n, bins, patches = plt.hist(llama_token_counts, bins=50, alpha=0.5, label='Llama Counts')

# Adding labels and legend
plt.xlabel('Value')
plt.ylabel('Frequency')
x_ticks = list(np.linspace(bins[0], bins[-1], num=10))
plt.xticks(x_ticks, [f'{int(tick):.1f}' for tick in x_ticks])
plt.legend()

# Displaying the plot
plt.show()