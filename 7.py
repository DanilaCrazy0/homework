import sys

from zakaz2 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click)
        self.plainTextEdit.setReadOnly(True)
        self.textEdit_1.setText('0')
        self.textEdit_1.setReadOnly(True)
        self.textEdit_2.setText('0')
        self.textEdit_2.setReadOnly(True)
        self.textEdit_3.setText('0')
        self.textEdit_3.setReadOnly(True)
        self.textEdit_4.setText('0')
        self.textEdit_4.setReadOnly(True)
        self.checkBox_1.clicked.connect(self.galochka)
        self.checkBox_2.clicked.connect(self.galochka)
        self.checkBox_3.clicked.connect(self.galochka)
        self.checkBox_4.clicked.connect(self.galochka)

    def galochka(self):
        if self.sender() == self.checkBox_1:
            self.textEdit_1.setReadOnly(False)
            self.textEdit_1.setText('1')
        if self.sender() == self.checkBox_2:
            self.textEdit_2.setReadOnly(False)
            self.textEdit_2.setText('1')
        if self.sender() == self.checkBox_3:
            self.textEdit_3.setReadOnly(False)
            self.textEdit_3.setText('1')
        if self.sender() == self.checkBox_4:
            self.textEdit_4.setReadOnly(False)
            self.textEdit_4.setText('1')

    def click(self):
        self.plainTextEdit.setPlainText("Ваш заказ:")
        self.plainTextEdit.appendPlainText('')
        if self.checkBox_1.isChecked():
            self.plainTextEdit.appendPlainText(str(self.checkBox_1.text() + '-----' + self.textEdit_1.text() + '-----' +
                                                   str(int(self.textEdit_1.text()) * 10)))
        if self.checkBox_2.isChecked():
            self.plainTextEdit.appendPlainText(str(self.checkBox_2.text() + '-----' + self.textEdit_2.text() + '-----' +
                                                   str(int(self.textEdit_2.text()) * 12)))
        if self.checkBox_3.isChecked():
            self.plainTextEdit.appendPlainText(str(self.checkBox_3.text() + '-----' + self.textEdit_3.text() + '-----' +
                                                   str(int(self.textEdit_3.text()) * 15)))
        if self.checkBox_4.isChecked():
            self.plainTextEdit.appendPlainText(str(self.checkBox_4.text() + '-----' + self.textEdit_4.text() + '-----' +
                                                   str(int(self.textEdit_4.text()) * 30)))
        self.plainTextEdit.appendPlainText('')
        self.plainTextEdit.appendPlainText('Итого: ' + str(int(self.textEdit_1.text()) * 10 + int(self.textEdit_2.text()) * 12 +
                                           + int(self.textEdit_3.text()) * 15 + int(self.textEdit_4.text()) * 30))



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