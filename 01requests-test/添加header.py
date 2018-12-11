import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
r=requests.get('https://www.zhihu.com/',headers=headers)
r.encoding='utf-8'
print(r.text)