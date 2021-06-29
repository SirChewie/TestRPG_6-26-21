from PyQt5 import QtWidgets, QtCore


class Ui_testRPG(object):

    def setupUi(self, testRPG):
        testRPG.setObjectName("testRPG")
        testRPG.resize(800, 600)

        self.centralWidget = QtWidgets.QWidget(testRPG)
        self.centralWidget.setObjectName("centralWidget")

    def retranslateUi(self, testRPG):
        _translate = QtCore.QCoreApplication.translate
        testRPG.setWindowTitle(_translate("testRPG", "Main Window"))
