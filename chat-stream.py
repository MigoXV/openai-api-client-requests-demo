import requests
import json
import config

host, key = config.get_config()

url = host+"/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sess-233"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "帮我写一篇记叙文，不少于100字"
        }
    ],
    "stream": True
}

response = requests.post(url=url, headers=headers,
                         data=json.dumps(data), stream=True)

# 检查响应状态
if response.status_code == 200:
    # 逐块处理返回的数据
    for chunk in response.iter_lines():
        # # 对于每个块，您可以进行解析或其它处理
        # print(chunk.decode('utf-8'))
        if chunk.decode("utf-8").startswith('data: '):  # 确保只处理以 'data: ' 开头的部分
            json_data = chunk.decode("utf-8")[6:]  # 去除 'data: '
            try:
                if json_data != "[DONE]":
                    # 将 JSON 字符串解析为字典
                    if 'content' in json.loads(json_data)["choices"][0]["delta"]:
                        print(json.loads(json_data)[
                              "choices"][0]["delta"]['content'], end='')
            except json.JSONDecodeError:
                print("解析错误:", json_data)
else:
    print("Error:", response.status_code)
