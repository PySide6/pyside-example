import sys

from PySide6.QtGui import QPixmap, QIcon, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QLineEdit, \
    QTextEdit


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Normal Button')

        # 普通按钮
        self.button1 = QPushButton()
        self.button1.setText("按钮1")

        # 触发点击信号
        self.button2 = QPushButton()
        self.button2.setText('按钮2 clicked 信号')
        self.button2.clicked.connect(self.button2_click)

        # 图标+文字按钮
        self.button3 = QPushButton()
        self.button3.setIcon(QIcon(QPixmap('res/save_3.png')))
        self.button3.setText('图标按钮')

        # 存图标按钮
        self.button4 = QPushButton()
        self.button4.setIcon(QIcon(QPixmap('res/save_3.png')))

        # pressed 信号
        self.button5 = QPushButton()
        self.button5.setText("pressed信号")
        self.button5.pressed.connect(self.button5_pressed)

        # released 信号
        self.button6 = QPushButton()
        self.button6.setText('released信号')
        self.button6.released.connect(self.button6_released)

        # 凸起按钮
        self.button7 = QPushButton()
        self.button7.setFlat(True)
        self.button7.setText('平滑按钮，不显示外边框')

        main_widget = QWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        layout.addWidget(self.button7)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)

    def button2_click(self):
        """点击信号"""
        self.text_edit.setText(self.text_edit.toPlainText() + "\nclicked")

    def button5_pressed(self):
        """按下信号"""
        self.text_edit.setText(self.text_edit.toPlainText() + "\npressed")

    def button6_released(self):
        """释放信号"""
        self.text_edit.setText(self.text_edit.toPlainText() + "\nreleased")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
