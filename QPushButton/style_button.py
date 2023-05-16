import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QMainWindow, QWidget

qssStyle = """
    QPushButton {
        font-size: 18px;
        color: #eeeeee;
    }
    
    QPushButton#button1 {
        background-color: pure;
    }
    
    QPushButton#button2 {
        background-color: red;
        border-radius: 4px;
    }
    
    QPushButton#button3 {
        background-color: green;
        border-radius: 30px;
    }
    
    QPushButton#button4 {
        background-color: blue;
        border-top-left-radius: 8px;
        border-bottom-right-radius: 8px;
    }
    
    QPushButton#button5 {
        background-color: orange;
        border: 1px solid #cccccc;
        padding-top: 8px;
        padding-bottom: 8px;
        border-radius: 4px;
    }

"""


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('带样式的Button')
        layout = QVBoxLayout(self)

        button1 = QPushButton("")
        button1.setObjectName("button1")
        button1.setText('普通按钮')

        button2 = QPushButton()
        button2.setText('圆角按钮')
        button2.setObjectName('button2')

        button3 = QPushButton()
        button3.setText('圆形按钮')
        button3.setObjectName('button3')
        # 设置样式为宽高的一半，即可组圆形按钮
        button3.setMaximumSize(60, 60)
        button3.setMinimumSize(60, 60)

        button4 = QPushButton()
        button4.setText('蓝色按钮')
        button4.setObjectName('button4')

        button5 = QPushButton()
        button5.setText('橙色按钮')
        button5.setObjectName('button5')

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        main_widget = QWidget(self)
        main_widget.setLayout(layout)

        self.setStyleSheet(qssStyle)
        self.setCentralWidget(main_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec())
