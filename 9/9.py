import sys
from lukomorie import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            lst = f.readlines()
            i = randint(0, len(lst) - 1)
            self.textBrowser.setText(lst[i])



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