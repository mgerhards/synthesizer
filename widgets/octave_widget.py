from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QStackedLayout
from PyQt6.QtCore import Qt, QPoint, QRect


class KeyWidget(QWidget):

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def clickHandler(self):
        print(self.name)

class OctaveWidget(QWidget):

    clickedValue = QtCore.pyqtSignal(int)

    def __init__(self, steps=5, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

    def _calculate_clicked_value(self, e):
        parent = self.parent()
        vmin, vmax = parent.minimum(), parent.maximum()
        d_height = self.size().height() + (self._padding * 2)
        step_size = d_height / self.n_steps
        click_y = e.y() - self._padding - step_size / 2

        pc = (d_height - click_y) / d_height
        value = vmin + pc * (vmax - vmin)
        self.clickedValue.emit(value)