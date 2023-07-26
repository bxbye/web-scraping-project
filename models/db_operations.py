from pymongo import MongoClient


class DbManager:
    def __init__(self, db_server_url, db_name) -> None:
        self.client = MongoClient(db_server_url)
        self.database = self.client[db_name]
    def set_collection(self, col_name):
        self.collection = self.database[col_name]

    # insert item to collection
    def insert_single_item(self, item):
        result = self.collection.insert_one(item)
        return result.inserted_id
    # insert many item to collection
    def insert_many_item(self, items):
        result = self.collection.insert_many(items)
        return result.inserted_ids
    # document size of the collection
    def get_item_count(self, query):
        return self.collection.count_documents(query)
    # delete collections method
    def drop_collection(self):
        self.collection.drop()
    # close connection
    def close_connection(self):
        self.client.close()