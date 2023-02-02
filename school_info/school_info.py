"""
Analysis of the provincescore, specialplan and specialscore json file
"""
from setup_crawler import *
from data_storage import *
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')
BASE_URL = "https://static-data.gaokao.cn/www/2.0/school/{school_id}/dic/{subject}.json"


class JsonAnalysis:
    def __init__(self, school_name):
        self.school_name = school_name
        id_query = DataStorage()
        self.school_id = id_query.school_province_id_query(school_name)

    def analysis(self, subject_name):
        subject_dic = {'province': 'provincescore', 'plan': 'specialplan', 'score': 'specialscore'}
        url = BASE_URL.format(school_id=self.school_id, subject=subject_dic[subject_name])
        crawler = CeeCrawler(url)
        response = crawler.get_response()
        if response is None:
            return False
        if response.get('message') == '\u6210\u529f':
            logging.info('scraping %s with status code %s', subject_dic[subject_name], response.get('message'))
            return response
        else:
            logging.info('anomaly status code %s', response.get('message'))
