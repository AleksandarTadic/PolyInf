from abc import ABC, abstractmethod

class IMetadata(ABC):

    @staticmethod
    @abstractmethod
    def load():
        pass
    
    @staticmethod
    @abstractmethod
    def get_metadata(name):
        pass

    @staticmethod
    @abstractmethod
    def get_headers(name):
        pass

    @staticmethod
    @abstractmethod
    def get_code_names(name):
        pass
