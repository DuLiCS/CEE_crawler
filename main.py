# This is a sample Python script.
import requests


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                      'Version/15.5 Safari/605.1.15 '
    }
    url = 'https://www.gaokao.cn'
    response = requests.get(url, headers=headers)
    page_text = response.text
    fileName = 'gaokao.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
