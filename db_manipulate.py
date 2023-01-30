from data_storage import *

db_manipulate = DataStorage()
collection = db_manipulate.db['full_school_info']
mini_collection = db_manipulate.db['school_info']
results = mini_collection.find({'plan_flag':1})
for result in results:
    school_name = result['school_name']
    print(school_name)
    collection.find_one_and_update({'name':school_name},{'$set':{'plan_flag':1}})