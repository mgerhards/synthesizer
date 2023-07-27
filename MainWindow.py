import sys
from thinkdsp import CosSignal, SinSignal

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


from matplotlib.backends.qt_compat import QtWidgets

from widgets import FrequencySlider, MplCanvas, WaveformSelector

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")        
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        self.layout = QtWidgets.QVBoxLayout(self._main)
        
        # Add wave buttons
        self.waveform_selector = WaveformSelector(parent=self._main, main_window=self)
        self.layout.addWidget(self.waveform_selector)
        
        #Add a slider
        self.slider = FrequencySlider(Qt.Orientation.Horizontal)
        self.layout.addWidget(self.slider) 
        
        # Add area for plotting signal with matplotlib
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])        
        self.layout.addWidget(self.sc)
        
        self.playButton = QPushButton("Play")
        self.playButton.clicked.connect(self.playButtonClicked)        
        self.layout.addWidget(self.playButton)
        
        
    def playButtonClicked(self):
        pass
        
