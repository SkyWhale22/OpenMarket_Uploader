# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Global import SingletonInstance, BaseClass
from Views.UI_ItemUploader import UiUploader, Widget_1, Widget_2, Widget_3
from Views.UI_ExcelFileGenerator import UiExcelFormatGenerator
from Global import GetResHeight, GetResWidth
from Log import Log


class WindowController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("엑셀 일괄 업로드")
        self.resize(GetResWidth(), GetResHeight())

        #self.generateExcel = UiExcelFormatGenerator(self, self.m_centralwidget)
        self.MakeToolBar()

        self.m_centralwidget = QWidget(self)
        widget_layout = QBoxLayout(QBoxLayout.LeftToRight, self.m_centralwidget)
        widget_layout.setGeometry(QRect(0, 0, GetResWidth(), GetResHeight()))
        self.m_centralwidget.setObjectName("centralwidget")
        self.m_upload = UiUploader(self.m_centralwidget)
        self.setCentralWidget(self.m_centralwidget)

    def Display(self, i):
        self.stack.setCurrentIndex(i)
    def Show(self):
        self.show()

    # ======================================================================================================
    # Tool bar
    # ======================================================================================================
    def MakeToolBar(self):
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 1280, 100))
        self.menubar.setObjectName("menubar")

        upload = QAction("파일 업로드", self)
        upload.setShortcut("Ctrl+1")
        upload.triggered.connect(self.ChangeLayoutToUploader)

        generateXlsx = QAction("엑셀 양식 생성", self)
        generateXlsx.setShortcut("Ctrl+2")
        generateXlsx.triggered.connect(self.ChangeLayoutToExcelMaker)

        self.menu = QMenu(self.menubar)
        self.menu.setObjectName("&Menu")
        self.menu.addAction(upload)
        self.menu.addAction(generateXlsx)

        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.RetranslateUi()
        QMetaObject.connectSlotsByName(self)

    def RetranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # --------------------------------------------------------------------------------------------------
        self.menu.setTitle(_translate("MainWindow", "메뉴"))

    def ChangeLayoutToUploader(self):
        self.Display(0)
        Log.Getinstance().AddMessage("Test1.")
        self.generateExcel.setHidden(True)
        self.m_upload.setHidden(False)

    def ChangeLayoutToExcelMaker(self):
        self.Display(1)
        Log.Getinstance().AddMessage("Test2.")
        self.generateExcel.setHidden(False)
        self.m_upload.setHidden(True)


    def ShowDialog(self, textLine):
        # Get file's directory in string
        fname = QFileDialog.getOpenFileName(self.m_centralWidget, 'Open file', './')

        # Check file's existence
        if(fname[0]):
            # Check file's extension
            extension = fname[0][len(fname[0]) - 5:]
            if (extension == ".xlsm" or extension == ".xlsx"):
                textLine.setText(fname[0])
                Log.Getinstance().AddMessage(fname[0] + " 파일이 선택되었습니다.")
            else:
                reply = QMessageBox.question(self.m_centralWidget, 'Message', '엑셀 파일이 아닙니다.',
                                             QMessageBox.Yes)
                Log.Getinstance().AddMessageWithColor("엑셀 파일이 아닙니다.", QColor(255, 0, 0))


if __name__ == "__main__":
    m_app = QApplication(sys.argv)

    ctrl = WindowController()
    ctrl.Show()
    sys.exit(m_app.exec_())

    # ui = UiMainWindow()
    # ui.SetupUi(mainWindow)
    # mainWindow.show()
    # sys.exit(app.exec_())
    #

# import sys
# from PyQt5.QtWidgets import (QApplication, QFormLayout, QLabel, QRadioButton, QCheckBox,
#                              QListWidget, QStackedWidget, QLineEdit,
#                              QHBoxLayout, QGridLayout
#                              )
# from PyQt5.Qt import QWidget, QMainWindow
#
# class StackedExample(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.leftlist = QListWidget()
#         self.leftlist.insertItem(0, 'Contact' )
#         self.leftlist.insertItem(1, 'Personal' )
#
#         self.central_widget = QWidget(self)               # define central widget
#         self.setCentralWidget(self.central_widget)    # set QMainWindow.centralWidget
#
#         self.stack1 = QWidget()
#         self.stack2 = QWidget()
#
#         self.stack1UI()
#         self.stack2UI()
#
#         self.Stack = QStackedWidget (self)
#         self.Stack.addWidget (self.stack1)
#         self.Stack.addWidget (self.stack2)
#         grid = QGridLayout()
#         self.centralWidget().setLayout(grid)          # add the layout to the central widget
#         grid.addWidget(self.leftlist,0,0)
#         grid.addWidget(self.Stack,0,1)
#
#         self.leftlist.currentRowChanged.connect(self.display)
#         self.resize(300,100)
#         self.show()
#
#     def stack1UI(self):
#         layout = QFormLayout()
#         layout.addRow("Name", QLineEdit())
#         layout.addRow("Address", QLineEdit())
#         self.stack1.setLayout(layout)
#
#     def stack2UI(self):
#         layout = QFormLayout()
#         sex = QHBoxLayout()
#         sex.addWidget(QRadioButton("Male"))
#         sex.addWidget(QRadioButton("Female"))
#         layout.addRow(QLabel("Sex"), sex)
#         layout.addRow("Date of Birth", QLineEdit())
#
#         self.stack2.setLayout(layout)
#
#     def display(self, i):
#         self.Stack.setCurrentIndex(i)
# def main():
#     app = QApplication(sys.argv)
#     ex = StackedExample()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()