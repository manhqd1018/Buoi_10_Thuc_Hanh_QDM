import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
class ViDuGridLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ví dụ QGridLayout")
        self.resize(300, 200)
        layout = QGridLayout()
        layout.addWidget(QLabel("Họ tên: "), 0, 0)
        layout.addWidget(QLabel("Tuổi: "), 1, 0)
        layout.addWidget(QPushButton("Đồng ý"), 2, 0)
        layout.addWidget(QPushButton("Hủy"), 2, 1)
        self.setLayout(layout)
app = QApplication(sys.argv)
cua_so = ViDuGridLayout()
cua_so.show()
sys.exit(app.exec_())