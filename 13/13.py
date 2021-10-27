import sys

from PyQt5.QtGui import QPainter

from square import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def xs(self, x):
        return x + 500

    def ys(self, y):
        return 500 - y

    def draw(self, qp):
        for i in range(0, int(self.lineEdit_3.text())):
            if i == 0:
                current_x = -int(self.lineEdit_1.text()) // 2
                current_y = -int(self.lineEdit_1.text()) // 2
            else:
                current_x = round(-int(self.lineEdit_1.text()) // 2 * float(self.lineEdit_2.text()) ** i)
                current_y = round(-int(self.lineEdit_1.text()) // 2 * float(self.lineEdit_2.text()) ** i)
                print(current_x, current_y)
            qp.drawLine(self.xs(current_x), self.ys(current_y), self.xs(current_x), self.ys(-current_y))
            qp.drawLine(self.xs(current_x), self.ys(-current_y), self.xs(-current_x), self.ys(-current_y))
            qp.drawLine(self.xs(-current_x), self.ys(-current_y), self.xs(-current_x), self.ys(current_y))
            qp.drawLine(self.xs(-current_x), self.ys(current_y), self.xs(current_x), self.ys(current_y))



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