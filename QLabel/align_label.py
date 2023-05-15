import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *



app = QApplication()
label = QLabel(parent=None)
label.setText('first label')
label.setSelection(1, 4)
print(label.selectedText())
# 文本居中显示
label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
label.setWordWrap(True)
label.show()

sys.exit(app.exec())
