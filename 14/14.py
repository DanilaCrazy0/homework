import sys

from PyQt5.QtGui import QPainter
from math import sin, cos, atan
from square2 import Ui_MainWindow
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
        current_x = -100
        current_y = -100
        for i in range(0, int(self.lineEdit_2.text())):
            k = float(self.lineEdit_1.text())
            if i == 0:
                qp.drawLine(self.xs(current_x), self.ys(current_y), self.xs(current_x), self.ys(-current_y))
                qp.drawLine(self.xs(current_x), self.ys(-current_y), self.xs(-current_x), self.ys(-current_y))
                qp.drawLine(self.xs(-current_x), self.ys(-current_y), self.xs(-current_x), self.ys(current_y))
                qp.drawLine(self.xs(-current_x), self.ys(current_y), self.xs(current_x), self.ys(current_y))
                lenght = ((2 * current_x * k) ** 2 + (2 * current_x * (1 - k)) ** 2) ** 0.5
                alpha = atan(k / (1 - k))
                new_x = current_x
                new_y = current_y + 2 * abs(current_y) * float(self.lineEdit_1.text())
            else:
                x_up = current_x + lenght * sin(i * alpha)
                y_up = current_y + lenght * cos(i * alpha)
                x_right = x_up + lenght * cos(i * alpha)
                y_right = y_up - lenght * sin(i * alpha)
                x_down = x_right - lenght * sin(i * alpha)
                y_down = y_right - lenght * cos(i * alpha)
                qp.drawLine(self.xs(current_x), self.ys(current_y), self.xs(x_up), self.ys(y_up))
                qp.drawLine(self.xs(x_up), self.ys(y_up), self.xs(x_right), self.ys(y_right))
                qp.drawLine(self.xs(x_right), self.ys(y_right), self.xs(x_down), self.ys(y_down))
                qp.drawLine(self.xs(x_down), self.ys(y_down), self.xs(current_x), self.ys(current_y))
                new_x = current_x + lenght * k * sin(i * alpha)
                new_y = current_y + lenght * k * cos(i * alpha)
                lenght = ((lenght * k) ** 2 + (lenght * (1-k)) ** 2) ** 0.5
            current_x, current_y = new_x, new_y



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