from setup_crawler import *
from data_storage import *

MONGO_DB_NAME = 'cee_crawler'
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                        'Version/16.1 Safari/605.1.15'}
school_name = '中国科学技术大学'


id_query = DataStorage(MONGO_DB_NAME, MONGO_CONNECTION_STRING)
