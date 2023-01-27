"""
This file contains functions that initialize the CEE crawler
"""
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')
Safari_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Version/16.1 Safari/605.1.15'}


class CeeCrawler(object):
    def __init__(self, url, headers=Safari_headers):
        self.url = url
        self.headers = Safari_headers

    def get_response(self):
        logging.info('start scraping %s', self.url)
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                return response.json()
            logging.error('get invalid status code %s while scraping %s', response.status_code, self.url)
        except requests.RequestException:
            logging.error('error occurred while scraping %s', self.url, exc_info=True)
