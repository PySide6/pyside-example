import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel('hello world')
label.show()

sys.exit(app.exec())
