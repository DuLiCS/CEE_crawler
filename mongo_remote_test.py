import pymongo

MONGO_DB_NAME = 'cee_crawler'
MONGO_CONNECTION_STRING = 'mongodb://192.168.0.103:27017'

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
print('connection established')
db = client[MONGO_DB_NAME]
connection = db['school_info']

print(connection.find_one())
