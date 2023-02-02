from main_crawler import *

num = 0
crawler = Crawler()
while crawler.plan_crawler():
    num += 1
    if num % 100 == 0:
        time.sleep(300)
