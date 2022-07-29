import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Version/15.5 Safari/605.1.15 '
}
url = 'https://www.sogou.com/web'
keyword = '高考'
param = {
    'query': keyword
}
response = requests.get(url, params=param,headers=headers)
page_text = response.text
fileName = keyword + '.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)