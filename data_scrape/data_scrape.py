import random
import time
from school_info import *

default_school_name = '西安交通大学'
default_province_name = '陕西'
default_province_collection = 'province_score'


class DataScrape:
    def __init__(self, school_name=default_school_name, province_name=default_province_name):
        self.school_name = school_name
        self.province_name = province_name
        id_query = DataStorage()
        self.school_id, self.province_id = id_query.school_province_id_query(school_name)
        self.data_storage = DataStorage()

    def province_score_scrape(self):
        province_score = JsonAnalysis(self.school_name)
        province_response = province_score.analysis(subject_name='province')
        years = province_response.get('data').get('newsdata').get('year')[self.province_id]
        for year in years:
            key = '{}_{}'.format(self.province_id, year)
            subjects = province_response.get('data').get('newsdata').get('type')[key]
            for subject in subjects:
                base_url = 'https://static-data.gaokao.cn/www/2.0/schoolprovinceindex/{year}/{school_id}/{province_id}/{subjects}/1.json'
                url = base_url.format(year=str(year), school_id=self.school_id, province_id=self.province_id, subjects=subject)
                time.sleep(random.randint(7, 20))
                province_crawler = CeeCrawler(url)
                province_data = province_crawler.get_response()
                self.data_storage.store(province_data.get('data').get('item'), collection_name=default_province_collection)




