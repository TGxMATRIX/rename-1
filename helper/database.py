import motor.motor_asyncio
from config import DB_URL, DB_NAME
from helper.date import add_date
DB_NAME = os.environ.get("DB_NAME","")
DB_URL = os.environ.get("DB_URL","")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]

#Total User 

def total_user():
      user = dbcol.count_documents({})
      return user
      
#insert bot Data 
def botdata(chat_id):
	bot_id = int(chat_id)
	try:
		bot_data = {"_id":bot_id,"total_rename":0,"total_size":0}
		dbcol.insert_one(bot_data)
	except:
		pass


def total_rename(chat_id,renamed_file):
	now = int(renamed_file) + 1
	dbcol.update_one({"_id":chat_id},{"$set":{"total_rename":str(now)}})
	
def total_size(chat_id,total_size,now_file_size):
	now = int(total_size) + now_file_size
	dbcol.update_one({"_id":chat_id},{"$set":{"total_size":str(now)}})

	
#insert user data 
def insert(chat_id):
            user_id = int(chat_id)
            user_det = {"_id":user_id,"file_id":None ,"caption":None ,"daily":0 ,"date":0 , "uploadlimit" :2147483648,"used_limit":0,"usertype":"Free","prexdate" : None}
            try:
            	dbcol.insert_one(user_det)
            except:
            	return True
            	pass
class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.user

    def new_user(self, id):
        return dict(
            _id=int(id),                                   
            file_id=None,
            caption=None
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return bool(user)

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'_id': int(user_id)})
    
    async def set_thumbnail(self, id, file_id):
        await self.col.update_one({'_id': int(id)}, {'$set': {'file_id': file_id}})

    async def get_thumbnail(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('file_id', None)

    async def set_caption(self, id, caption):
        await self.col.update_one({'_id': int(id)}, {'$set': {'caption': caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('caption', None)


db = Database(DB_URL, DB_NAME)
