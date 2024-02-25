import pymongo

from CONFIG.CONFIG_DATABASE import HOST
from CONFIG.CONFIG import *

    
class EasyDBCreator:
    def __init__(self):
        self.host = HOST
        self.collections = None
        
    def generate_db(self):
        try:
            client = pymongo.MongoClient(self.host)
        except Exception as exp:
            print(exp)
        db = client.bot
        
        grid = db.grid # {'_id': chat_id, 'grid_id': grid_id}
        chats = db.chats # {'_id': chat_id, 'chat_name': chat_name, 'vip': True|False, 'count_msg': count_msg, 'admins': [(admin_id, 1), (admin_id, 2), (owner_id, 3)]}
        permissions = db.permissions # {'_id': chat_id, 'permissions': {'permission_4: 4, permission_0' : 0, permission_1' : 1, 'permission_2' : 1, 'permission_3' : 3}} --> 1,2,3 - rangs, 0 - all, 4 - nobody
        users = db.users
        locales = db.locales
        
        self.collections = {'grid': grid,
                            'chats': chats,
                            'permissions': permissions,
                            'users': users,
                            'locales': locales}
        return
        
    def insert(self, coll_name, query):
        self.collections[coll_name].insert_one(query)
        return
        
    def find(self, coll_name, query, filter=None):
        return list(self.collections[coll_name].find(query, filter))
        
    def sort_limit(self, coll_name, filter, limit=50):
        return list(self.collections[coll_name].sort(filter).limit(limit))
    
    def count(self, coll_name, filter=None):
        return self.collections[coll_name].count_documents(filter)
    
    def update(self, coll_name, current, new_data):
        self.collections[coll_name].update_one(current, new_data)
    
    def delete(self, coll_name, query):
        self.collections[coll_name].delete_one(query)
    