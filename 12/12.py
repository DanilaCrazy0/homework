import sys
from text_edit import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_create.clicked.connect(self.creates)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_open.clicked.connect(self.open)

    def creates(self):
        new_file = open(f'{self.lineEdit.text()}', 'w', encoding='utf8')
        new_file.close()

    def save(self):
        with open(f'{self.lineEdit.text()}', 'w', encoding='utf8') as f:
            f.write(self.textEdit.toPlainText())

    def open(self):
        with open(f'{self.lineEdit.text()}', 'r', encoding='utf8') as f:
            self.textEdit.setText(f.read())

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