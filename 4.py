import sys

from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QApplication


morse_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
}


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Азбука Морзе 2')
        self.setGeometry(800, 100, 800, 100)
        self.wndw = QLineEdit(self)
        self.wndw.setGeometry(600, 50, 600, 50)
        self.wndw.move(0, 45)
        a = 0
        self.btn_lst = []
        for key, i in zip(morse_dict, range(1, 28)):
            btn = QPushButton(self)
            btn.setText(key)
            btn.setGeometry(30, 30, 30, 30)
            btn.move(a, 0)
            btn.clicked.connect(self.click)
            self.btn_lst.append(btn)
            a += 30

    def click(self):
        self.wndw.setText(self.wndw.text() + morse_dict[self.sender().text()])


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())