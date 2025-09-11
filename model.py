import requests
import json

url = "http://localhost:12434/engines/llama.cpp/v1/chat/completions"

data = {
    "model": "ai/gemma3n:latest",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Please write 500 words about Frank Ocean"
        }
    ]
}

# Disable SSL verification here just for local testing
response = requests.post(url, json=data, verify=False)

print("Status Code:", response.status_code)
print("Response:", response.text)
