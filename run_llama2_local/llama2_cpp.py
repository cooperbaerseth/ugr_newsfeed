"""
using llama-cpp-python
"""

# python3 -m llama_cpp.server --model /Users/sethcooper-baer/Desktop/Desktop/personal_projects/llama2/llama_cpp/open-llama-7B-open-instruct.ggmlv3.q4_0.bin --n_gpu_layers 1

# from llama_cpp import Llama

# print("hey")

# llm = Llama(model_path="/Users/sethcooper-baer/Desktop/Desktop/personal_projects/llama2/llama_cpp/llama-2-13b-chat.ggmlv3.q4_0.bin")

# print(llm)


"""
using ctransformers
"""

import time
from ctransformers import AutoModelForCausalLM

llama2_path = "/Users/sethcooper-baer/Desktop/Desktop/personal_projects/llama2/llama_cpp/llama-2-13b-chat.ggmlv3.q4_0.bin"

llm = AutoModelForCausalLM.from_pretrained(llama2_path, model_type='llama')

while(True):
    input_str = input('Enter: ')
    input_token_length = input('Enter length: ')

    if(input_str == 'exit'):
        break

    timeStart = time.time()

    print(llm(input_str, max_new_tokens=int(input_token_length)))

    print("Time taken: ", -timeStart + time.time())