"""
This file contains functions of tools using in the CEE crawler
"""

import base64
import hmac
from hashlib import sha1, md5
from data_storage import *
default_check_db_name = 'school_info'


def hash_hmac(code, key='D23ABC@#56'):
    hmac_code = hmac.new(key.encode(), code.encode(), sha1).digest()
    b_64_t = base64.b64encode(hmac_code).decode()
    return md5(b_64_t.encode()).hexdigest()

def error_log(type_name, school_name, error_code):
    school_filter = {'school_name': school_name}
    new_values = {(type_name + '_flag'): error_code}
    store = DataStorage()
    collection = store.db[default_check_db_name]
    collection.update_one(school_filter, {'$set': new_values})




