from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton

from thinkdsp import CosSignal, SawtoothSignal, SquareSignal, TriangleSignal

class WaveformSelector(QWidget):
    def __init__(self, parent=None, main_window=None):
        QWidget.__init__(self, parent)
        
        self.main_window = main_window
        self.layout = QHBoxLayout()
        self.sineButton = QPushButton("Sine")
        self.sineButton.clicked.connect(self.sineButtonClicked)
        self.layout.addWidget(self.sineButton)
        
        self.squareButton = QPushButton("Square")
        self.squareButton.clicked.connect(self.squareButtonClicked)
        self.layout.addWidget(self.squareButton)
        
        self.sawButton = QPushButton("Sawtooth")
        self.sawButton.clicked.connect(self.sawButtonClicked)
        self.layout.addWidget(self.sawButton)
        
        self.triangleButton = QPushButton("Triangle")
        self.triangleButton.clicked.connect(self.triangleButtonClicked)
        self.layout.addWidget(self.triangleButton)
         
        self.setLayout(self.layout)

    def sineButtonClicked(self):        
        self.main_window.setSignal(CosSignal)
        self.main_window.updateWaveCanvas()     
        
    def squareButtonClicked(self):
        self.main_window.setSignal(SquareSignal)
        self.main_window.updateWaveCanvas()     
    
    def sawButtonClicked(self):
        self.main_window.setSignal(SawtoothSignal)
        self.main_window.updateWaveCanvas()        
        
    def triangleButtonClicked(self):
        self.main_window.setSignal(TriangleSignal)
        self.main_window.updateWaveCanvas()