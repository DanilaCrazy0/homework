import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from game import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Крестики-нолики')
        self.radioButton_1.setChecked(True)
        self.label.hide()
        self.flag = True
        self.radioButton_1.clicked.connect(self.new_game)
        self.radioButton_2.clicked.connect(self.new_game)
        self.pushButton_10.clicked.connect(self.new_game)
        self.lst = [[self.pushButton_1, self.pushButton_2, self.pushButton_3],
                    [self.pushButton_4, self.pushButton_5, self.pushButton_6],
                    [self.pushButton_7, self.pushButton_8, self.pushButton_9]]
        self.lst1 = [self.pushButton_1, self.pushButton_2, self.pushButton_3,
                     self.pushButton_4, self.pushButton_5, self.pushButton_6,
                     self.pushButton_7, self.pushButton_8, self.pushButton_9]
        for obj in self.lst:
            for elem in obj:
                elem.clicked.connect(self.click)

    def new_game(self):
        for obj in self.lst:
            for elem in obj:
                elem.setEnabled(True)
                elem.setText('')
            if self.radioButton_1.isChecked():
                self.flag = True
            else:
                self.flag = False
            self.label.hide()

    def click(self):
        if self.flag:
            self.sender().setText('X')
            self.flag = False
        else:
            self.sender().setText('O')
            self.flag = True
        for i in range(3):
            for j in range(3):
                if all([self.lst[i][0].text(), self.lst[i][1].text(), self.lst[i][2].text()]):
                    if self.lst[i][0].text() == self.lst[i][1].text() == self.lst[i][2].text():
                        self.winner = self.lst[i][0].text()
                        self.win()
                elif all([self.lst[0][j].text(), self.lst[1][j].text(), self.lst[2][j].text()]):
                    if self.lst[0][j].text() == self.lst[1][j].text() == self.lst[2][j].text():
                        self.winner = self.lst[0][j].text()
                        self.win()
                elif all([self.lst[0][0].text(), self.lst[1][1].text(), self.lst[2][2].text()]):
                    if self.lst[0][0].text() == self.lst[1][1].text() == self.lst[2][2].text():
                        self.winner = self.lst[0][0].text()
                        self.win()
                elif all([self.lst[0][2].text(), self.lst[1][1].text(), self.lst[2][0].text()]):
                    if self.lst[0][2].text() == self.lst[1][1].text() == self.lst[2][0].text():
                        self.winner = self.lst[1][1].text()
                        self.win()
        lst_true = []
        for elem in self.lst1:
            lst_true.append(bool(elem.text()))
        if all(lst_true):
            for elem in self.lst1:
                elem.setEnabled(False)
            self.label.setText('Ничья!')
            self.label.show()



    def win(self):
        for elem in self.lst1:
            elem.setEnabled(False)
        self.label.setText(f'Выиграл {self.winner}!')
        self.label.show()

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