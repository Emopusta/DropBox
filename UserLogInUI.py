# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserLogInUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from sqlite3 import Cursor
import sys
from DropboxManager import DropboxManager
from User import User
from PyQt5 import QtCore, QtGui, QtWidgets
from UserManager import UserManager
from MainWindowUI import Ui_MainWindow
from EmopDataBase import *

class Ui_LogInWindow(object):
    user = User()
    def GetUser(self):
        return self.user

    def SendDataToMainWindow(self):#sends user information to mainwindow
        self.ui.user = self.user

    def SearchUser(self):

        cursor.execute(""" SELECT * FROM Users """)
        #not done yet 
        list_all = cursor.fetchall()
        print(list_all)
        


    def ClickedEnter(self):
        self.user = User(self.UserName.text(),self.Password.text())
        #userManager = UserManager()
        #dropboxManager = DropboxManager(user) 
        #print(userManager.PrintName(user))
        if self.user.userName == "Emre" :
            self.SearchUser()
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            self.ui.ListItemsToListView()
            self.SendDataToMainWindow()
            self.MainWindow.show()
            
            


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

