import pymysql
from .interface_connection import IConnection

class MySQLConnection(IConnection):
    _connection = None

    def __init__(self, host: str, port: int, user: str, password: str) -> None:
        if MySQLConnection._connection is None:
            MySQLConnection._connection = pymysql.connect(host=host, user=user, password=password, db=None, charset="utf8", cursorclass=pymysql.cursors.DictCursor)

    @staticmethod
    def get_connection(host: str, port: str, user: str, password: str):
        if not MySQLConnection._connection:
            MySQLConnection._connection = pymysql.connect(host=host, user=user, password=password, db=None, charset="utf8", cursorclass=pymysql.cursors.DictCursor)
        return MySQLConnection._connection
    
    @staticmethod
    def close_connection():
        MySQLConnection._connection.close()
        MySQLConnection._connection = None


