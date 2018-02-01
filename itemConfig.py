# -*- coding: utf-8 -*-

"""
保存设置
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget
import sys
import Helper
from Helper import itemConf,generalConf,reloadConf

class Ui_ItemConfigWindow(QWidget):
    def setupUi(self):
        self.setObjectName("ItemConfigWindow")
        self.resize(908, 532)
        self.setMinimumSize(QtCore.QSize(908, 532))
        self.setMaximumSize(QtCore.QSize(908, 532))
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(740, 490, 145, 44))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.cancelBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        
        self.saveBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.saveBtn.setAutoDefault(False)
        self.saveBtn.setFlat(False)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout.addWidget(self.saveBtn)

        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(20, 60, 861, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(23, 80, 861, 413))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.remote_suffix_adr_debug = QtWidgets.QLineEdit(self.widget)
        self.remote_suffix_adr_debug.setText("")
        self.remote_suffix_adr_debug.setObjectName("remote_suffix_adr_debug")
        self.gridLayout.addWidget(self.remote_suffix_adr_debug, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.local_path_adr_release = QtWidgets.QLineEdit(self.widget)
        self.local_path_adr_release.setObjectName("local_path_adr_release")
        self.gridLayout.addWidget(self.local_path_adr_release, 9, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 10, 0, 1, 1)
        self.remote_suffix_ios_release = QtWidgets.QLineEdit(self.widget)
        self.remote_suffix_ios_release.setObjectName("remote_suffix_ios_release")
        self.gridLayout.addWidget(self.remote_suffix_ios_release, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.local_path_adr_debug = QtWidgets.QLineEdit(self.widget)
        self.local_path_adr_debug.setObjectName("local_path_adr_debug")
        self.gridLayout.addWidget(self.local_path_adr_debug, 7, 0, 1, 1)
        self.remote_suffix_adr_release = QtWidgets.QLineEdit(self.widget)
        self.remote_suffix_adr_release.setText("")
        self.remote_suffix_adr_release.setObjectName("remote_suffix_adr_release")
        self.gridLayout.addWidget(self.remote_suffix_adr_release, 7, 1, 1, 1)
        self.release_svn_game_data_path = QtWidgets.QLineEdit(self.widget)
        self.release_svn_game_data_path.setObjectName("release_svn_game_data_path")
        self.gridLayout.addWidget(self.release_svn_game_data_path, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 1, 1, 1)
        self.remote_suffix_ios_debug = QtWidgets.QLineEdit(self.widget)
        self.remote_suffix_ios_debug.setObjectName("remote_suffix_ios_debug")
        self.gridLayout.addWidget(self.remote_suffix_ios_debug, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 1, 1, 1)
        self.local_path_ios_release = QtWidgets.QLineEdit(self.widget)
        self.local_path_ios_release.setObjectName("local_path_ios_release")
        self.gridLayout.addWidget(self.local_path_ios_release, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)
        self.local_path_ios_debug = QtWidgets.QLineEdit(self.widget)
        self.local_path_ios_debug.setObjectName("local_path_ios_debug")
        self.gridLayout.addWidget(self.local_path_ios_debug, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 10, 1, 1, 1)
        self.remote_path_ios_debug = QtWidgets.QLineEdit(self.widget)
        self.remote_path_ios_debug.setObjectName("remote_path_ios_debug")
        self.gridLayout.addWidget(self.remote_path_ios_debug, 11, 0, 1, 1)
        self.remote_sftp_ip = QtWidgets.QLineEdit(self.widget)
        self.remote_sftp_ip.setObjectName("remote_sftp_ip")
        self.gridLayout.addWidget(self.remote_sftp_ip, 11, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 12, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 12, 1, 1, 1)
        self.remote_path_adr_debug = QtWidgets.QLineEdit(self.widget)
        self.remote_path_adr_debug.setObjectName("remote_path_adr_debug")
        self.gridLayout.addWidget(self.remote_path_adr_debug, 13, 0, 1, 1)
        self.remote_sftp_port = QtWidgets.QLineEdit(self.widget)
        self.remote_sftp_port.setText("")
        self.remote_sftp_port.setObjectName("remote_sftp_port")
        self.gridLayout.addWidget(self.remote_sftp_port, 13, 1, 1, 1)
        self.verChoose = QtWidgets.QComboBox(self.centralWidget)
        self.verChoose.setGeometry(QtCore.QRect(80, 20, 171, 26))
        self.verChoose.setObjectName("verChoose")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 52, 19))
        self.label.setObjectName("label")
        # self.setCentralWidget(self.centralWidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ItemConfigWindow", "版本设置"))
        self.label.setText(_translate("ItemConfigWindow", "选择版本"))
        self.label_2.setText(_translate("ItemConfigWindow", "SVN发布日志路径"))
        self.label_9.setText(_translate("ItemConfigWindow", "ios测试资源服脚本扩展名"))
        self.label_3.setText(_translate("ItemConfigWindow", "ios开发版路径"))
        self.label_10.setText(_translate("ItemConfigWindow", "adr测试资源服脚本扩展名"))
        self.label_4.setText(_translate("ItemConfigWindow", "ios发布版路径"))
        self.label_11.setText(_translate("ItemConfigWindow", "ios正式资源服脚本扩展名"))
        self.label_5.setText(_translate("ItemConfigWindow", "adr开发版路径"))
        self.label_12.setText(_translate("ItemConfigWindow", "adr正式资源服脚本扩展名"))
        self.label_6.setText(_translate("ItemConfigWindow", "adr发布版路径"))
        self.label_7.setText(_translate("ItemConfigWindow", "ios测试资源服路径"))
        self.label_13.setText(_translate("ItemConfigWindow", "测试资源服ip"))
        self.label_8.setText(_translate("ItemConfigWindow", "adr测试资源服路径"))
        self.label_14.setText(_translate("ItemConfigWindow", "测试资源服端口"))
        self.saveBtn.setText(_translate("ItemConfigWindow", "保存"))
        self.cancelBtn.setText(_translate("ItemConfigWindow", "取消"))

    def initUI(self):
        # self.center()
        self.show()

    def __init__(self):
        super(Ui_ItemConfigWindow, self).__init__()
        self.setupUi()
        self.retranslateUi()
        self.initData()
        self.initUI()

    def initData(self):
        itemList = itemConf.sections()
        self.verChoose.activated[str].connect(self.onChooseVer)
        for i in itemList:
            self.verChoose.addItem(i)
        print(itemList)
        self.onlyVerListIos = [self.local_path_ios_debug,self.release_svn_game_data_path,self.local_path_ios_release,self.remote_path_ios_debug,
            self.remote_suffix_ios_debug,self.remote_suffix_ios_release,self.remote_sftp_ip,self.remote_sftp_port]
        self.onlyVerListAdr = [self.local_path_adr_debug,self.release_svn_game_data_path,self.local_path_adr_release,self.remote_path_adr_debug,
            self.remote_suffix_adr_debug,self.remote_suffix_adr_release,self.remote_sftp_ip,self.remote_sftp_port]
        self.allLineEdit = [self.local_path_ios_debug,self.release_svn_game_data_path,self.local_path_ios_release,self.remote_path_ios_debug,
            self.remote_suffix_ios_debug,self.remote_suffix_ios_release,self.remote_sftp_ip,self.remote_sftp_port,self.local_path_adr_debug,
            self.local_path_adr_release,self.remote_path_adr_debug,self.remote_suffix_adr_debug,self.remote_suffix_adr_release]


        for i in self.allLineEdit:
            i.textEdited.connect(self.saveOption)

        lastVer = Helper.getLastConf()

        self.verChoose.setCurrentText(lastVer)
        self.onChooseVer(lastVer)
        self.saveBtn.clicked.connect(self.saveAndExit)
        self.cancelBtn.clicked.connect(self.noSaveAndExit)

        # print("a",self.onlyVerListIos)
        # print("b",self.onlyVerListAdr)
        # print("c",self.allLineEdit)
    def noSaveAndExit(self):
        reloadConf()
        self.close()


    def saveAndExit(self):
        Helper.saveOptions()
        self.close()

    def onChooseVer(self,text):
        for i in self.allLineEdit:
            # print(i)
            i.setReadOnly(True)
            i.setText("")
        try:
            onlyVer = itemConf.get(text,"onlyVer")
        except:
            onlyVer = None

        combined = False
        if itemConf.has_option(text,"combined"):
            combined = itemConf.getboolean(text,"combined")

        if onlyVer == None:
            print("onlyVer:",onlyVer)
            for i in self.allLineEdit:
                i.setReadOnly(False)
                i.setText(self.getOption(text,i.objectName()))
        else:
            if onlyVer == "adr":
                for i in self.onlyVerListAdr:
                    i.setReadOnly(False)
                    i.setText(self.getOption(text,i.objectName()))
            elif onlyVer == "ios":
                for i in self.onlyVerListIos:
                    i.setReadOnly(False)
                    i.setText(self.getOption(text,i.objectName()))
            else:
                for i in self.allLineEdit:
                    i.setReadOnly(False)
                    i.setText(self.getOption(text,i.objectName()))
        self.selectedVer = text
        Helper.setLastConf(text)

    def getOption(self,text,optName):
        try:
            return itemConf.get(text,optName)
        except Exception as e:
            return ""


    def saveOption(self):
        sender = self.sender()
        if len(sender.text()) > 0:
            itemConf.set(self.selectedVer,sender.objectName(),sender.text())
        else:
            try:
                itemConf.remove_option(self.selectedVer,sender.objectName())
            except:
                pass

   

        







if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ui_ItemConfigWindow()
    sys.exit(app.exec_())













