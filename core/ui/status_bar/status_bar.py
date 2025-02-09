from datetime import date

from PySide6 import QtWidgets, QtGui, QtCore

# from obs.observer import Observer
from core.design_patterns.observer.observer import Observer

class StatusBar(QtWidgets.QStatusBar, Observer):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_window = parent
        self.message = None
        self.showMessage('Status bar je prazan!')

    def show_message(self, message):
        self.message = message
        self.showMessage(self.message)

    def show_status(self, task, name):
        name = name.replace("_", " ").split(" - ")
        message = task + " ste " + name[0] + "!          Tip: " + name[1]
        self.message = message
        self.showMessage(self.message)


    def update(self, event, **kwargs):
        if event == "SHOW_MESSAGE":
            self.showMessage(kwargs["message"])
        if event == "SHOW_STATUS":
            self.showMessage(kwargs["message"])
        