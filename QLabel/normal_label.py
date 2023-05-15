import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

app = QApplication()
label = QLabel(parent=None)
label.setText('first label')
# 文本居中显示
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
label.show()

sys.exit(app.exec())
