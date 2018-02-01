# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import Qt,pyqtSlot,pyqtSignal,QThread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction
from PyQt5 import QtCore,QtWidgets
from itemConfig import Ui_ItemConfigWindow

import fastColuacoMain
import itemConfig
import Helper
from Helper import itemConf,getResPathByName
from generalSettingsL import GSettingsWin


class MainWindow(QMainWindow, fastColuacoMain.Ui_FastColuaco):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initData()

    def initData(self):
        itemList = itemConf.sections()
        self.verChoose.activated[str].connect(self.onChooseVer)
        for i in itemList:
            self.verChoose.addItem(i)
        lastVer = Helper.getLastConf()
        print(lastVer)
        self.verChoose.setCurrentText(lastVer)
        self.onChooseVer(lastVer)
        self.check_if_comb_release.stateChanged.connect(self.onReleaseCheck)
        
        self.log_window.setReadOnly(True)
        Helper.exportTxtObj = self

        self.processorThread=ProcessorThread(self) 
        self.processorThread.appendTextSignal.connect(self.appendTextSlot, Qt.QueuedConnection) 
        self.processorThread.setTextSignal.connect(self.setTextSlot, Qt.QueuedConnection) 
        self.processorThread.setProgressSignal.connect(self.updateProgress, Qt.QueuedConnection) 
        self.statusBar().showMessage('就绪')
        # self.btn_start.setCheckable(True)
        # 
        self.toolBar = QtWidgets.QToolBar(self)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        settingsAction = QAction(QIcon(getResPathByName('ver.png')), '版本设置', self)
        settingsAction.setShortcut('Ctrl+S')
        settingsAction.triggered.connect(self.openSettingsWin)
        self.toolBar.addAction(settingsAction)

        gSettingsAction = QAction(QIcon(getResPathByName('settings.png')), '基本设置', self)
        gSettingsAction.setShortcut('Ctrl+G')
        gSettingsAction.triggered.connect(self.OpenGSettingsWin)
        self.toolBar.addAction(gSettingsAction)

        self.btn_start.clicked.connect(self.processorThread.start)
        # self.startProcess()
        # 
    def OpenGSettingsWin(self):
        self.gSwin = GSettingsWin()

        # 
    def openSettingsWin(self):
        self.ex = Ui_ItemConfigWindow()

    @pyqtSlot(str)
    def updateProgress(self,text):
        if text == "start":
            print("setDown")
            self.btn_start.setEnabled(False)
            self.statusBar().showMessage('执行中')
        elif text == "end":
            print("endddddd")
            self.btn_start.setEnabled(True)
            self.statusBar().showMessage('就绪')
        else:
            self.statusBar().showMessage(text)

    @pyqtSlot(str) 
    def appendTextSlot(self, text): 
        self.log_window.append(text)

    @pyqtSlot(str) 
    def setTextSlot(self,text): 
        self.log_window.setText(text)

    def onReleaseCheck(self,status):
        if status == 2:
            self.check_if_upload.setCheckState(1)
            self.check_if_upload.setEnabled(False)
            self.check_if_comb.setCheckState(1)
            self.check_if_comb.setEnabled(False)
        else:
            self.check_if_upload.setCheckState(0)
            self.check_if_upload.setEnabled(True)
            self.check_if_comb.setCheckState(0)
            self.check_if_comb.setEnabled(True)


    def onChooseVer(self,text):
        self.selectedVer = text
        Helper.setLastConf(text)

    def startProcess(self):
        statusOk = True
        if self.check_if_down_data.checkState() == 2 and statusOk:
            statusOk = Helper.getFromSvn(self.selectedVer)
        if self.check_if_comb.checkState() == 2 and statusOk:
            statusOk = Helper.processCombine(self.selectedVer,False)
        if self.check_if_comb_release.checkState() == 2 and statusOk:
            statusOk = Helper.processCombine(self.selectedVer,True)
        if self.check_if_upload.checkState() == 2 and statusOk:
            statusOk = Helper.uploadFile(self.selectedVer)

        

class ProcessorThread(QThread): 
    appendTextSignal = pyqtSignal(str) 
    setTextSignal = pyqtSignal(str) 
    setProgressSignal = pyqtSignal(str) 

    def __init__(self,mainWin): 
        super(ProcessorThread,self).__init__()  
        self.mainWin = mainWin

    def run(self): 
        Helper.exportTxtSignal = self.appendTextSignal
        Helper.progressSignal = self.setProgressSignal
        self.setTextSignal.emit("")
        self.appendTextSignal.emit("操作开始")
        self.setProgressSignal.emit("start")
        self.mainWin.startProcess()  
        self.setProgressSignal.emit("end")
        self.appendTextSignal.emit("操作完成")
        self.quit()
        
        



if __name__ == '__main__':

    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())




