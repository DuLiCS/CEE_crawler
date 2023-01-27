"""
Analysis of the provincescore, specialplan and specialscore json file
"""
from setup_crawler import *
BASE_JSON_URL = 'https://static-data.gaokao.cn/www/2.0/school/{school_id}/dic/provincescore.json'


class JsonAnalysis:
    def __init__(self, school_name):
        self.school_name = school_name

    def province_score_analysis(self, school_id):
        pass

    def special_score_analysis(self):
        pass

    def special_plan_analysis(self):
        pass
