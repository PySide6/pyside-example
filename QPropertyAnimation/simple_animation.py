from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import QRect, QPropertyAnimation

if __name__ == "__main__":
    app = QApplication([])

    # 创建一个 QLabel 对象作为动画的目标
    label = QLabel("Hello, World!")
    label.show()

    # 创建一个 QPropertyAnimation 对象，指定动画的目标对象和属性
    animation = QPropertyAnimation(label, b"geometry")

    # 设置动画的起始值和结束值
    animation.setStartValue(QRect(100, 100, 100, 30))
    animation.setEndValue(QRect(200, 200, 200, 60))

    # 设置动画的持续时间
    animation.setDuration(1000)

    # 启动动画
    animation.start()

    app.exec()
