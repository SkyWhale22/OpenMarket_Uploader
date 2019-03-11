from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Log import Log
from Global import GetResWidth, GetResHeight, UIBase

class UiExcelFormatGenerator(QWidget):
	def __init__(self, mainWindow, centralWidget):
		QWidget.__init__(self)
		self.m_centralWidget = centralWidget
		self.m_mainWindow = mainWindow
		self.SetupUi()
		self.MakeGbLog()
		self.setVisible(True)

	def SetupUi(self):
		self.MakeGbAccountSelection()

	# ======================================================================================================
	# Group Box - Account Selection
	# ======================================================================================================
	def MakeGbAccountSelection(self):
		self.gbAccount = QGroupBox(self.m_centralWidget)
		# self.gbAccount = QGroupBox()

		self.gbAccount.setGeometry(QRect(300, 300, 500, 100))
		self.gbAccount.setStyleSheet(
			'''
			QGroupBox { 
				border: 2px solid gray; 
				border-radius: 3px; 
			} 
			'''
		)

		font = QFont()
		font.setPointSize(9)

		self.gbAccount.setFont(font)
		self.gbAccount.setObjectName("gbAccount")

		self.horizontalLayout = QHBoxLayout(self.gbAccount)
		self.horizontalLayout.setObjectName("horizontalLayout")

		self.rbHyMedi = QRadioButton(self.gbAccount)

		self.rbHyMedi.setObjectName("radioButton_4")
		self.horizontalLayout.addWidget(self.rbHyMedi)

		self.rbMirae = QRadioButton(self.gbAccount)
		self.rbMirae.setObjectName("radioButton_3")
		self.horizontalLayout.addWidget(self.rbMirae)

	# ======================================================================================================
	# Log
	# ======================================================================================================
	def MakeGbLog(self):
		self.centralwidget = QWidget(self.m_mainWindow)
		# self.centralwidget = QWidget()

		self.centralwidget.setObjectName("centralwidget")

		self.gbLog = QGroupBox(self.m_centralWidget)
		self.gbLog.setGeometry(QRect(520, 120, 700, 460))
		self.gbLog.setStyleSheet(
			'''
			QGroupBox { 
				border: 2px solid gray; 
				border-radius: 3px; 
			} 
			'''
		)

		Log.Instance().SetData(self.gbLog, self.gbLog.width(), self.gbLog.height())

	def RetranslateUi(self, mainWindow):
		_translate = QCoreApplication.translate
		# --------------------------------------------------------------------------------------------------
		self.gbAccount.setTitle(_translate("MainWindow", "계정 선택"))
		self.rbMirae.setText(_translate("MainWindow", "미래메디쿠스"))
		self.rbHyMedi.setText(_translate("MainWindow", "HY 메디칼"))
