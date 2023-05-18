from PySide6.QtWidgets import QApplication, QCheckBox
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve


class CustomCheckBox(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.animation = QPropertyAnimation(self, b"animationProgress")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.OutBack)
        self.animation.valueChanged.connect(self.update)

        self._animationProgress = 0.0
        self._animationColor = QColor(0, 150, 255)
        self._animationColor.setAlphaF(0.0)

        self.setContentsMargins(16, 16, 16, 16)

    def animationProgress(self):
        return self._animationProgress

    def setAnimationProgress(self, progress):
        self._animationProgress = progress
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        option = self.palette().button()

        # 绘制背景和边框
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(option.color)
        painter.drawRoundedRect(self.rect(), 5, 5)

        # 绘制勾选状态
        if self.isChecked():
            painter.setBrush(self._animationColor)
            painter.setPen(QPen(Qt.NoPen))
            painter.drawRoundedRect(self.rect(), 5, 5)

    def animateCheckState(self, checked):
        if checked:
            self.animation.setStartValue(0.0)
            self.animation.setEndValue(1.0)
        else:
            self.animation.setStartValue(1.0)
            self.animation.setEndValue(0.0)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication([])

    checkbox = CustomCheckBox()
    checkbox.setText("Check me")
    checkbox.setCheckable(True)
    checkbox.resize(200, 40)
    checkbox.show()

    app.exec()
