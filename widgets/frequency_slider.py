
from PyQt6.QtWidgets import QWidget, QSlider, QLabel, QHBoxLayout, QPushButton, QVBoxLayout

from PyQt6.QtCore import QSize, Qt



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
        self.slider.setValue(440)
        
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
        self.main_window.setPitch(self.slider.value())
        self.main_window.updateWaveCanvas()
        self.frequency_value_label.setText(str(self.slider.value()))
        self.min_label.setText(str(self.slider.minimum()))
        self.max_label.setText(str(self.slider.maximum()))
        
        