import requests
import json
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def otter_request(content, image_list):
    # Define the URL and headers
    url = "http://214.2.254.234:5002/app/otter"
    headers = {
        "Content-Type": "application/json"
    }

    data_payload = {
        "content": [
            {
                "prompt": content,
                "images": {
                    'image0': image_to_base64(image_list[0]),
                    'image1': image_to_base64(image_list[1]),
                    'image2': image_to_base64(image_list[2]),
                    'image3': image_to_base64(image_list[3]),
                    }
            }
        ],
        "token": "sk-ICLRBESTPAPERAWARDOCTOPUS"
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data_payload))
    print(response.text)
    return response.text["result"]

if __name__ == "__main__":
    content = ''
    image_list = []
    otter_request()