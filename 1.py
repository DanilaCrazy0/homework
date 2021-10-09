import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLineEdit



class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(230, 30, 230, 30)
        self.setWindowTitle('Фокус со словами')
        self.btn = QPushButton(self)
        self.btn.setText("->")
        self.btn.setGeometry(30, 30, 30, 30)
        self.btn.move(100, 0)
        self.btn.clicked.connect(self.click)
        self.wndw1 = QLineEdit(self)
        self.wndw2 = QLineEdit(self)
        self.wndw2.move(130, 0)

    def click(self):
        if self.btn.text() == '->':
            self.btn.setText("<-")
        else:
            self.btn.setText("->")
        if self.wndw1.text():
            self.wndw2.setText(self.wndw1.text())
            self.wndw1.setText('')
        else:
            self.wndw1.setText(self.wndw2.text())
            self.wndw2.setText('')

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())