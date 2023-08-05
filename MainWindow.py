from thinkdsp import CosSignal, SinSignal, Audio, SquareSignal, TriangleSignal, SawtoothSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider
import simpleaudio as sa
import numpy as np
from matplotlib.backends.qt_compat import QtWidgets

from widgets.octave_widget import OctaveWidget

from PyQt6.QtWidgets import QTabWidget

from widgets.synth_table import SignalSelector


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        self._frequency = 440

        self.layout = QtWidgets.QVBoxLayout(self._main)
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.West)
        self.tabs.setMovable(True)

        self.signal_selector_1 = SignalSelector(1, parent=self._main, main_window=self)
        self.signal_selector_2 = SignalSelector(2, parent=self._main, main_window=self)

        self.tabs.addTab(self.signal_selector_1, "Signal 1")
        self.tabs.addTab(self.signal_selector_2, "Signal 2")

        self.layout.addWidget(self.tabs)

        self.playButton = QPushButton("Play")
        self.playButton.clicked.connect(self.playButtonClicked)        
        self.layout.addWidget(self.playButton)

        self.updateWaveCanvasses()

        self.pianoWidget = OctaveWidget(parent=self._main)
        self.layout.addWidget(self.pianoWidget)
        self.pianoWidget.keyPressed.connect(self.pianoKeyPressed)



    def updateWaveCanvasses(self):
        self.signal_selector_1.updateWaveCanvas()
        self.signal_selector_2.updateWaveCanvas()

    def pianoKeyPressed(self, freq):
        self.setFrequency(freq)
        print(str(freq))
        self.playTone()

    def playButtonClicked(self):
        self.playTone()

    def setFrequency(self, freq):
        self._frequency = freq

    def playTone(self):
        f = self._frequency
        s1 = self.signal_selector_1.getSignal()
        s2 = self.signal_selector_2.getSignal()
        signal_1 = s1(freq=f, amp=5.0, offset=0)
        signal_2 = s2(freq=f, amp=5.0, offset=0)
        signal = signal_1 + signal_2
        w = signal.make_wave(duration=1, framerate=44100)
        audio_data = (w.ys * 32767).astype(np.int16)
        play_obj = sa.play_buffer(audio_data, num_channels=1, bytes_per_sample=2, sample_rate=w.framerate)
        play_obj.wait_done()