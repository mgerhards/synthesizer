## a widget that holds the buttons for selecting a waveform, and a slider for selecting the frequency and the canvas for plotting the signal and spectrum
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout

from widgets.frequency_slider import FrequencySlider
from widgets.waveform_selector import WaveformSelector
from widgets.mpl_canvas import MplCanvas

from thinkdsp import CosSignal, SinSignal, Audio, SquareSignal, TriangleSignal, SawtoothSignal

class SignalSelector(QtWidgets.QWidget):

    def __init__(self, i, main_window=None, parent=None):
        self._main_window = main_window
        self.i = i
        super().__init__(parent=parent)
        self._pitch = 440
        self._signal_func = CosSignal
        self.layout = QVBoxLayout()
        # add Label
        self.label = QtWidgets.QLabel("Signal " + str(self.i))
        # set alignment to center
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # set style to h1
        self.label.setStyle(QtWidgets.QStyleFactory.create("h1"))
        self.layout.addWidget(self.label)
        # Add wave buttons
        self.waveform_selector = WaveformSelector(parent=self, main_window=self)
        self.layout.addWidget(self.waveform_selector)

        #Add a slider
        self.slider = FrequencySlider(main_window=self)
        self.layout.addWidget(self.slider)

        self.sc = MplCanvas(self, width=3, height=2, dpi=150)
        self.fc = MplCanvas(self, width=3, height=2, dpi=150)

        self.graphics_layout = QtWidgets.QHBoxLayout()
        self.graphics_layout.addWidget(self.sc)
        self.graphics_layout.addWidget(self.fc)

        signal_widget = QtWidgets.QWidget()
        signal_widget.setLayout(self.graphics_layout)

        self.layout.addWidget(signal_widget)

    def updateWaveCanvas(self):
        self.sc.axes.clear()
        signal = self._signal_func(freq=self._pitch, amp=1.0, offset=0)
        wave = signal.make_wave(duration=0.25, framerate=10000)
        self.sc.axes.plot(wave.ts[:500], wave.ys[:500])
        self.sc.draw()
        self.updateSpectrumCanvas()

    def updateSpectrumCanvas(self):
        self.fc.axes.clear()
        signal = self._signal_func(freq=self._pitch, amp=1.0, offset=0)
        wave = signal.make_wave(duration=0.25, framerate=10000)
        spectrum = wave.make_spectrum()
        self.fc.axes.plot(spectrum.fs[:500], spectrum.amps[:500])
        self.fc.draw()

    def setSignal(self, signal):
        self._signal_func = signal

    def getSignal(self):
        return self._signal_func

    def getPitch(self):
        return self._pitch

    def getPitch(self, frequency):
        self._pitch = frequency