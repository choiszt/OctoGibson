import requests
import json

# Endpoint URL
url = 'https://2077ai.com/ai-hub-api/app/chat-gpt'

# Headers
headers = {
    'Content-Type': 'application/json'
}

# Data payload
data = {
    "content": [
        {
            "role": "user",
            "content": "Hello! I am Jack."
        },
        {
            "role": "assistant",
            "content": "Hello Jack! I am XiaoDuXiaoDu. How can I assist you today?"
        },
        {
            "role": "user",
            "content": "How to spell you name?"
        }
    ],
    "model": "CHAT_GPT_4_32K",
    "token": "sk-73dedelSgNkMqhiOaS63pie8hnTqt2LkICsN3VrwNCjPID0A"
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

response = response.json()

### this is what we need
content = response["data"]["0"]["message"]["content"]
# Check the response
if response.status_code == 200:
    print("Success:", json.dumps(response.json(), indent=4))
else:
    print("Failed:", response.content)