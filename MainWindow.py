from thinkdsp import CosSignal, SinSignal, Audio, SquareSignal, TriangleSignal, SawtoothSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider
import simpleaudio as sa
import numpy as np
from matplotlib.backends.qt_compat import QtWidgets

from widgets.frequency_slider import FrequencySlider
from widgets.waveform_selector import WaveformSelector
from widgets.mpl_canvas import MplCanvas
from widgets.octave_widget import OctaveWidget

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._signal_func = CosSignal
        self._frequency = 440
        self.setWindowTitle("My App")        
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        self.layout = QtWidgets.QVBoxLayout(self._main)
        
        # Add wave buttons
        self.waveform_selector = WaveformSelector(parent=self._main, main_window=self)
        self.layout.addWidget(self.waveform_selector)
        
        #Add a slider
        self.slider = FrequencySlider(main_window=self)
        self.layout.addWidget(self.slider) 
        
        # Add area for plotting signal with matplotlib
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])        
        self.layout.addWidget(self.sc)

        self.playButton = QPushButton("Play")
        self.playButton.clicked.connect(self.playButtonClicked)        
        self.layout.addWidget(self.playButton)

        self.updateWaveCanvas()
        self.pianoWidget = OctaveWidget(parent=self._main)
        self.layout.addWidget(self.pianoWidget)
        self.pianoWidget.keyPressed.connect(self.pianoKeyPressed)

    def pianoKeyPressed(self, freq):
        self.setFrequency(freq)
        print(str(freq))
        self.playTone()

    def setSignal(self, signal):
        self._signal_func = signal
    
    def setFrequency(self, frequency):
        self._frequency = frequency
    
    def updateWaveCanvas(self):
        self.sc.axes.clear()
        signal = self._signal_func(freq=self._frequency, amp=1.0, offset=0)        
        wave = signal.make_wave(duration=1, framerate=10000)
        self.sc.axes.plot(wave.ts[:500], wave.ys[:500])
        self.sc.draw()

    def playButtonClicked(self):
        self.playTone()

    def playTone(self):
        signal = self._signal_func(freq=self._frequency, amp=1.0, offset=0)        
        w = signal.make_wave(duration=1, framerate=44100)
        audio_data = (w.ys * 32767).astype(np.int16)
        play_obj = sa.play_buffer(audio_data, num_channels=1, bytes_per_sample=2, sample_rate=w.framerate)
        play_obj.wait_done()