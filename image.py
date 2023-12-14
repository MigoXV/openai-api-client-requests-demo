# from openai import OpenAI
import json
import requests
import config

host, key = config.get_config()

url = host+"/v1/images/generations"

heardes = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {key}"
}

data = {
    "model": "dall-e-3",
    "prompt": "可爱的戴帽子的小黑猫进食照片",
    "n": 1,
    "size": "1024x1024"
}

response = requests.post(url=url,
                         headers=heardes,
                         data=json.dumps(data))

if response.status_code == 200:
    if "error" in response.json():
        print(response.json()["error"]["message"])
    else:
        print(response.json()["data"][0]["url"])
else:
    print("status_code：",response.status_code)
