from dotenv import load_dotenv
import os
import requests
import json

def chat_bot(prompt:str):
    load_dotenv("./")
    API_KEY : str = os.getenv("OPEN_ROUTER_API_KEY")
    MODEL : str = "deepseek/deepseek-r1-0528:free"
    BASE_URL : str = "https://openrouter.ai/api/v1"
    authorization_value : str = "Bearer "+API_KEY
    request : dict =  requests.post(
        url=BASE_URL+"/chat/completions",
        headers={
            "Authorization":authorization_value
        },
        data=json.dumps(
            {
                "model":MODEL,
                "messages":[
                    {
                        "role":"user",
                        "content":prompt
                    }
                ]
            }
        )
    )
    response : dict = request.json()
    return response["choices"][0]["message"]["content"]