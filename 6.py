import sys

from zakaz import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QCheckBox, QPlainTextEdit, QApplication


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click)
        self.plainTextEdit.setReadOnly(True)


    def click(self):
        self.plainTextEdit.setPlainText("Ваш заказ:")
        self.plainTextEdit.appendPlainText('')
        if self.checkBox_1.isChecked():
            self.plainTextEdit.appendPlainText(self.checkBox_1.text())
        if self.checkBox_2.isChecked():
            self.plainTextEdit.appendPlainText(self.checkBox_2.text())
        if self.checkBox_3.isChecked():
            self.plainTextEdit.appendPlainText(self.checkBox_3.text())
        if self.checkBox_4.isChecked():
            self.plainTextEdit.appendPlainText(self.checkBox_4.text())



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