# Form implementation generated from reading ui file 'account.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWindowAccount(object):
    def setupUi(self, mainWindowAccount):
        mainWindowAccount.setObjectName("mainWindowAccount")
        mainWindowAccount.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(mainWindowAccount)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listViewWallets = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewWallets.sizePolicy().hasHeightForWidth())
        self.listViewWallets.setSizePolicy(sizePolicy)
        self.listViewWallets.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.listViewWallets.setObjectName("listViewWallets")
        self.verticalLayout.addWidget(self.listViewWallets)
        self.pushButtonNew = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNew.setObjectName("pushButtonNew")
        self.verticalLayout.addWidget(self.pushButtonNew)
        self.pushButtonImport = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonImport.setObjectName("pushButtonImport")
        self.verticalLayout.addWidget(self.pushButtonImport)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        mainWindowAccount.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindowAccount)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 24))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        mainWindowAccount.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindowAccount)
        self.statusbar.setObjectName("statusbar")
        mainWindowAccount.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(mainWindowAccount)
        self.actionExit.setObjectName("actionExit")
        self.actionActivate = QtGui.QAction(mainWindowAccount)
        self.actionActivate.setObjectName("actionActivate")
        self.actionChangePassword = QtGui.QAction(mainWindowAccount)
        self.actionChangePassword.setObjectName("actionChangePassword")
        self.menuSettings.addAction(self.actionActivate)
        self.menuSettings.addAction(self.actionChangePassword)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(mainWindowAccount)
        QtCore.QMetaObject.connectSlotsByName(mainWindowAccount)

    def retranslateUi(self, mainWindowAccount):
        _translate = QtCore.QCoreApplication.translate
        mainWindowAccount.setWindowTitle(_translate("mainWindowAccount", "账户"))
        self.pushButtonNew.setText(_translate("mainWindowAccount", "新建钱包"))
        self.pushButtonImport.setText(_translate("mainWindowAccount", "导入钱包"))
        self.menuSettings.setTitle(_translate("mainWindowAccount", "设置"))
        self.actionExit.setText(_translate("mainWindowAccount", "退出"))
        self.actionExit.setShortcut(_translate("mainWindowAccount", "Ctrl+Q"))
        self.actionActivate.setText(_translate("mainWindowAccount", "激活"))
        self.actionChangePassword.setText(_translate("mainWindowAccount", "修改密码"))
