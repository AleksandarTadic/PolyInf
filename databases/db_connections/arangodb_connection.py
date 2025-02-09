from pyArango.connection import *
import json
from .interface_connection import IConnection

class ArangoDBConnection(IConnection):
    _connection = None

    def __init__(self, host: str, port: int, user: str, password: str) -> None:
        if ArangoDBConnection._connection is None:
            ArangoDBConnection._connection = Connection(arangoURL=f"http://{host}:{port}", username=user, password=password)


    @staticmethod
    def get_connection(host: str, port: int, user: str, password: str):
        if not ArangoDBConnection._connection:
            ArangoDBConnection._connection = Connection(arangoURL=f"http://{host}:{port}", username=user, password=password)
        return ArangoDBConnection._connection
    
    @staticmethod
    def close_connection():
        # ????
        ArangoDBConnection._connection.disconnectSession()
        ArangoDBConnection._connection = None
        # ArangoDBConnection.__connection.close()
