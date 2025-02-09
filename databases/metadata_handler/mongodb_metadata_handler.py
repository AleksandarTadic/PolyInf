import json

from .interface_metadata import IMetadata
from ..databaseFactory import DatabaseFactory

class MongoDBMetadataHandler(IMetadata):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDBMetadataHandler, cls).__new__(cls)
        return cls._instance

    def load(self):
        database = DatabaseFactory().get_database("MongoDB", {
            "host":"localhost",
            "port": 27017,
            "user": "root",
            "password": "root",
            "database": "rukovalac_heterogenim_skladistima"
        })
        return database


    def get_metadata(self, name):
        metadata = self.load()
        return metadata.get_all("metadata")

    def get_headers(self, name):
        metadata = self.get_metadata(name)
        if len(metadata) == 0:
            return []
        return list(metadata[0].keys())

    def get_code_names(self, name):
        metadata = self.get_metadata(name)
        if len(metadata) == 0:
            return []
        return list(metadata[0].keys())
    

