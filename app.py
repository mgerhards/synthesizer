from PyQt6.QtWidgets import QApplication
# Only needed for access to command line arguments
import sys
from MainWindow import MainWindow
import thinkdsp
from qt_material import apply_stylesheet
from PyQt6.QtWidgets import QStyleFactory
print(QStyleFactory.keys())

app = QApplication(sys.argv)
apply_stylesheet(app, theme='dark_blue.xml')

window = MainWindow()

window.show()

app.exec()
