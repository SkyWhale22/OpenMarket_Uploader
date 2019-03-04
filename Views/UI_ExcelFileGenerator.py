from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Log import Log
from Global import GetResWidth, GetResHeight, UIBase

class UiExcelFormatGenerator(UIBase):
	def SetupUi(self, mainWindow):
		mainWindow.setObjectName("엑셀 일괄 업로드")
		mainWindow.resize(GetResWidth(), GetResHeight())

	def RetranslateUi(self, mainWindow):
		pass
