# -*- coding: utf-8 -*-

from generalSettings import Ui_generalSettings

from PyQt5.QtWidgets import QDialog

from Helper import generalConf,saveOptions,reloadConf


class GSettingsWin(QDialog, Ui_generalSettings):
    def __init__(self):
        super(GSettingsWin, self).__init__()
        self.setupUi(self)
        self.initData()
        self.show()

    def initData(self):
        self.client_data_root.setText(generalConf.get("svn_settings","client_data_root"))
        self.user_name.setText(generalConf.get("svn_settings","user_name"))
        self.password.setText(generalConf.get("svn_settings","password"))
        self.client_data_root.textEdited.connect(self.saveOption)
        self.user_name.textEdited.connect(self.saveOption)
        self.password.textEdited.connect(self.saveOption)


    def accept(self):
    	print("accept")
    	saveOptions()
    	super().accept()

    def reject(self):
    	print("reject")
    	reloadConf()
    	super().reject()

    def saveOption(self):
        sender = self.sender()
        if len(sender.text()) > 0:
            generalConf.set("svn_settings",sender.objectName(),sender.text())
        else:
            generalConf.set("svn_settings",sender.objectName(),"")
