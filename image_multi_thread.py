import json
import requests
import threading
import time
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


def post_in_thread(index):
    print(f"task {index} start")
    response = requests.post(url=url,
                             headers=heardes,
                             data=json.dumps(data))

    if response.status_code == 200:
        if "error" in response.json():
            print(f"task {index} return", response.json()["error"]["message"])
        else:
            print(f"task {index} return", response.json()["data"][0]["url"])
    else:
        print("status_code：", response.status_code)


if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=post_in_thread, args=[i]).start()
        time.sleep(12)
