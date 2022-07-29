import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Version/15.5 Safari/605.1.15 '
}
post_url = 'https://fanyi.baidu.com/sug'
data = {
    'kw': 'cat'
}
response = requests.post(post_url, data, headers=headers)
dic_obj = response.json()
fp = open('./cat.json', 'w', encoding='utf-8')
json.dump(dic_obj, fp=fp, ensure_ascii=False)

