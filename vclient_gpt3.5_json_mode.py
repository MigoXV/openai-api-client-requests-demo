import requests
import json
import config

host, key = config.get_config()

url = host+"/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {key}"
}

data = {
    "model": "gpt-3.5-turbo-1106",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "使用json来描述某一天的天气"
        }
    ],
    "response_format": {"type": "json_object"}
}

response = requests.post(url=url, headers=headers, data=json.dumps(data))
if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"])
else:
    print("status_code：", response.status_code)
