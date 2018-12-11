import requests

url='http://httpbin.org/post'
files={'file':open('test.png','rb')}

response=requests.post(url,files=files)
print(response.text)