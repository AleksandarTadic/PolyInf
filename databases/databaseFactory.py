from .mysql_controller import MySQLController
from .mongodb_controller import MongoDBController
from .arangodb_controller import ArangoDBController

class DatabaseFactory:
    @staticmethod
    def get_database(type, credentials):
        if type == "MYSQL":
            return MySQLController(credentials)
        if type == "MongoDB":
            return MongoDBController(credentials)
        if type == "ArangoDB":
            return ArangoDBController(credentials)
        return None


# test = DatabaseFactory.get_database("NOSQL", {
#     "host": "localhost",
#     "port": 3306,
#     "user": "root",
#     "password": "root",
#     "database": "2023_nosql_baza_cinjenica"
# })