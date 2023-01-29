from main_crawler import *

num = 0
crawler = Crawler()
while crawler.score_crawler():
    num += 1
    if num % 100 == 0:
        time.sleep(600)
