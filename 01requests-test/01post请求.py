import requests

url='http://httpbin.org/post'
data={
    'name':'Jack',
    'age':28
}

response=requests.post(url,data=data)
print(response.text)