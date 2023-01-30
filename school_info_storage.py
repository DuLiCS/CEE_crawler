from setup_crawler import *
from data_storage import *

MONGO_DB_NAME = 'cee_crawler'
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
school_num_url = 'https://static-gkcx.gaokao.cn/www/2.0/json/live/v2/schoolnum.json'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                        'Version/16.1 Safari/605.1.15'}

crawler_test = CeeCrawler(school_num_url, headers)
response = crawler_test.get_response()
school_info_db = DataStorage(MONGO_DB_NAME, MONGO_CONNECTION_STRING)
collection_name = 'school_info_full'
school_info_db.store(response.get('data'), collection_name)
