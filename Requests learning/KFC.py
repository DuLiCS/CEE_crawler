import requests
import json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
params = {
    'keyword': '汉中'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Version/15.5 Safari/605.1.15 '
}

response = requests.post(url, params=params, headers=headers)
list_data = response.text
fileName = '汉中' + '.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(list_data)

