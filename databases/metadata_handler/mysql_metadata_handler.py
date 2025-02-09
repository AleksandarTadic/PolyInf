import json

from .interface_metadata import IMetadata

class MySQLMetadataHandler(IMetadata):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MySQLMetadataHandler, cls).__new__(cls)
        return cls._instance

    def load(self):
        try:
            with open("databases\metadata_handler\metadata\metadata_mysql.json") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Fajl nije pronadjen na ovoj putanji")
        except Exception as e:
            print(f"Dogodio se error: {e}")


    def get_metadata(self, name):
        metadata = self.load()
        for table in metadata:
            if table["name"] == name:
                return table

    def get_headers(self, name):
        metadata = self.get_metadata(name)
        headers = []
        for data in metadata["columns"]:
            headers.append(data["label"])
        return headers  

    def get_code_names(self, name):
        metadata = self.get_metadata(name)
        code_names = []
        for data in metadata["columns"]:
            code_names.append(data["code"])
        return code_names  
    
    def get_linked_tables(self, name):
        metadata = self.get_metadata(name)
        return metadata["linked_keys"]


# test = MySQLMetadataHandler()
# print(test.get_metadata("poslovni_subjekat"))
# print(test.get_headers("poslovni_subjekat"))
# print(test.get_code_names("poslovni_subjekat"))
# print(test.get_linked_tables("poslovni_subjekat"))


