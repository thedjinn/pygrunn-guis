import sys
from PyQt4 import QtGui, QtCore

class ExampleWindow(QtGui.QWidget):
    def __init__(self):
        super(ExampleWindow, self).__init__()

        # Set up the window
        self.setWindowTitle("PyGrunn Demo")
        self.setGeometry(250, 150, 300, 150)

        # Create the label
        label = QtGui.QLabel("This is an <b>example label</b>. Click on the button below to show a dialog.", self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setWordWrap(True)

        # Create the button
        button = QtGui.QPushButton("Click Me!", self)
        button.setGeometry(20, 110, 260, 70)
        button.clicked.connect(self.click_handler)

        # Create a box
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(button)
        vbox.setSpacing(20)
        vbox.setContentsMargins(20, 20, 20, 20)
        self.setLayout(vbox)

        # Show the window
        self.show()
        self.raise_()

    def click_handler(self):
        # Show the dialog window, blocks until the window is dismissed
        QtGui.QMessageBox.information(self, "Dialog", "<b>You clicked the button.</b><br><br>Now go grab yourself a cold one, because you've earned it!")

app = QtGui.QApplication(sys.argv)
example = ExampleWindow()
sys.exit(app.exec_())
