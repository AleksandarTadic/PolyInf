from ..design_patterns.observer.observable import Observable

class CommunicationService(Observable):
    def __init__(self) -> None:
        super(Observable, self).__init__()
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, event, **kwargs):
        for observer in self._observers:
            observer.update(event, **kwargs)