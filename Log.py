from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Global import BaseClass, SingletonInstance

class Log(BaseClass, SingletonInstance):

    def SetData(self, widget, width, height):
        self.m_txtLog = QTextEdit(widget)
        self.m_txtLog.setGeometry(QRect(0, 0, width-20, height-20))
        self.m_txtLog.move(10, 10)
        self.m_txtLog.setReadOnly(True)

        font = QFont()
        font.setPointSize(12)

        self.m_txtLog.setFont(font)

    def AddMessage(self, message):
        self.m_txtLog.append(message)
        self.m_txtLog.setTextColor(QColor(0, 0, 0))
        self.m_txtLog.append("-" * 50 + "\n")

    def AddMessageWithColor(self, message, color):
        self.m_txtLog.setTextColor(color)
        self.AddMessage(message)
