import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('qlabel 展示图片')
        self.image_label = QLabel(self)
        self.image_label.setText('展示图片')
        self.image_label.setPixmap(QPixmap('res/image.png'))

        # self.image_label = QLabel(QIcon(QPixmap('res/image.png')), self)


def main():
    app = QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())




if __name__ == '__main__':
    main()


