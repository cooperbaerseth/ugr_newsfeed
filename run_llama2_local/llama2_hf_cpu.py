import time
import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

conf_path = 'config.json'
with open(conf_path, 'r') as f:
    conf = json.load(f)

# Read the API key from the text file
hugging_face_api_key_path = conf["hugging_face_api_key_path"]
with open(hugging_face_api_key_path, "r") as file:
    hugging_face_api_key = file.read().strip()

timeStart = time.time()

tokenizer = AutoTokenizer.from_pretrained(
    conf["hugging_face_model_name"], 
    use_auth_token=hugging_face_api_key
)

model = AutoModelForCausalLM.from_pretrained(
    conf["hugging_face_model_name"],
    use_auth_token=hugging_face_api_key,
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True
)

print("Load model time: ", -timeStart + time.time())

while(True):
    input_str = input('Enter: ')
    input_token_length = input('Enter length: ')

    if(input_str == 'exit'):
        break

    timeStart = time.time()

    inputs = tokenizer.encode(
        input_str,
        return_tensors="pt"
    )

    outputs = model.generate(
        inputs,
        max_new_tokens=int(input_token_length),
    )

    output_str = tokenizer.decode(outputs[0])

    print(output_str)

    print("Time taken: ", -timeStart + time.time())
