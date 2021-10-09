import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLineEdit, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 400, 200)
        self.setWindowTitle('Арифмометр')
        self.wndw1 = QLineEdit(self)
        self.wndw1.setGeometry(60, 30, 60, 30)
        self.wndw1.move(10, 0)
        self.wndw2 = QLineEdit(self)
        self.wndw2.setGeometry(60, 30, 60, 30)
        self.wndw2.move(160, 0)
        self.btn1 = QPushButton(self)
        self.btn1.setText('+')
        self.btn1.setGeometry(30, 30, 30, 30)
        self.btn1.move(70, 0)
        self.btn1.clicked.connect(self.click1)
        self.btn2 = QPushButton(self)
        self.btn2.setText('-')
        self.btn2.setGeometry(30, 30, 30, 30)
        self.btn2.move(100, 0)
        self.btn2.clicked.connect(self.click2)
        self.btn3 = QPushButton(self)
        self.btn3.setText('*')
        self.btn3.setGeometry(30, 30, 30, 30)
        self.btn3.move(130, 0)
        self.btn3.clicked.connect(self.click3)
        self.lbl = QLabel(self)
        self.lbl.move(225, 0)
        self.lbl.setText('=')
        self.wndw3 = QLineEdit(self)
        self.wndw3.setGeometry(60, 30, 60, 30)
        self.wndw3.move(235, 0)
        self.wndw3.setReadOnly(True)

    def click1(self):
        self.wndw3.setText(f"{int(self.wndw1.text()) + int(self.wndw2.text())}")

    def click2(self):
        self.wndw3.setText(f'{int(self.wndw1.text()) - int(self.wndw2.text())}')

    def click3(self):
        self.wndw3.setText(f'{int(self.wndw1.text()) * int(self.wndw2.text())}')


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())