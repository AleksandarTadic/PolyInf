from PySide6 import QtWidgets, QtGui, QtCore
from core.design_patterns.observer.observable import Observable


import json

class DockModel(Observable):
    def __init__(self) -> None:
        super().__init__()
        self.metadatas = self.load_metadata()
    
    def display(self):
        self.notify("DISPLAY", message = self.metadatas)
    
    def load_metadata(self):
        with open("resources/data/metadata.json", encoding="utf-8") as f:
            return json.load(f)
