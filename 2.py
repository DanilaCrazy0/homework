import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLineEdit, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 400, 200)
        self.setWindowTitle('Прятки для виджетов')
        self.checkmark1 = QCheckBox(self)
        self.checkmark1.setText('edit1')
        self.checkmark1.move(20, 0)
        self.checkmark1.clicked.connect(self.click)
        self.wndw1 = QLineEdit(self)
        self.wndw1.setText('Поле edit1')
        self.wndw1.move(70, 0)
        self.checkmark2 = QCheckBox(self)
        self.checkmark2.setText('edit2')
        self.checkmark2.move(20, 40)
        self.wndw2 = QLineEdit(self)
        self.wndw2.setText('Поле edit2')
        self.wndw2.move(70, 40)
        self.checkmark3 = QCheckBox(self)
        self.checkmark3.setText('edit3')
        self.checkmark3.move(20, 80)
        self.wndw3 = QLineEdit(self)
        self.wndw3.setText('Поле edit3')
        self.wndw3.move(70, 80)
        self.checkmark4 = QCheckBox(self)
        self.checkmark4.setText('edit4')
        self.checkmark4.move(20, 120)
        self.checkmark2.clicked.connect(self.click)
        self.checkmark3.clicked.connect(self.click)
        self.checkmark4.clicked.connect(self.click)

        self.wndw4 = QLineEdit(self)
        self.wndw4.setText('Поле edit4')
        self.wndw4.move(70, 120)

    def click(self):
        if self.checkmark1.isChecked():
            self.wndw1.show()
        else:
            self.wndw1.hide()
        if self.checkmark2.isChecked():
            self.wndw2.show()
        else:
            self.wndw2.hide()
        if self.checkmark3.isChecked():
            self.wndw3.show()
        else:
            self.wndw3.hide()
        if self.checkmark4.isChecked():
            self.wndw4.show()
        else:
            self.wndw4.hide()


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