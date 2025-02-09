class Observable:
    def __init__(self) -> None:
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)
    
    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]
    
    def notify(self, event, **kwargs):
        for observer in self.observers:
            observer.update(event, **kwargs)