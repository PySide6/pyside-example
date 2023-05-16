import sys

from PyQt5.QtGui import QColor
from PySide6.QtCore import QSize
from PySide6.QtGui import QPainter, QBrush
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QSizePolicy

"""
自定义圆形按钮
"""


class CircleButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        size = QSize(40, 40)
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # 设置按钮的样式
        self.setStyleSheet('''
                    QPushButton {
                        background-color: transparent;
                        border-style: none;
                        border-radius: 20px;
                        color: white;
                        font-size: 16px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: rgba(255, 255, 255, 0.2);
                    }
                    QPushButton:pressed {
                        background-color: rgba(0, 0, 0, 0.2);
                    }
                ''')

        def paintEvent(self, event):
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            brush = QBrush(QColor('#0078d7'))
            painter.setBrush(brush)
            painter.drawEllipse(self.rect())


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        button = CircleButton()
        button.setText('clicked me')
        self.setCentralWidget(button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
