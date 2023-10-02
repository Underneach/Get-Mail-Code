import re
import webbrowser
import sys

import pyperclip
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

from load_ui import Load_UI, resource_path
from getmail import GetCode
from setting import Save_settings


class User_UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.app_version = "2.0"
        Load_UI(self)

    def closeEvent(self, event) -> None:
        self.ui.setWindowTitle(f"GetCode {self.app_version} | rx580 LZT | Closing...")
        self.ui.close()
        event.accept()

    def Create_Regexp(self) -> None:
        print("create_regexp")
        webbrowser.open("https://bablosoft.github.io/RegexpConstructor/")

    def get_code(self) -> None:

        self.ui.Textline_mail.textChanged.connect(lambda: self.ui.Textline_code.setText("..."))
        self.ui.Textline_regular.currentTextChanged.connect(lambda: self.ui.Textline_code.setText("..."))
        self.ui.Textline_imap.currentTextChanged.connect(lambda: self.ui.Textline_code.setText("..."))

        if re.match(r".+@.+\:.+", self.ui.Textline_mail.text().strip()) is None:
            self.ui.Textline_code.setText("Неверный формат Log:Pass")
            return
        if re.match(r".+.+", str(self.ui.Textline_imap.currentText()).strip()) is None:
            self.ui.Textline_code.setText("Enter imap")
            return
        if len(str(self.ui.Textline_regular.currentText()).strip()) < 1:
            self.ui.Textline_code.setText("Enter RegExp")
            return

        try:
            split_string = self.ui.Textline_mail.text().strip().split(":")
            USERNAME = split_string[0]
            PASSWORD = split_string[1]
        except IndexError:
            self.ui.Textline_code.setText("Incorrect Log:Pass")
            return

        regular_string = str(self.ui.Textline_regular.currentText()).strip()
        IMAP_SERVER = str(self.ui.Textline_imap.currentText()).strip()

        Save_settings(self, regular_string, IMAP_SERVER)

        self.ui.Textline_code.setText("Ожидайте   ")
        self.ui.Textline_code.setEnabled(False)
        self.ui.setWindowTitle(f"GetCode {self.app_version} | rx580 LZT | Working...")
        self.ui.Textline_code.setStyleSheet('background-color: #214340;'
                                            'color: #247156;'
                                            'border-radius: 10px;'
                                            'padding-left: 4px;'
                                            'padding-right: 4px;')

        self.worker = GetCode(USERNAME, PASSWORD, IMAP_SERVER, regular_string)
        self.worker.send_code.connect(self.ui.setWindowTitle(f"GetCode {self.app_version} | rx580 LZT"))
        self.worker.send_code.connect(self.set_active)
        self.worker.send_code.connect(self.set_code)

        self.worker.start()

    def set_active(self) -> None:
        self.ui.Textline_code.setStyleSheet('background-color: #2d5b57;'
                                            'color: #37ae85;'
                                            'border-radius: 10px;'
                                            'padding-left: 4px;'
                                            'padding-right: 4px;')

    def set_code(self, code: str) -> None:
        self.ui.Textline_code.setText(code)
        self.ui.Textline_code.setEnabled(True)

    def copy_code(self) -> None:
        code = self.ui.Textline_code.text()
        pyperclip.copy(self.ui.Textline_code.text())

        self.ui.Textline_code.setEnabled(False)
        self.ui.Textline_code.setText("Copied")

        QTimer.singleShot(1000, lambda: self.ui.Textline_code.setText(code))
        QTimer.singleShot(1000, lambda: self.ui.Textline_code.setEnabled(True))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = User_UI()
    app.exec()
