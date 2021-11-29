import csv
import sys
from PyQt5.QtGui import QColor
from tablica import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable('rez.csv')
        schools = sorted(list(set(map(lambda x: x[0], self.info_lst))))
        schools.insert(0, 'Все')
        classes = sorted(list(set(map(lambda x: x[1], self.info_lst))))
        classes.insert(0, 'Все')
        self.comboBox_1.addItems(schools)
        self.comboBox_2.addItems(classes)
        self.pushButton.clicked.connect(self.search)
        self.comboBox_1.currentTextChanged.connect(self.change1)

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            self.reader = list(csv.reader(csvfile,
                                delimiter=',', quotechar='"'))
            del self.reader[0]
            self.reader = list(map(lambda x: [x[1], x[7], x[1]], self.reader))
            self.info_lst = list(map(lambda x: x[0].split(' '), self.reader))
            self.info_lst = list(map(lambda x: [x[1], x[2], x[3]], self.info_lst))
            self.reader = list(map(lambda x: [x[0][8:-2], x[1], x[2]], self.reader))
            for i in range(len(self.reader)):
                self.info_lst[i].append(self.reader[i][1])
                self.info_lst[i].append(self.reader[i][2])
            for i, row in enumerate(self.reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
            leaders = sorted(list(set(map(lambda x: int(x[3]), self.info_lst))), reverse=True)
            for i, row in enumerate(self.reader):
                for j in range(len(row)):
                    if int(self.tableWidget.item(i, 1).text()) == leaders[0]:
                        self.tableWidget.item(i, j).setBackground(QColor('yellow'))
                    elif int(self.tableWidget.item(i, 1).text()) == leaders[1]:
                        self.tableWidget.item(i, j).setBackground(QColor('gray'))
                    elif int(self.tableWidget.item(i, 1).text()) == leaders[2]:
                        self.tableWidget.item(i, j).setBackground(QColor('brown'))
        self.tableWidget.resizeColumnsToContents()

    def search(self):
        self.tableWidget.setRowCount(0)
        new_lst = []
        for i in range(len(self.info_lst)):
            if self.comboBox_1.currentText() == 'Все':
                if self.comboBox_2.currentText() == 'Все':
                    new_lst = self.reader
                    break
                else:
                    if self.info_lst[i][1] == self.comboBox_2.currentText():
                        new_lst.append([self.info_lst[i][2], self.info_lst[i][3], self.info_lst[i][4]])
            elif self.comboBox_2.currentText() == 'Все':
                if self.info_lst[i][0] == self.comboBox_1.currentText():
                    new_lst.append([self.info_lst[i][2], self.info_lst[i][3], self.info_lst[i][4]])
            elif self.info_lst[i][0] == self.comboBox_1.currentText() and self.info_lst[i][1] == self.comboBox_2.currentText():
                new_lst.append([self.info_lst[i][2], self.info_lst[i][3], self.info_lst[i][4]])
        print(new_lst)
        for i, row in enumerate(new_lst):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(elem))
        leaders = sorted(list(set(map(lambda x: int(x[1]), new_lst))), reverse=True)
        for i, row in enumerate(new_lst):
            for j in range(len(row)):
                if int(self.tableWidget.item(i, 1).text()) == leaders[0]:
                    self.tableWidget.item(i, j).setBackground(QColor('yellow'))
                elif int(self.tableWidget.item(i, 1).text()) == leaders[1]:
                    self.tableWidget.item(i, j).setBackground(QColor('gray'))
                elif int(self.tableWidget.item(i, 1).text()) == leaders[2]:
                    self.tableWidget.item(i, j).setBackground(QColor('brown'))



    def change1(self, text):
        if text == 'Все':
            self.comboBox_2.clear()
            classes = sorted(list(set(map(lambda x: x[1], self.info_lst))))
            classes.insert(0, 'Все')
            self.comboBox_2.addItems(classes)
        else:
            classes = sorted(list(set(map(lambda x: x[1], filter(lambda x: x[0] == text, self.info_lst)))))
            while self.comboBox_2.count() != 1:
                self.comboBox_2.removeItem(1)
            self.comboBox_2.addItems(classes)


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