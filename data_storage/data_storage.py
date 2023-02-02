"""
This file contains the class store the json data to txt, csv, json file and Mangodb
"""
import pymongo
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')
MONGO_DB_NAME = 'cee_crawler'
MONGO_CONNECTION_STRING = 'mongodb://192.168.0.103:27017'
default_check_db_name = 'full_school_info'
province = {
    11: "\u5317\u4eac",
    12: "\u5929\u6d25",
    13: "\u6cb3\u5317",
    14: "\u5c71\u897f",
    15: "\u5185\u8499\u53e4",
    21: "\u8fbd\u5b81",
    22: "\u5409\u6797",
    23: "\u9ed1\u9f99\u6c5f",
    31: "\u4e0a\u6d77",
    32: "\u6c5f\u82cf",
    33: "\u6d59\u6c5f",
    34: "\u5b89\u5fbd",
    35: "\u798f\u5efa",
    36: "\u6c5f\u897f",
    37: "\u5c71\u4e1c",
    41: "\u6cb3\u5357",
    42: "\u6e56\u5317",
    43: "\u6e56\u5357",
    44: "\u5e7f\u4e1c",
    45: "\u5e7f\u897f",
    46: "\u6d77\u5357",
    50: "\u91cd\u5e86",
    51: "\u56db\u5ddd",
    52: "\u8d35\u5dde",
    53: "\u4e91\u5357",
    54: "\u897f\u85cf",
    61: "\u9655\u897f",
    62: "\u7518\u8083",
    63: "\u9752\u6d77",
    64: "\u5b81\u590f",
    65: "\u65b0\u7586",
    81: "\u9999\u6e2f",
    82: "\u6fb3\u95e8",
    71: "\u53f0\u6e7e",
    99: "\u5176\u5b83",
    100: "\u4e0d\u5206\u7701",
    0: "\u5176\u5b83"
}

province = dict(zip(province.values(), province.keys()))


def province_id_query(province_name):
    return str(province[province_name])


class DataStorage:
    def __init__(self, db_name=MONGO_DB_NAME, addr=MONGO_CONNECTION_STRING):
        self.db_name = db_name
        client = pymongo.MongoClient(addr)
        self.db = client[self.db_name]

    def store(self, data, collection_name, method='mango'):
        if method == 'json':
            pass
        elif method == 'csv':
            pass
        elif method == 'mango':
            collection = self.db[collection_name]
            collection.insert_many(data)
            logging.info('data saving successfully')

    def school_province_id_query(self, school_name, collection_name='full_school_info'):
        collection = self.db[collection_name]
        school_query = {'name': school_name}
        record = collection.find_one(school_query)
        return record['school_id']

    def no_scrape_name(self, type_name):
        collection = self.db[default_check_db_name]
        result = collection.find_one({(type_name + '_flag'): 0})
        return result['name']

    def flag_change(self, type_name, school_name, change_num=1):
        school_filter = {'name': school_name}
        new_values = {(type_name + '_flag'): change_num}
        collection = self.db[default_check_db_name]
        collection.update_one(school_filter, {'$set': new_values})







