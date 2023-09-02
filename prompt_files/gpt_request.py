import requests
import json


def gpt_request(content=None):
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
                "content": content
            }
        ],
        "model": "CHAT_GPT_4_32K",
        "token": "sk-73dedelSgNkMqhiOaS63pie8hnTqt2LkICsN3VrwNCjPID0A"
    }

    # Make the POST request
    while True:
        response = requests.post(url, headers=headers, json=data)

        response = response.json()
        
        if 'status' in response.keys():
            print('retry')
            continue
        if 'code' in response.keys():
            break

    ### this is what we need
    repsonse_content = response["data"]["0"]["message"]["content"]
    print(repsonse_content)
    # Check the response
    if response["code"] == 200:
        print("Success")
    else:
        print("Failed", response.content)
    
    return repsonse_content

gpt_request("Hello, I'm dongyuhao")