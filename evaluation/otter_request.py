import requests
import json
import base64
from io import BytesIO
from PIL import Image
def encode_image_to_base64(image_path):
    # 打开图像
    with Image.open(image_path) as img:
        # 调整图像大小为224x224
        img_resized = img.resize((224, 224))

        # 保存调整大小的图像到一个字节缓冲区
        buffered = BytesIO()
        img_resized.save(buffered, format="JPEG")

        # 将字节缓冲区内容转换为Base64
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        image_file=image_file.resize((224,224))
        return base64.b64encode(image_file.read()).decode('utf-8')

def code_llamarequest(content,image_list):
    url = "http://172.21.25.95:5441/app/otter"
    headers = {
        "Content-Type": "application/json"
    }
    data_payload = {
        "content": [
            {
                "prompt": content,
            }
        ],
        "token": "sk-ICLRBESTPAPERAWARDOCTOPUS"
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data_payload))
    print(response.text)
    return response.text

def otter_request(content, image_list):
    # Define the URL and headers
    url = "http://172.21.25.95:5441/app/otter"
    headers = {
        "Content-Type": "application/json"
    }
    data_payload = {
        "content": [
            {
                "prompt": content,
                "images": {
                    'image0': encode_image_to_base64(image_list[0]),
                    'image1': encode_image_to_base64(image_list[1]),
                    'image2': encode_image_to_base64(image_list[2]),
                    'image3': encode_image_to_base64(image_list[3]),
                    'image4': encode_image_to_base64(image_list[4]),
                    'image5': encode_image_to_base64(image_list[5]),
                    'image6': encode_image_to_base64(image_list[6]),
                    'image7': encode_image_to_base64(image_list[7]),
                    'image8': encode_image_to_base64(image_list[8]),
                    'image9': encode_image_to_base64(image_list[9]),
                    }
            }
        ],
        "token": "sk-ICLRBESTPAPERAWARDOCTOPUS"
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data_payload))
    print(response.text)
    return response.text

if __name__ == "__main__":
    content = ''
    image_list=[]
    for i in range(8):
        image_list.append(f"/shared/liushuai/OmniGibson/prompt_files/data/cook_bacon/subtask_1/rgb{i}_detect_surroundings.png")
    otter_request(content='1',image_list=image_list)