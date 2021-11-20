import requests
import json

url = "http://127.0.0.1:8000/message/"


payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)


data = json.loads(response.text.encode('utf8'))
final_dict = {}

final_dict['people'] = data
print(final_dict)


with open("api_message.json", "w") as file:
    json.dump(final_dict, file, indent=2)




