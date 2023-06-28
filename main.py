import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from getmail import GetCode


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 152)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(630, 152))
        MainWindow.setMaximumSize(QtCore.QSize(630, 152))
        MainWindow.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 630, 155))
        self.frame.setStyleSheet("background-color: rgb(44, 58, 71);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(5, 5, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(
            "background-color:rgb(73, 92, 108);\n"
            "color: #37ae85;\n"
            "border-radius: 10px;"
            )
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.Textline_mail = QtWidgets.QLineEdit(self.frame)
        self.Textline_mail.setGeometry(QtCore.QRect(205, 5, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Textline_mail.setFont(font)
        self.Textline_mail.setStyleSheet(
            "background-color: #2d5b57; \n"
            "color: #37ae85;\n"
            "border-radius: 10px;\n"
            "padding-left: 2px;\n"
            "padding-right: 2px;"
            )
        self.Textline_mail.setText("")
        self.Textline_mail.setObjectName("Textline_mail")
        self.Textline_mail.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(5, 55, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(
            "background-color:rgb(73, 92, 108);\n"
            "color: #37ae85;\n"
            "border-radius: 10px;"
            )
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.Textline_regular = QtWidgets.QLineEdit(self.frame)
        self.Textline_regular.setGeometry(QtCore.QRect(205, 55, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Textline_regular.setFont(font)
        self.Textline_regular.setStyleSheet(
            "background-color: #2d5b57; \n"
            "color: #37ae85;\n"
            "border-radius: 10px;\n"
            "padding-left: 2px;\n"
            "padding-right: 2px;"
            )
        self.Textline_regular.setText("")
        self.Textline_regular.setObjectName("Textline_regular")
        self.Textline_regular.setAlignment(QtCore.Qt.AlignCenter)
        self.Textline_code = QtWidgets.QPushButton(self.frame)
        self.Textline_code.setGeometry(QtCore.QRect(370, 105, 255, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Textline_code.setFont(font)
        self.Textline_code.setStyleSheet(
            "QPushButton {\n"
            "background-color: #2d5b57; \n"
            "color: #37ae85;\n"
            "border-radius: 10px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(47, 68, 44);\n"
            "    color: rgb(205, 205, 205);\n"
            "    border-style: outset;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.Textline_code.setText("...")
        self.Textline_code.setObjectName("Textline_code")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(5, 105, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(
            "background-color:rgb(73, 92, 108);\n"
            "color: #37ae85;\n"
            "border-radius: 10px;"
            )
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.Select_proxy_button = QtWidgets.QPushButton(self.frame)
        self.Select_proxy_button.setGeometry(QtCore.QRect(205, 105, 155, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Select_proxy_button.setFont(font)
        self.Select_proxy_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Select_proxy_button.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(60, 107, 67);\n"
            "    color: #37ae85;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(47, 68, 44);\n"
            "    color: rgb(205, 205, 205);\n"
            "    border-style: outset;\n"
            "    border-radius: 10px;\n"
            "}"
            )
        self.Select_proxy_button.setObjectName("Select_proxy_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Select_proxy_button.clicked.connect(self.get_code)
        self.Textline_code.clicked.connect(self.copy_code)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Get Mail Code Rambler"))
        self.label_3.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-size:14pt;\">Log:Pass почты:</span></p></body></html>"
                )
            )
        self.label_4.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-size:14pt;\">Регулярка:</span></p></body></html>"
                )
            )
        self.label_5.setText(
            _translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Код:</span></p></body></html>"
                )
            )
        self.Select_proxy_button.setText(_translate("MainWindow", "Получить"))

    def get_code(self):
        if self.Textline_mail.text() == "":
            self.Textline_code.setText("Введите почту")
            return
        if self.Textline_regular.text() == "":
            self.Textline_code.setText("Введите регулярку")
            return
        self.Textline_code.setText("Ожидайте")
        mail_data = self.Textline_mail.text()
        regular_string = self.Textline_regular.text()
        self.worker = GetCode(mail_data, regular_string)
        self.worker.send_code.connect(self.set_code)
        self.worker.start()

    def set_code(self, code):
        self.Textline_code.setText(code)

    def copy_code(self):
        code = self.Textline_code.text()
        pyperclip.copy(self.Textline_code.text())
        self.Textline_code.setEnabled(False)
        self.Textline_code.setText("Скопировано!")
        QTimer.singleShot(1000, lambda: self.Textline_code.setText(code))
        QTimer.singleShot(1000, lambda: self.Textline_code.setEnabled(True))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
