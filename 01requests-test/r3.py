import requests
import json

r=requests.get("http://httpbin.org/get")
print(r.status_code)
print(type(r.text))
print(r.json())
print(type(r.json()))
print(json.loads(r.text))
print(r.content)