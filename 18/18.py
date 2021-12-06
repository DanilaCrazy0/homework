import sys
import csv
from random import randint

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from titanic_table import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable('titanic.csv')
        self.paint()
        self.lineEdit.textEdited.connect(self.search)

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            self.reader = list(csv.reader(csvfile,
                                delimiter=',', quotechar='"'))
            title = self.reader[0]
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(self.reader[1:]):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        print(self.reader)
        self.tableWidget.resizeColumnsToContents()

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)

    def paint(self):
        for i in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(i, 5).text() == '0':
                self.color_row(i, QColor('red'))
            else:
                self.color_row(i, QColor('Green'))

    def search(self, text):
        if len(text) <= 3:
            for i, row in enumerate(self.reader[1:]):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
                if self.tableWidget.item(i, 5).text() == '0':
                    self.color_row(i, QColor('red'))
                elif self.tableWidget.item(i, 5).text() == '1':
                    self.color_row(i, QColor('green'))
        else:
            new_lst = []
            for elem in self.reader:
                if text.lower() in elem[1].lower():
                    new_lst.append(elem)
            self.tableWidget.clear()
            for i, row in enumerate(new_lst):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
                if self.tableWidget.item(i, 5).text() == '0':
                    self.color_row(i, QColor('red'))
                elif self.tableWidget.item(i, 5).text() == '1':
                    self.color_row(i, QColor('green'))



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