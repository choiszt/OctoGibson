#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://gpt4-32k-oai-us-east-2.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "28a2a30822fe4902921e35ae0673df1f"

def gpt_request(content):
    response = openai.ChatCompletion.create(
        engine="finally-have-a-32k-model",
        messages = [{"role":"user","content":content}],
        temperature=0,
        max_tokens=8000,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
    print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']

# repsonse = gpt_request("hi,how are you?")
# print(repsonse['choices'][0]['message']['content'])