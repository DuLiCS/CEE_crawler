from data_scrape import *


class Crawler:
    def __init__(self):
        self.data_operator = DataStorage()

    def plan_crawler(self):
        plan_school_name = self.data_operator.no_scrape_name('plan')
        if plan_school_name is not None:
            plan_scrape = DataScrape(plan_school_name)
            plan_scrape.special_plan_scrape()
            self.data_operator.flag_change('plan', plan_school_name)
            return True
        else:
            return False

    def score_crawler(self):
        score_school_name = self.data_operator.no_scrape_name('score')
        if score_school_name is not None:
            score_scrape = DataScrape(score_school_name)
            score_scrape.special_score_scrape()
            self.data_operator.flag_change('score', score_school_name)
            return True
        else:
            return False

