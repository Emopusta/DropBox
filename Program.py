from UserManager import *
from UserLogInUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class Program:

    def __init__(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
            

x = Program()