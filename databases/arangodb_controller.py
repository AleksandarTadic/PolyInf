# import pymongo

from .interfaces.idatabase_controller import IDatabaseController
from .db_connections.arangodb_connection import ArangoDBConnection



# Zbog buga u pymongo koji je resen ali i dalje nije updatovana trenutna verzija ne sme se zatvarati konekcija sa mongom
# https://github.com/MongoEngine/mongoengine/issues/2627
class ArangoDBController(IDatabaseController):
    def __init__(self, credentials) -> None:
        self.credentials = credentials

        self.connection = ArangoDBConnection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])

    def get_connection(self):
        return self.connection.get_connection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])


    def get_all(self, collection, columns=None, values=None):
        pass
        
    
    def get_one(self, table_name, columns, values):
        pass
      

    def insert(self, collection, new_object):
        pass

    def update(self, collection, old_object, new_object):
        pass

    def delete(self, collection, object):
        pass
        # try:
        #     self.get_collection().delete_one(obj)
        # except Exception as e:
        #     print(e)
        # finally:
        #     self.disconect()
        #     self.connection = None
        #     self.load_data()
