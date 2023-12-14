import os
import json

def get_config():
    
    # 读取配置文件config.json，没有则创建
    if not os.path.exists("config.json"):

        # 默认url
        host = "https://api.openai.com"

        config = {
            "host": host,
            "key": "your key here",
        }

        with open("config.json", "w") as f:
            json.dump(config, f, indent=4)

    else:
        with open("config.json", "r") as f:
            config = json.load(f)    

    return config["host"], config["key"]
        
if __name__ == "__main__":
    print(get_config())
