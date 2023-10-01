import sys
import os

from PySide6 import QtGui, QtUiTools, QtCore

from setting import Load_settings


def resource_path(relative_path) -> str:
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


def Load_UI(self) -> None:
    self.ui = QtUiTools.QUiLoader().load(resource_path("res/gui.ui"), self)
    self.ui.setWindowIcon(QtGui.QIcon(resource_path('res/icon.ico')))
    self.ui.setWindowTitle(f"GetCode {self.app_version} | rx580 LZT")
    self.ui.setWindowFlags(self.ui.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

    add_regexp_list_icon = resource_path('res/plus.png').replace("\\", "/")

    # установка иконок
    self.ui.add_regexp.setStyleSheet("QPushButton {"
                                     "background-color: #22664e;"
                                     f"image: url({add_regexp_list_icon});"
                                     "color: #2d8a6a;"
                                     "border-radius: 10px;"
                                     "padding-left: 8px;"
                                     "padding-right: 8px;"
                                     "             }"

                                     "QPushButton:pressed {"
                                     "	background-color: rgb(47, 68, 44);"
                                     "    color: rgb(205, 205, 205);"
                                     "    border-style: outset;"
                                     "    border-radius: 10px;"
                                     "             }")

    self.ui.Get_Code.clicked.connect(self.get_code)
    self.ui.Textline_code.clicked.connect(self.copy_code)
    self.ui.add_regexp.clicked.connect(self.Create_Regexp)

    Load_settings(self)

    self.ui.show()
