# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserLogInUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from User import User
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def ClickedEnter(self):
        user = User(self.UserName.text(),self.Password.text(),self.AuthKey.text())
        user.PrintName()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 182)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UserNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.UserNameLabel.setGeometry(QtCore.QRect(30, 20, 81, 21))
        self.UserNameLabel.setObjectName("UserNameLabel")
        self.UserName = QtWidgets.QLineEdit(self.centralwidget)
        self.UserName.setGeometry(QtCore.QRect(110, 20, 113, 20))
        self.UserName.setObjectName("UserName")
        self.PasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.PasswordLabel.setGeometry(QtCore.QRect(30, 50, 61, 16))
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.Password.setObjectName("Password")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(250, 110, 75, 23))
        self.Enter.setObjectName("Enter")
        self.Enter.clicked.connect(self.ClickedEnter)
        self.AuthKeyLabel = QtWidgets.QLabel(self.centralwidget)
        self.AuthKeyLabel.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.AuthKeyLabel.setObjectName("AuthKeyLabel")
        self.AuthKey = QtWidgets.QLineEdit(self.centralwidget)
        self.AuthKey.setGeometry(QtCore.QRect(110, 80, 221, 20))
        self.AuthKey.setObjectName("AuthKey")
        self.Register = QtWidgets.QPushButton(self.centralwidget)
        self.Register.setGeometry(QtCore.QRect(160, 110, 75, 23))
        self.Register.setObjectName("Register")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 356, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.UserNameLabel.setText(_translate("MainWindow", "Kullanici Adi"))
        self.PasswordLabel.setText(_translate("MainWindow", "     Sifre"))
        self.Enter.setText(_translate("MainWindow", "Giris"))
        self.AuthKeyLabel.setText(_translate("MainWindow", "Auth Key"))
        self.Register.setText(_translate("MainWindow", "Kayit Ol"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
