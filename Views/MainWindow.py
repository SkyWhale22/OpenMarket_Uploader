# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5.QtWidgets import *
from Global import SingletonInstance, BaseClass
from Views.UI_ItemUploader import UiUploader
from Views.UI_ExcelFileGenerator import UiExcelFormatGenerator


class WindowController(SingletonInstance):

    def InitialSetup(self):
        self.m_app = QApplication(sys.argv)
        self.m_mainWindow = QMainWindow()
        self.m_currentUI = UiUploader()
        self.m_currentUI.SetupUi(self.m_mainWindow)

    def SetWindow(self, ui):
        self.m_currentUI = ui

    def Show(self):
        self.m_mainWindow.show()

    def Destory(self):
        sys.exit(self.m_app.exec_())

if __name__ == "__main__":
    m_app = QApplication(sys.argv)
    m_mainWindow = QMainWindow()
    m_currentUI = UiUploader()
    m_currentUI.SetupUi(m_mainWindow)

    m_mainWindow.show()
    sys.exit(m_app.exec_())

    ctrl = WindowController.Instance().InitialSetup()
    ctrl.Show()
    ctrl.SetWindow(UiExcelFormatGenerator())
    ctrl.Destory()
    #ui = UiMainWindow()
    # ui.SetupUi(mainWindow)
    # mainWindow.show()
    # sys.exit(app.exec_())
    #

