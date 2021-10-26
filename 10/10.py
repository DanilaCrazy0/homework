import sys
from consider import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.click)

    def click(self):
        try:
            open(f'{self.textEdit.text()}', 'r', encoding='utf-8')
        except FileNotFoundError:
            self.label_hide.setText(f'Файл {self.textEdit.text()} не найден')
        else:
            with open(f'{self.textEdit.text()}', 'r', encoding='utf-8') as f:
                lst = f.readlines()
                lst1 = lst[0].split(' ')
                try:
                    if len(lst) > 1:
                        raise BaseException
                    lst_numbers = list(map(lambda x: int(x), lst1))
                except BaseException:
                    self.label_hide.setText(f'Некорректный тип файла')
                else:
                    print(f.readlines())
                    self.textEdit_2.setText(f'{max(lst_numbers)}')
                    self.textEdit_3.setText(f'{min(lst_numbers)}')
                    self.textEdit_4.setText(f'{sum(lst_numbers) / len(lst_numbers)}')
                    with open('output.txt', 'w', encoding='utf-8') as file:
                        file.write(self.textEdit_2.text() + '\n')
                        file.write(self.textEdit_3.text() + '\n')
                        file.write(self.textEdit_4.text() + '\n')



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