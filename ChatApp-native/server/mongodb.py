from pymongo import MongoClient
import datetime
import pprint
from bson.objectid import ObjectId
client = MongoClient('mongodb://localhost:27017/')
db = client['chat-database']
users = db['users_collection']
messages = db['messages_collection']
message = {"mssg":'hello',
"date": datetime.datetime.utcnow()}
user = {"email": 'ahmed',
         "password": '5434182',
         "date": datetime.datetime.utcnow()}
msg = messages.insert([message,user])
# for x in msg:
#     for i in messages.find({"_id": ObjectId(x)}):
#         print(i)
# users_data = users.insert_one(user)
# user = users.find_one({"email":'elmahdy30@gmail.com'})
# print(user)
