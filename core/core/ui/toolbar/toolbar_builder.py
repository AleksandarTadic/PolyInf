from PySide6 import QtWidgets, QtGui, QtCore
from .interface_toolbar_builder import IToolbarBuilder
from .toolbar import Toolbar

class ToolbarBuilder(IToolbarBuilder):
    def __init__(self, parent, invoker):
        self.toolbar = Toolbar(parent)
        self.invoker = invoker

    def set_spacer(self):
        spacer = QtWidgets.QWidget()
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer)
        return self

    def set_first(self):
        action = QtGui.QAction(self.toolbar)
        action.setText("First row")
        action.setIcon(QtGui.QIcon('resources/icons/up.png'))
        action.triggered.connect(lambda: self.invoker.execute("FIRST_ROW"))
        self.toolbar.addAction(action)
        return self

    def set_last(self):
        action = QtGui.QAction(self.toolbar)
        action.setText("Last row")
        action.setIcon(QtGui.QIcon('resources/icons/down.png'))
        action.triggered.connect(lambda: self.invoker.execute("LAST_ROW"))
        self.toolbar.addAction(action)
        return self

    def set_previous_page(self):
        action = QtGui.QAction(self.toolbar)
        action.setText("Previous page")
        action.setIcon(QtGui.QIcon('resources/icons/previous_page.png'))
        action.triggered.connect(lambda : self._message("Alert!", "Not implemented!"))
        self.toolbar.addAction(action)
        return self

    def set_next_page(self):
        action = QtGui.QAction(self.toolbar)
        action.setText("Next page")
        action.setIcon(QtGui.QIcon('resources/icons/next_page.png'))
        action.triggered.connect(lambda : self._message("Alert!", "Not implemented!"))
        self.toolbar.addAction(action)
        return self

    def set_insert(self):
        action = QtGui.QAction("ADD", self.toolbar)
        action.setText("Add row")
        action.setIcon(QtGui.QIcon("resources/icons/new_row.png"))
        action.triggered.connect(lambda : self._message("Alert!", "Not implemented!"))
        self.toolbar.addAction(action)
        return self

    def set_delete(self):
        action = QtGui.QAction("DELETE", self.toolbar)
        action.setText("Delete row")
        action.setIcon(QtGui.QIcon("resources/icons/delete_row.png"))
        action.triggered.connect(lambda : self._message("Alert!", "Not implemented!"))
        self.toolbar.addAction(action)
        return self
    
    def set_promote_subtable(self):
        action = QtGui.QAction("PROMOTE", self.toolbar)
        action.setText("Promote subtable")
        action.setIcon(QtGui.QIcon("resources/icons/promote.png"))
        action.triggered.connect(lambda: self.invoker.execute("PROMOTE_SUBTABLE"))
        self.toolbar.addAction(action)
        return self

    def set_combobox(self):
        combobox = QtWidgets.QComboBox()
        combobox.setEditable(False)
        combobox.setMinimumWidth(100)
        combobox.addItem('Table')
        combobox.addItem('Tree')
        combobox.addItem('Text')
        combobox.setCurrentText(self.toolbar.interface.get_display_type()) 
        self.toolbar.addWidget(combobox)

        def text_changed(new_value):
            self.toolbar.interface.set_display_type(new_value)
            self.invoker.execute("CHANGE_DISPLAY_TYPE")

        combobox.currentTextChanged.connect(text_changed)
        return self

    def get_result(self):
        return self.toolbar
    
    def _message(self, title, message):
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowIcon(QtGui.QIcon("resources/icons/wrr.png"))
        dlg.setIcon(QtWidgets.QMessageBox.Information)
        dlg.setWindowTitle(title)
        dlg.setText(message)
        dlg.exec()