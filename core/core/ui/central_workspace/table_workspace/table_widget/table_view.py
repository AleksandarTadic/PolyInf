from PySide6 import QtWidgets, QtGui, QtCore

class TableView(QtWidgets.QTableView):
        def __init__(self, parent):
            super().__init__(parent)
            self.interface = parent
            self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
            self.horizontalHeader().setStretchLastSection(True)

        def first_row(self):
            return self.selectRow(0)
    
        def last_row(self):
            return self.selectRow(self.interface.model.rowCount(0)-1)
        
        def promote_subtable(self):
            return self.interface.workspace.workspace.main_window.central_widget.add_tab_widget(self.interface.data_info, self.interface.credentials)