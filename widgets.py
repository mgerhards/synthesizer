
from PyQt6.QtWidgets import QWidget, QSlider, QLabel, QHBoxLayout, QPushButton, QVBoxLayout

from PyQt6.QtCore import QSize, Qt
from matplotlib.figure import Figure

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from thinkdsp import CosSignal, SawtoothSignal, SquareSignal, TriangleSignal

class FrequencySlider(QWidget):
    # setupt the slider
    def __init__(self, main_window, parent=None):
        QWidget.__init__(self, parent)
        
        self.main_window = main_window
        self.vlayout = QVBoxLayout()
        self.layout = QHBoxLayout()
        self.min_label = QLabel()
        self.max_label = QLabel()
        self.slider = QSlider(orientation=Qt.Orientation.Horizontal)
        
        self.layout.addWidget(self.min_label)
        self.layout.addWidget(self.slider)  
        self.layout.addWidget(self.max_label)
        
        self.frequency_label = QLabel("Frequency")
        self.frequency_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vlayout.addWidget(self.frequency_label)
        
        self.frequency_value_label = QLabel("0")
        self.frequency_value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)   
        self.vlayout.addWidget(self.frequency_value_label)
        
        self.vlayout.addLayout(self.layout)
        
        self.setLayout(self.vlayout)

        # Default minimum and maximum values
        self.setMinimum(16)
        self.setMaximum(8000)
        self.setValues(16, 8000)
        
        # Connect the slider's valueChanged signal to the updateLabels function
        self.slider.valueChanged.connect(self.updateLabels)
    
    def setMinimum(self, value):
        self.slider.setMinimum(value)

    def setMaximum(self, value):
        self.slider.setMaximum(value)

    def setValues(self, min_val, max_val):
        self.slider.setRange(min_val, max_val)

    def setValue(self, value):
        self.slider.setValue(value)

    def updateLabels(self):
        self.main_window.setFrequency(self.slider.value())
        self.main_window.updateWaveCanvas()
        self.frequency_value_label.setText(str(self.slider.value()))
        self.min_label.setText(str(self.slider.minimum()))
        self.max_label.setText(str(self.slider.maximum()))
        
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
    
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        
        