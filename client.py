import requests
import json

url = 'http://127.0.0.1:5000/'

response1 = requests.get(url)
print(response1.text)

payload = {"decimals": [0.1, 0.2, 0.3, 0.4, 0.5]}
response1 = requests.post(url + "edit", json.dumps(payload))
print("for post: ")
print(response1.text)

payload = {"decimals": "shivani"}
response1 = requests.put(url + "update", json.dumps(payload))
print("for put: ")
print(response1.text)


