import requests
import json

url = "http://127.0.0.1:8000/message/"

# content message
payload = json.dumps({
  "sender": "Ami",
  "receiver": "Afek",
  "message": "temp",
  "subject": "temp"
})
headers = {
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
