import sys
from peremeshat import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.click)

    def click(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            lst = f.readlines()
            str_even = ''
            str_odd = ''
            for i in range(len(lst)):
                lst[i].strip()
                if i % 2 == 0:
                    str_even += lst[i]
                else:
                    str_odd += lst[i]
            self.textBrowser.setText(str_odd + '\n' + str_even)


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