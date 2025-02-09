from .mysql_metadata_handler import MySQLMetadataHandler
from .mongodb_metadata_handler import MongoDBMetadataHandler
class MetadataFactory:
    @staticmethod
    def get_metadata_handler(type):
        if type == "MYSQL":
            return MySQLMetadataHandler()
        if type == "MongoDB":
            return MongoDBMetadataHandler()
        if type == "ArangoDB":
            pass
        return None