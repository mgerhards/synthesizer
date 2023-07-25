from PyQt6.QtWidgets import QApplication
# Only needed for access to command line arguments
import sys
from MainWindow import MainWindow
import thinkdsp

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
