import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


from matplotlib.backends.qt_compat import QtWidgets

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")        
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)
        
        #Add a slider
        slider = QSlider(Qt.Orientation.Horizontal)
        layout.addWidget(slider)
        
        # Add area for plotting signal with matplotlib
        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(dynamic_canvas)

if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    # Only needed for access to command line arguments
    import sys
    from gui.MainWindow import MainWindow

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
