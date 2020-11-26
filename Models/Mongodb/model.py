from pymongo import MongoClient

client = MongoClient(f"mongodb://mongo:Dev123@192.168.99.100:27017")
db = client.total_bank


class Usuarios(object):
    
    def __init__(self):
        None
    
    def query(self):
        None
    
    def insertData(self):
        None