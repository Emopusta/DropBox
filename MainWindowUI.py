# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUI2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from posixpath import split
from PyQt5 import QtCore, QtGui, QtWidgets
import dropbox as dropbox
from DropboxManager import DropboxManager
from User import User

class Ui_MainWindow(object):
    user = User()
    file = ""
    fileName = ""
    def ReturnFileNames(self,dbx):
        x = str(dbx.files_list_folder("")).split(",")
        listOfNames = []
        for i in x:
            if i.find("name=")==1:
                listOfNames.append(i)
        return listOfNames
    
    def ShowInListView(self,listOfNames):
        for i in listOfNames:
            self.listWidget.addItem(i)
    
    def ListItemsToListView(self):
        # we'll get these from database
        self.user = User("Emre","asd",oAuthKey="sl.BF_2p_WIZnmdW4MIWDb6yqSDCr-f7M1B0PGIyDyzNZ1OfuP6yDWnzx1F3cVAAD7sB0WN6P642bwPfEJ47THcBBfk1MhW-axNmueWMLcAL8bRhzCP3TMQpCH5iUXm6MSxT288jw69FHuF")
        dbx = dropbox.Dropbox(self.user.oAuthKey)
        listOfNames = self.ReturnFileNames(dbx)
        self.listWidget.clear()
        self.ShowInListView(listOfNames)


        
    def ChooseFileFromBrowser(self):
        fname = QtWidgets.QFileDialog.getOpenFileName()
        splitted = fname[0].split("/")
        self.label_2.setText(fname[0])
        self.file = fname[0]
        self.fileName = "/"+splitted[len(splitted)-1]
        print(self.file,self.fileName)
    
    def SendDataFunc(self):
        dbx = dropbox.Dropbox(self.user.oAuthKey)
        dbx.users_get_current_account()
        if self.file != "":
            with open(self.file,"rb") as f:
                dbx.files_upload(bytes(f.read()),self.fileName,mute = True)
            print("dosya gonderildi")
        else :
            print("dosya seciniz")

    
    def deneme(self):
        
        print(self.listWidget.currentItem().text())
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SendDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendDataButton.setGeometry(QtCore.QRect(680, 510, 91, 31))
        self.SendDataButton.setObjectName("SendDataButton")
        self.SendDataButton.clicked.connect(self.SendDataFunc)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 260, 131, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.AddUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddUserButton.setGeometry(QtCore.QRect(500, 290, 75, 23))
        self.AddUserButton.setObjectName("AddUserButton")
        self.AddUserButton.clicked.connect(self.deneme)
        self.UserChooserCBox = QtWidgets.QComboBox(self.centralwidget)
        self.UserChooserCBox.setGeometry(QtCore.QRect(640, 460, 131, 31))
        self.UserChooserCBox.setObjectName("UserChooserCBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 460, 61, 31))
        self.label.setObjectName("label")
        self.SelectFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.SelectFileButton.setGeometry(QtCore.QRect(670, 320, 101, 31))
        self.SelectFileButton.setObjectName("SelectFileButton")
        self.SelectFileButton.clicked.connect(self.ChooseFileFromBrowser)
        self.ShowFileDirectoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.ShowFileDirectoryLabel.setGeometry(QtCore.QRect(600, 370, 161, 21))
        self.ShowFileDirectoryLabel.setText("")
        self.ShowFileDirectoryLabel.setObjectName("ShowFileDirectoryLabel")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(610, 260, 171, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.UserRemover = QtWidgets.QPushButton(self.centralwidget)
        self.UserRemover.setGeometry(QtCore.QRect(660, 420, 111, 31))
        self.UserRemover.setObjectName("UserRemover")
        self.DeleteFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteFileButton.setGeometry(QtCore.QRect(440, 450, 121, 41))
        self.DeleteFileButton.setObjectName("DeleteFileButton")
        self.FileMarker = QtWidgets.QSpinBox(self.centralwidget)
        self.FileMarker.setGeometry(QtCore.QRect(470, 410, 51, 22))
        self.FileMarker.setObjectName("FileMarker")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 370, 121, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 500, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(460, 10, 301, 221))
        self.graphicsView.setObjectName("graphicsView")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 391, 481))
        self.listWidget.setObjectName("listWidget")
        
        self.RefreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshButton.setGeometry(QtCore.QRect(300, 500, 101, 31))
        self.RefreshButton.setObjectName("RefreshButton")
        self.RefreshButton.clicked.connect(self.ListItemsToListView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.SendDataButton.setText(_translate("MainWindow", "Gönder"))
        self.AddUserButton.setText(_translate("MainWindow", "Kullanici Ekle"))
        self.label.setText(_translate("MainWindow", " Kullanici adi"))
        self.SelectFileButton.setText(_translate("MainWindow", "Dosya Seç"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Göndermek istediğiniz dosyayı bilgisayarınızdan seçiniz</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.UserRemover.setText(_translate("MainWindow", "Seçilen kullanıcıyı sil"))
        self.DeleteFileButton.setText(_translate("MainWindow", "Seçilen Dosyayi Sil"))
        self.label_2.setText(_translate("MainWindow", "Dosya numarasi seçiniz"))
        self.pushButton.setText(_translate("MainWindow", "Seçilen Dosyayı İndir"))
        self.RefreshButton.setText(_translate("MainWindow", "Yenile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #ui.ListItemsToListView()
    MainWindow.show()
    
    sys.exit(app.exec_())
