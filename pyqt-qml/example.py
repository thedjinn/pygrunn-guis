import sys

from PyQt4.QtCore import QDateTime, QObject, QUrl, pyqtSignal
from PyQt4.QtGui import QApplication
from PyQt4.QtDeclarative import QDeclarativeView

# This class will emit the current date and time as a signal when
# requested.
class Controller(QObject):
    def __init__(self):
        QObject.__init__(self)

        # Create window
        self.view = QDeclarativeView()
        self.view.setWindowTitle("PyGrunn QML Demo")
        self.view.setSource(QUrl('interface.qml'))
        self.view.setResizeMode(QDeclarativeView.SizeRootObjectToView)

        # Setup root object
        self.root = self.view.rootObject()
        self.root.updateMessage("Click to get the current date and time")

        # Connect signals
        self.root.getTime.connect(self.getTime)

        # Show window
        self.view.setGeometry(100, 100, 400, 240)
        self.view.show()
        self.view.raise_()

    def getTime(self):
        formattedDate = QDateTime.currentDateTime().toString()
        self.root.updateMessage(formattedDate)

app = QApplication(sys.argv)
controller = Controller()
app.exec_()
