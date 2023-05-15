import sys

from PySide6.QtGui import QPixmap, QIcon, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QWidget, QVBoxLayout


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Button')

        button1 = QPushButton()
        button1.setText("按钮1")

        self.button2 = QPushButton()
        self.button2.setText('按钮2')

        self.button2.clicked.connect(self.button2_click)

        self.button3 = QPushButton()
        self.button3.setIcon(QIcon(QPixmap('res/save_3.png')))
        self.button3.setText('图标按钮')

        self.button4 = QPushButton()
        self.button4.setIcon(QIcon(QPixmap('res/save_3.png')))

        main_widget = QWidget()

        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)

    def button2_click(self):
        self.button2.setText('点击')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
