from UserManager import *
from UserLogInUI import Ui_LogInWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Program:

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        LogInWindow = QtWidgets.QMainWindow()
        ui = Ui_LogInWindow()
        ui.setupUi(LogInWindow)
        LogInWindow.show()
        sys.exit(app.exec_())
        #asdasd
            

x = Program()