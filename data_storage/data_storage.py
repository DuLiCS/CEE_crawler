"""
This file contains the class store the json data to txt, csv, json file and Mangodb
"""
import pymongo
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')


class DataStorage:

    def __init__(self, db_name, addr):
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
            collection.insert_many(data.get('data').values())
            logging.info('data saving successfully')

    def school_province_id_query(self, school_name, collection_name='school_info'):
        collection = self.db[collection_name]
        school_query = {'school_name':school_name}
        record = collection.find_one(school_query)
        return record['school_id'], record['province_id']