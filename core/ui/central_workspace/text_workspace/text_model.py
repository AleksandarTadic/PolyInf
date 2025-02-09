from PySide6 import QtWidgets, QtGui, QtCore
from databases.databaseFactory import DatabaseFactory
# import json
from ....design_patterns.observer.observable import Observable
from bson import json_util

class TextModel(Observable):
    def __init__(self, parent):
        self.observers = []
        self.interface = parent
        self.data_info = self.interface.data_info
        self.credentials = self.interface.credentials

    def get_text(self):
        self.database = DatabaseFactory().get_database(self.data_info["type"], self.credentials)
        self.data = self.database.get_all(self.data_info["name"])
        self.data = str(json_util.dumps(self.data, indent=4, ensure_ascii=False).encode('utf8').decode('utf-8'))

        document = QtGui.QTextDocument(self.data)
        text = document.toHtml()
        text = text.replace("style=\"", "style=\" color:#FFFFFF;")
        text = text.replace(",", "<span style='color:#FF7000'>,</span>").replace("&quot;: ", "&quot;<span style='color:#FF7000'>:</span> ")
        text = text.replace("[", "<span style='color:#FFFF00'>[</span>").replace("]", "<span style='color:#FFFF00'>]</span>").replace("{", "<span style='color:#FF0000'>{</span>").replace("}", "<span style='color:#FF0000'>}</span>")
        return text
    
    def update(self):
        self.notify("UPDATE", text = self.get_text())