import requests
from requests.packages import urllib3

url='https://www.12306.cn'

# urllib3.disable_warining()
response=requests.get(url,verify=False)
print(response.status_code)