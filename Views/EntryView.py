# import sys
#
# from PyQt5 import QtCore
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
#
#
# class MyApp(object):
#
#     def SetupUI(self, mainWindow):
#         mainWindow.setWindowTitle("오픈마켓 업로더")
#         mainWindow.resize(1280, 720)
#
#         self.centralwidget = QWidget(mainWindow)
#
#         #self.Center()
#
#         # Code goes here ------------------------------------------
#         # exitAction = QAction('Exit', self)
#         # exitAction.setShortcut('Ctrl+Q')
#         # exitAction.setStatusTip('Exit application')
#         # exitAction.triggered.connect(qApp.quit)
#         #
#         # self.statusBar()
#         #
#         # menubar = self.menuBar()
#         # menubar.setNativeMenuBar(False)
#         # fileMenu = menubar.addMenu('&File')
#         # fileMenu.addAction(exitAction)
#         #
#         self.CreateAccountSelectionGB()
#         self.CreateMarketTypeGB()
#         self.CreateSalesStatusGB()
#
#         # ----------------------------------------------------------
#         #self.show()
#
#     def CreateAccountSelectionGB(self):
#         accountSelectionBox = QGroupBox(self.centralwidget)
#         _translate = QtCore.QCoreApplication.translate
#         accountSelectionBox.setTitle(_translate("MainWindow", "계정 선택"))
#
#         accountSelectionBox.setMinimumWidth(450)
#         accountSelectionBox.setMinimumHeight(100)
#         accountSelectionBox.setStyleSheet(
#             '''
#             QGroupBox
#             {
#                 subcontrol-origin: margin;
#                 subcontrol-position: top left;
#                 padding: 5 5px;
#                 font-size: 30px;
#                 font-weight: bold;
#                 minimum
#             }
#             '''
#         )
#         boxLayout = QBoxLayout(QBoxLayout.LeftToRight, parent=self.centralwidget)
#         accountSelectionBox.setLayout(boxLayout)
#
#         rbHyMedical = QRadioButton()
#         rbHyMedical.setStyleSheet(
#             '''
#             QRadioButton
#             {
#                 font: 9pt;
#                 width: 15px;
#                 height: 15px;
#             }
#             '''
#         )
#         rbHyMedical.setText("HY 메디칼")
#
#         rbMirae = QRadioButton()
#         rbMirae.setStyleSheet(
#             '''
#             QRadioButton
#             {
#                 font: 9pt;
#                 width: 15px;
#                 height: 15px;
#             }
#             '''
#         )
#         rbMirae.setEnabled(False)
#         rbMirae.setText("미래메디쿠스")
#
#         boxLayout.addWidget(rbHyMedical)
#         boxLayout.addWidget(rbMirae)
#
#         accountSelectionBox.move(25, 75)
#
#     def CreateMarketTypeGB(self):
#         marketType = QGroupBox("마켓 선택", self.centralwidget)
#
#         marketType.setMinimumWidth(450)
#         marketType.setMinimumHeight(250)
#         marketType.setStyleSheet(
#             '''
#             QGroupBox
#             {
#                 subcontrol-origin: margin;
#                 subcontrol-position: top left;
#                 padding: 5 5px;
#                 font-size: 30px;
#                 font-weight: bold;
#                 minimum
#             }
#             '''
#         )
#         boxLayout = QBoxLayout(QBoxLayout.TopToBottom, parent=self.centralwidget)
#         marketType.setLayout(boxLayout)
#
#         gmarket = QRadioButton()
#         gmarket.setStyleSheet(
#             '''
#             QRadioButton
#             {
#                 font: 9pt;
#                 width: 15px;
#                 height: 15px;
#             }
#             '''
#         )
#         gmarket.setText("ESM Plus")
#
#         eleventhSt = QRadioButton()
#         eleventhSt.setStyleSheet(
#             '''
#             QRadioButton
#             {
#                 font: 9pt;
#                 width: 15px;
#                 height: 15px;
#             }
#             '''
#         )
#         eleventhSt.setEnabled(False)
#         eleventhSt.setText("11번가")
#
#         smartStore = QRadioButton()
#         smartStore.setStyleSheet(
#             '''
#             QRadioButton
#             {
#                 font: 9pt;
#                 width: 15px;
#                 height: 15px;
#             }
#             '''
#         )
#         smartStore.setEnabled(False)
#         smartStore.setText("스마트 스토어")
#
#         boxLayout.addWidget(gmarket)
#         boxLayout.addWidget(eleventhSt)
#         boxLayout.addWidget(smartStore)
#
#         marketType.move(25, 200)
#
#     def CreateSalesStatusGB(self):
#         salesStatus = QGroupBox("판매 상태", self.centralwidget)
#
#         salesStatus.setMinimumWidth(450)
#         salesStatus.setMinimumHeight(175)
#         salesStatus.setStyleSheet(
#             '''
#             QGroupBox
#             {
#                 subcontrol-origin: margin;
#                 subcontrol-position: top left;
#                 padding: 5 5px;
#                 font-size: 30px;
#                 font-weight: bold;
#                 minimum
#             }
#             '''
#         )
#         boxLayout = QBoxLayout(QBoxLayout.TopToBottom, parent=self.centralwidget)
#         salesStatus.setLayout(boxLayout)
#
#         rbBeginSales = QRadioButton()
#         rbBeginSales.setStyleSheet(
#             '''
#             QRadioButton
#             {
#                 font: 9pt;
#                 width: 15px;
#                 height: 15px;
#             }
#             '''
#         )
#         rbBeginSales.setText("판매 시작")
#
#         rbPauseSales = QRadioButton()
#         rbPauseSales.setStyleSheet(
#             '''
#             QRadioButton
#             {
#                 font: 9pt;
#                 width: 15px;
#                 height: 15px;
#             }
#             '''
#         )
#         rbPauseSales.setChecked(True)
#         rbPauseSales.setText("판매 중지")
#
#         boxLayout.addWidget(rbBeginSales)
#         boxLayout.addWidget(rbPauseSales)
#
#         salesStatus.move(25, 475)
#
#     def ShowFileOpen(self):
#         fname = QFileDialog.getOpenFileName(self)
#         self.label.setText(fname[0])
#
#     def Center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainWindow = QMainWindow()
#     mainWindowUI = MyApp()
#     mainWindowUI.SetupUI(mainWindow)
#     mainWindow.show()
#
#     sys.exit(app.exec_())

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)
import sys

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

        if ok:
            self.le.setText(str(text))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())