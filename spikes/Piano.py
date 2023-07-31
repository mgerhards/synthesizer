import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt, QPoint, QRect

class ImageMapWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = QPixmap("assets\Piano_Keyboard.jpg")  # Replace "your_image_path.png" with the actual image path

        self.image_map = {
            "region1": QRect(100, 50, 200, 100),
            "region2": QRect(250, 180, 100, 150),
            # Define more regions as needed
        }

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

    def mousePressEvent(self, event):
        for region, rect in self.image_map.items():
            if rect.contains(event.pos()):
                print(f"Clicked on {region}")
                # Add your action for this region here
                break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    image_map_widget = ImageMapWidget()
    image_map_widget.resize(400, 300)
    image_map_widget.show()
    sys.exit(app.exec())