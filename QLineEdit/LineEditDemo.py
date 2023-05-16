import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, \
    QTextEdit


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        self.line_edit = QLineEdit()
        # 提示
        self.line_edit.setPlaceholderText('请输入内容')
        # 监听文本改变信号
        self.line_edit.textChanged.connect(self.line_edit_changed)
        # 回车触发
        self.line_edit.returnPressed.connect(self.line_edit_returnPressed)



        tool_layout = QHBoxLayout()

        self.button = QPushButton('设置值')
        self.button.clicked.connect(self.button_click)
        self.button2 = QPushButton('获取值')
        self.button2.clicked.connect(self.button2_click)

        self.button3 = QPushButton('清空值')
        self.button3.clicked.connect(self.button3_click)
        self.button4 = QPushButton('利用QLineEdit clear信号清空')
        self.button4.clicked.connect(self.line_edit.clear)

        tool_layout.addWidget(self.button)
        tool_layout.addWidget(self.button2)
        tool_layout.addWidget(self.button3)
        tool_layout.addWidget(self.button4)

        self.display = QTextEdit()

        main_layout.addWidget(self.line_edit)
        main_layout.addLayout(tool_layout)
        main_layout.addWidget(self.display)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

    def button_click(self):
        self.line_edit.setText('hello world')

    def button2_click(self):
        self.display.setText(self.line_edit.text())

    def button3_click(self):
        self.line_edit.clear()

    def line_edit_changed(self, text):
        self.display.setText(text)

    def line_edit_returnPressed(self):
        self.display.setText('回车')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
