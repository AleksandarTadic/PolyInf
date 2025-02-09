from PySide6 import QtWidgets, QtGui, QtCore

class TreeView(QtWidgets.QTreeWidget):
        def __init__(self, parent):
            super().__init__(parent)
            self.interface = parent
            self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
            self.header().setMinimumSectionSize(300)
            self.header().resizeSection(0, 300)
            self.header().resizeSection(1, 800)
            
        def first_row(self):
            return self.setCurrentIndex(self.model().index(0, 0))
    
        def last_row(self):
            return self.setCurrentIndex(self.model().index(self.model().rowCount()-1, 0))