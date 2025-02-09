import pymongo
from .interface_connection import IConnection

class MongoDBConnection(IConnection):
    _connection = None

    def __init__(self, host: str, port: int, user: str, password: str) -> None:
        if MongoDBConnection._connection is None:
            MongoDBConnection._connection = pymongo.MongoClient(f"mongodb://{host}:{port}")

    @staticmethod
    def get_connection(host: str, port: int, user: str, password: str):
        if not MongoDBConnection._connection:
            MongoDBConnection._connection = pymongo.MongoClient(f"mongodb://{host}:{port}")
        return MongoDBConnection._connection
    
    @staticmethod
    def close_connection():
        MongoDBConnection._connection.close()
        MongoDBConnection._connection = None
