import requests

r = requests.get(
    'http://192.168.56.74:1120/message/queryMessageByTopic.query?begin=1535958000000&end=1535962560000&topic=order1')

print(r.json())


def get_json(json):
    if json:
        items = json.get('data')
        for item in items:
            orderId = item.get('properties').get('KEYS')
            print('orderId:', orderId)
            with open('mo_mible.txt', 'a+', encoding='utf8') as f:
                f.write('orderId:' + orderId+'\n')
    f.close()


get_json(r.json())
