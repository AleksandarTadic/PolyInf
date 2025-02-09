from abc import ABCMeta, abstractmethod

class IToolbarBuilder(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def set_spacer():
        pass

    @staticmethod
    @abstractmethod
    def set_first():
        pass

    @staticmethod
    @abstractmethod
    def set_last():
        pass

    @staticmethod
    @abstractmethod
    def set_insert():
        pass

    @staticmethod
    @abstractmethod
    def set_previous_page():
        pass

    @staticmethod
    @abstractmethod
    def set_next_page():
        pass

    @staticmethod
    @abstractmethod
    def set_delete():
        pass

    @staticmethod
    @abstractmethod
    def set_promote_subtable():
        pass

    @staticmethod
    @abstractmethod
    def set_combobox():
        pass
    
    @staticmethod
    @abstractmethod
    def get_result():
        pass