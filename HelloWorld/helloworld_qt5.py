import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt

# 创建一个 PyQt 应用程序
app = QApplication(sys.argv)

# 创建一个标签
label = QLabel()
# 给标签设置一个名为 "hello world" 的文本
label.setText('hello world')

# 设置标签内容居中
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
# 显示标签
label.show()

# 显示窗口控件，进入事件循环组
app.exec()
