from abc import ABC, abstractmethod

class IDatabaseController(ABC):
    @staticmethod
    @abstractmethod
    def get_all():
        pass
    
    @staticmethod
    @abstractmethod
    def get_one():
        pass

    @staticmethod
    @abstractmethod
    def insert():
        pass

    @staticmethod
    @abstractmethod
    def update():
        pass

    @staticmethod
    @abstractmethod
    def delete():
        pass