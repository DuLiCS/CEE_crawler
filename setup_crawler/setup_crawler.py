"""
This file contains functions that initialize the CEE crawler
"""
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')


class CeeCrawler(object):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_response(self):
        logging.info('start scraping %s', self.url)
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                return response.json()
            logging.error('get invalid status code %s while scraping %s', response.status_code, self.url)
        except requests.RequestException:
            logging.error('error occurred while scraping %s', self.url, exc_info=True)
