# import pymongo

from .interfaces.idatabase_controller import IDatabaseController
from .db_connections.mongodb_connection import MongoDBConnection



# Zbog buga u pymongo koji je resen ali i dalje nije updatovana trenutna verzija ne sme se zatvarati konekcija sa mongom
# https://github.com/MongoEngine/mongoengine/issues/2627
class MongoDBController(IDatabaseController):
    def __init__(self, credentials) -> None:
        self.credentials = credentials

        self.connection = MongoDBConnection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])


    def get_all(self, collection, columns=None, values=None):
        data = []
        connection = self.connection.get_connection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])
        try:
            db = connection[self.credentials["database"]][collection]
            data = list(db.find({}))
            # return list(db.find({}))
        except Exception as e:
            print(e)
        finally:
            self.connection.close_connection()
        return data
        
    # def get_all(self, collection, columns=None, values=None):
    #     data = []
    #     connection = self.connection.get_connection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])
    #     try:
    #         db = connection[self.credentials["database"]][collection]
    #         with db.find({}) as cursor:
    #             data = list(cursor)
    #             # data = list(db.find({}))
    #         # return list(db.find({}))
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         # pass
    #         self.connection.close_connection()
    #     return data
    
    def get_one(self, table_name, columns, values):
        pass
      

    def insert(self, collection, new_object):
        connection = self.connection.get_connection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])
        try:
            db = connection[self.credentials["database"]][collection]
            if type(new_object) == dict:
                db.insert_one(new_object)
            elif type(new_object) == []:
                db.insert_many(new_object)
        except Exception as e:
            print(e)
        finally:
            self.connection.close_connection()

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
