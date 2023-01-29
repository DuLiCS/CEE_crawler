import logging
import random
import time
from school_info import *
from crawler_tools import *

default_school_name = '西安交通大学'
default_province_name = '陕西'
default_province_collection = 'province_score'
default_plan_collection = 'plan'
default_score_collection = 'score'


class DataScrape:
    def __init__(self, school_name=default_school_name, province_name=default_province_name):
        self.school_name = school_name
        self.province_name = province_name
        id_query = DataStorage()
        self.school_id = id_query.school_province_id_query(school_name)
        self.province_id = province_id_query(province_name)
        self.data_storage = DataStorage()

    def province_score_scrape(self):
        province_score = JsonAnalysis(self.school_name)
        province_response = province_score.analysis(subject_name='province')
        years = province_response.get('data').get('newsdata').get('year')[self.province_id]
        for year in years:
            key = '{}_{}'.format(self.province_id, year)
            subjects = province_response.get('data').get('newsdata').get('type')[key]
            for subject in subjects:
                base_url = 'https://static-data.gaokao.cn/www/2.0/schoolprovinceindex/{year}/{school_id}/{' \
                           'province_id}/{subjects}/1.json'
                url = base_url.format(year=str(year), school_id=self.school_id, province_id=self.province_id,
                                      subjects=subject)
                time.sleep(random.randint(7, 20))
                province_crawler = CeeCrawler(url)
                province_data = province_crawler.get_response()
                self.data_storage.store(province_data.get('data').get('item'),
                                        collection_name=default_province_collection)

    def special_plan_scrape(self):
        special_plan = JsonAnalysis(self.school_name)
        plan_response = special_plan.analysis(subject_name='plan')
        years = plan_response.get('data').get('newsdata').get('year')[self.province_id]
        for year in years:
            key = '{}_{}'.format(self.province_id, year)
            subjects = plan_response.get('data').get('newsdata').get('type')[key]
            for subject in subjects:
                full_key = '{}_{}_{}'.format(self.province_id, year, subject)
                batches = plan_response.get('data').get('newsdata').get('batch')[full_key]
                for batch in batches:
                    base_url = 'api.eol.cn/web/api/?local_batch_id={batch}&local_province_id={province_id}&local_type_id={subject}' \
                               '&page=1&school_id={school_id}&size=10&special_group=&uri=apidata/api/gkv3/plan/school&year={year}'
                    url = base_url.format(batch=batch, province_id=self.province_id, subject=subject,
                                          school_id=self.school_id, year=year)
                    safe_sign = hash_hmac(url)
                    encrypted_url = 'https://' + url + '&signsafe=' + safe_sign
                    time.sleep(random.randint(10, 21))
                    plan_crawler = CeeCrawler(encrypted_url)
                    plan_data = plan_crawler.get_response()
                    num_found = plan_data.get('data').get('numFound')
                    if num_found == 0:
                        break
                    self.data_storage.store(plan_data.get('data').get('item'), collection_name=default_plan_collection)
                    logging.info('%s %s %s %s', self.school_name, year, batch, subject)
                    if num_found == 10:
                        continue
                    pages = num_found // 10
                    for page in range(2, pages + 2):
                        no_page_url = 'api.eol.cn/web/api/?local_batch_id={batch}&local_province_id={province_id}&local_type_id={subject}' \
                                   '&page={page}&school_id={school_id}&size=10&special_group=&uri=apidata/api/gkv3/plan/school&year={year}'
                        url = no_page_url.format(batch=batch, province_id=self.province_id, subject=subject, page=page, school_id=self.school_id, year=year)
                        safe_sign = hash_hmac(url)
                        encrypted_url = 'https://' + url + '&signsafe=' + safe_sign
                        time.sleep(random.randint(20, 60))
                        plan_crawler = CeeCrawler(encrypted_url)
                        plan_data = plan_crawler.get_response()
                        self.data_storage.store(plan_data.get('data').get('item'), collection_name=default_plan_collection)
                        logging.info('%s %s %s %s page%s', self.school_name, year, batch, subject, page)

    def special_score_scrape(self):
        special_score = JsonAnalysis(self.school_name)
        score_response = special_score.analysis(subject_name='score')
        years = score_response.get('data').get('newsdata').get('year')[self.province_id]
        for year in years:
            key = '{}_{}'.format(self.province_id, year)
            subjects = score_response.get('data').get('newsdata').get('type')[key]
            for subject in subjects:
                full_key = '{}_{}_{}'.format(self.province_id, year, subject)
                batches = score_response.get('data').get('newsdata').get('batch')[full_key]
                for batch in batches:
                    base_url = 'api.eol.cn/web/api/?local_batch_id={batch}&local_province_id={province_id}&local_type_id={subject}' \
                               '&page=1&school_id={school_id}&size=10&special_group=&uri=apidata/api/gk/score/special&year={year}'
                    url = base_url.format(batch=batch, province_id=self.province_id, subject=subject,
                                          school_id=self.school_id, year=year)
                    safe_sign = hash_hmac(url)
                    encrypted_url = 'https://' + url + '&signsafe=' + safe_sign
                    time.sleep(random.randint(10, 31))
                    score_crawler = CeeCrawler(encrypted_url)
                    score_data = score_crawler.get_response()
                    num_found = score_data.get('data').get('numFound')
                    if num_found == 0:
                        break
                    self.data_storage.store(score_data.get('data').get('item'), collection_name=default_score_collection)
                    logging.info('%s %s %s %s', self.school_name, year, batch,subject)
                    if num_found == 10:
                        continue
                    pages = num_found // 10
                    for page in range(2, pages + 2):
                        no_page_url = 'api.eol.cn/web/api/?local_batch_id={batch}&local_province_id={province_id}&local_type_id={subject}' \
                                   '&page={page}&school_id={school_id}&size=10&special_group=&uri=apidata/api/gk/score/special&year={year}'
                        url = no_page_url.format(batch=batch, province_id=self.province_id, subject=subject, page=page, school_id=self.school_id, year=year)
                        safe_sign = hash_hmac(url)
                        encrypted_url = 'https://' + url + '&signsafe=' + safe_sign
                        time.sleep(random.randint(5, 60))
                        score_crawler = CeeCrawler(encrypted_url)
                        score_data = score_crawler.get_response()
                        self.data_storage.store(score_data.get('data').get('item'), collection_name=default_score_collection)
                        logging.info('%s %s %s %s page%s', self.school_name, year, batch, subject, page)
