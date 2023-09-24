import requests
import json
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def otter_request(content, image_list):
    # Define the URL and headers
    url = "http://172.21.25.95:5432/app/otter"
    headers = {
        "Content-Type": "application/json"
    }
    data_payload = {
        "content": [
            {
                "prompt": "Inventory: None\nTask Goal: installing_a_fax_machine\nOriginal Subtasks: None\nPrevious Action Code: No code\nExecution error: No error\nNow, please output Explain, Subtasks (revise if necessary), Code that completing the next subtask, and Target States, according to the instruction above. Remember you can only use the functions provided above and pay attention to the response format.",
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
    image_list=[]
    for i in range(4):
        image_list.append(f"/shared/liushuai/OmniGibson/prompt_files/data/cook_bacon/subtask_1/rgb{i}_detect_surroundings.png")
    otter_request(content='1',image_list=image_list)