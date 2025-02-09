from PySide6 import QtWidgets, QtGui, QtCore

from .interface_toolbar_builder import IToolbarBuilder

class Toolbar(QtWidgets.QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.interface = parent
        self.setMovable(False)
        self.setFloatable(False)

