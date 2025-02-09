from abc import ABC, abstractmethod

class IConnection(ABC):
    @staticmethod
    @abstractmethod
    def get_connection():
        pass
    
    @staticmethod
    @abstractmethod
    def close_connection():
        pass