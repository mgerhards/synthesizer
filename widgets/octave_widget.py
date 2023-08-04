from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QStackedLayout
from PyQt6.QtCore import Qt, QPoint, QRect


NOTE_INDEX_MAPPING = {
    'C': 0,
    'C#': 1,
    'Db': 1,
    'D': 2,
    'D#': 3,
    'Eb': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'Gb': 6,
    'G': 7,
    'G#': 8,
    'Ab': 8,
    'A': 9,
    'A#': 10,
    'Bb': 10,
    'B': 11
}


class KeyWidget(QWidget):

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name


class OctaveWidget(QWidget):

    keyPressed = QtCore.pyqtSignal(float)

    def __init__(self, octave=4, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._octave = octave
        self._white_keys = [KeyWidget("C"), KeyWidget("D"), KeyWidget("E"), KeyWidget("F"), KeyWidget("G"), KeyWidget("A"), KeyWidget("B")]
        self._black_keys = [KeyWidget("C#"), KeyWidget("D#"), KeyWidget("F#"), KeyWidget("G#"), KeyWidget("A#")]

    def sizeHint(self) -> QtCore.QSize:
        return QtCore.QSize(100, 100)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        painter.fillRect(0, 0, painter.device().width(), painter.device().height(), QtGui.QColor(0, 0, 0))
        key_width = int(painter.device().width() / 7)
        key_height = painter.device().height()

        black_key_height = int(key_height / 2)

        # paints all white keys
        for i, key in enumerate(self._white_keys):
            brush.setColor(QtGui.QColor(255, 255, 255))
            brush.setStyle(Qt.BrushStyle.SolidPattern)
            painter.setBrush(brush)
            r = QRect(i * key_width, 0, key_width - 2, key_height)
            painter.drawRect(r)
            key.setGeometry(r)

        # paints all black keys
        gap = 0
        for i, key in enumerate(self._black_keys):
            brush.setColor(QtGui.QColor(40, 40, 40))
            brush.setStyle(Qt.BrushStyle.SolidPattern)
            painter.setBrush(brush)
            if i == 2:
                gap = 1
            r = QRect(int(key_width/2)+gap*key_width+i*key_width, 0, key_width-2, black_key_height)
            painter.drawRect(r)
            key.setGeometry(r)

    def mousePressEvent(self, event):
        for key in self._black_keys+self._white_keys:
            if key.geometry().contains(event.pos()):
                print(f"Clicked on rect: {key.name}")
                # emit signal with value
                f = self.get_piano_key_frequency(self._octave, NOTE_INDEX_MAPPING[key.name])
                self.keyPressed.emit(float(f))
                #print(f"Emitted freq: {f}")
                break

    def get_piano_key_frequency(self, i_octave, key_number):
        return 2 ** (((12 * i_octave + key_number) - 49) / 12) * 440

