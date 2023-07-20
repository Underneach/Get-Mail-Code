import os
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QTimer
from getmail import GetCode


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("getmail.ui", self)

        self.load_settings()

        self.Pushbutton.clicked.connect(self.get_code)
        self.Textline_code.clicked.connect(self.copy_code)

    def get_code(self):

        self.save_settings()

        if self.Textline_mail.text() == "":
            self.Textline_code.setText("Введите почту")
            return
        if self.Textline_regular.text() == "":
            self.Textline_code.setText("Введите регулярку")
            return
        if self.Textline_imap.text() == "":
            self.Textline_code.setText("Введите imap")
            return

        try:
            split_string = self.Textline_mail.text().split(":")
            USERNAME = split_string[0]
            PASSWORD = split_string[1]
        except IndexError:
            self.Textline_code.setText("Неверные данные")
            return

        regular_string = self.Textline_regular.text()
        IMAP_SERVER = self.Textline_imap.text()

        self.Textline_code.setText("Ожидайте")
        self.Textline_code.setEnabled(False)

        self.worker = GetCode(USERNAME, PASSWORD, IMAP_SERVER, regular_string)
        self.worker.send_code.connect(self.set_code)
        self.worker.start()

    def save_settings(self):
        path = os.getenv('APPDATA')
        with open(path + '\\settings.txt', 'w') as f:
            f.write(self.Textline_regular.text() + '\n')
            f.write(self.Textline_imap.text() + '\n')

    def load_settings(self):
        try:
            path = os.getenv('APPDATA')
            with open(path + '\\settings.txt', 'r') as f:
                self.Textline_regular.setText(f.readline()[:-1])
                self.Textline_imap.setText(f.readline()[:-1])
        except FileNotFoundError:
            pass

    def set_code(self, code):
        self.Textline_code.setEnabled(True)
        self.Textline_code.setText(code)

    def copy_code(self):
        code = self.Textline_code.text()
        pyperclip.copy(self.Textline_code.text())
        self.Textline_code.setEnabled(False)
        self.Textline_code.setText("Скопировано!")
        QTimer.singleShot(1000, lambda: self.Textline_code.setText(code))
        QTimer.singleShot(1000, lambda: self.Textline_code.setEnabled(True))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.setWindowFlags(Qt.WindowStaysOnTopHint)
    window.show()
    app.exec_()
