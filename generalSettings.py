# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generalSettings.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_generalSettings(object):
    def setupUi(self, generalSettings):
        generalSettings.setObjectName("generalSettings")
        generalSettings.resize(604, 198)
        generalSettings.setMinimumSize(QtCore.QSize(604, 198))
        generalSettings.setMaximumSize(QtCore.QSize(604, 198))
        self.gridLayoutWidget = QtWidgets.QWidget(generalSettings)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 571, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.client_data_root = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.client_data_root.setMinimumSize(QtCore.QSize(439, 0))
        self.client_data_root.setMaximumSize(QtCore.QSize(439, 21))
        self.client_data_root.setObjectName("client_data_root")
        self.gridLayout_2.addWidget(self.client_data_root, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 3, 1, 1, 1)
        self.password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password.setMinimumSize(QtCore.QSize(439, 0))
        self.password.setMaximumSize(QtCore.QSize(439, 21))
        self.password.setObjectName("password")
        self.gridLayout_2.addWidget(self.password, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.user_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.user_name.setMinimumSize(QtCore.QSize(439, 0))
        self.user_name.setMaximumSize(QtCore.QSize(439, 21))
        self.user_name.setObjectName("user_name")
        self.gridLayout_2.addWidget(self.user_name, 1, 1, 1, 1)

        self.retranslateUi(generalSettings)
        self.buttonBox.accepted.connect(generalSettings.accept)
        self.buttonBox.rejected.connect(generalSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(generalSettings)

    def retranslateUi(self, generalSettings):
        _translate = QtCore.QCoreApplication.translate
        generalSettings.setWindowTitle(_translate("generalSettings", "基本设置"))
        self.label.setText(_translate("generalSettings", "SVN密码："))
        self.label_2.setText(_translate("generalSettings", "配置表SVN地址："))
        self.label_3.setText(_translate("generalSettings", "SVN用户名："))

