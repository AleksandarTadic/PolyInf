from PySide6 import QtWidgets, QtGui, QtCore

from PySide6.QtWebEngineWidgets import QWebEngineView
class WebWorkspace(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.central_workspace = parent
        self.workspace = parent
        self.layout = QtWidgets.QVBoxLayout()

        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 150))
        self.setGraphicsEffect(self.shadow)

        self.web_view = QWebEngineView()
        self.web_view.setGraphicsEffect(self.shadow)
        self.web_view.graphicsEffect().setEnabled(False)
        self.web_view.load(QtCore.QUrl("http://127.0.0.1:8529/"))

        self.layout.addWidget(self.web_view)
        self.setLayout(self.layout)

