import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'
params = {
    'type': '1',
    'interval_id': '100:90',
    'action': '',
    'start': '1',
    'limit': '20'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Version/15.5 Safari/605.1.15 '
}

response = requests.get(url, params=params, headers=headers)
list_data = response.json()
fp = open('./douban.json', 'w', encoding='utf-8')
json.dump(list_data, fp, ensure_ascii=False)