"""
This file contains functions of tools using in the CEE crawler
"""
import pymongo
from data_storage import *

MONGO_DB_NAME = 'cee_crawler'
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'

def school_id_query(school_name):
    db = DataStorage(MONGO_DB_NAME, MONGO_CONNECTION_STRING)
    collection_name = 'school_info'