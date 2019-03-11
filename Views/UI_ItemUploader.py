from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Log import Log

from Global import GetResHeight, GetResWidth, WidgetBase


class UiUploader(WidgetBase):
    def __init__(self, mainWindow):
        super(UiUploader, self).__init__()
        self.m_centralWidget = self
        self.m_mainWindow = mainWindow
        self.SetupUi()
        self.resize(GetResWidth(), GetResHeight())
        #self.setDisabled(False)

    # ======================================================================================================
    # Group Box - Account Selection
    # ======================================================================================================
    def SetupUi(self):
        self.MakeGbAccountSelection()
        self.MakeGbMarketType()
        self.MakeGbSalesStatus()
        self.MakeGbUploadButton()
        self.MakeGbFileUpload()
        self.MakeGbLog()

        self.RetranslateUi()

    # ======================================================================================================
    # Group Box - Account Selection
    # ======================================================================================================
    def MakeGbAccountSelection(self):
        gbAccount = QGroupBox()
        #self.gbAccount = QGroupBox()

        gbAccount.setGeometry(QRect(10, 10, 500, 100))
        gbAccount.setStyleSheet(
            '''
			QGroupBox { 
				border: 2px solid gray; 
				border-radius: 3px; 
			} 
			'''
        )

        font = QFont()
        font.setPointSize(9)

        gbAccount.setFont(font)
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
    # Group Box - Market Type
    # ======================================================================================================
    def MakeGbMarketType(self):
        self.gbMarketType = QGroupBox(self.m_centralWidget)
        #self.gbMarketType = QGroupBox()

        self.gbMarketType.setGeometry(QRect(10, 120, 500, 250))
        self.gbMarketType.setStyleSheet(
            '''
			QGroupBox { 
				border: 2px solid gray; 
				border-radius: 3px; 
			} 
			'''
        )

        font = QFont()
        font.setPointSize(9)

        self.gbMarketType.setFont(font)
        self.gbMarketType.setObjectName("gbMarketType")

        self.verticalLayout = QVBoxLayout(self.gbMarketType)
        self.verticalLayout.setObjectName("verticalLayout")

        self.rbESMPlus = QRadioButton(self.gbMarketType)
        self.rbESMPlus.setObjectName("rbESMPlus")
        self.verticalLayout.addWidget(self.rbESMPlus)

        self.rb11st = QRadioButton(self.gbMarketType)
        self.rb11st.setEnabled(False)
        self.rb11st.setCheckable(True)
        self.rb11st.setObjectName("rb11st")
        self.verticalLayout.addWidget(self.rb11st)

        self.rbSmartStore = QRadioButton(self.gbMarketType)
        self.rbSmartStore.setEnabled(False)
        self.rbSmartStore.setCheckable(True)
        self.rbSmartStore.setObjectName("rbSmartStore")
        self.verticalLayout.addWidget(self.rbSmartStore)

    # ======================================================================================================
    # Group Box - Sales status
    # ======================================================================================================
    def MakeGbSalesStatus(self):
        self.gbSalesStatus = QGroupBox(self.m_centralWidget)
        #self.gbSalesStatus = QGroupBox()

        self.gbSalesStatus.setGeometry(QRect(10, 390, 500, 250))
        self.gbSalesStatus.setStyleSheet(
            '''
			QGroupBox { 
				border: 2px solid gray; 
				border-radius: 3px; 
			} 
			'''
        )
        font = QFont()
        font.setPointSize(9)

        self.gbSalesStatus.setFont(font)
        self.gbSalesStatus.setObjectName("gbSalesStatus")

        self.verticalLayout_3 = QVBoxLayout(self.gbSalesStatus)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.rbBeginSales = QRadioButton(self.gbSalesStatus)
        self.rbBeginSales.setChecked(True)
        self.rbBeginSales.setObjectName("rbBeginSales")
        self.verticalLayout_3.addWidget(self.rbBeginSales)

        self.rbPauseSales = QRadioButton(self.gbSalesStatus)
        self.rbPauseSales.setObjectName("rbPauseSales")
        self.verticalLayout_3.addWidget(self.rbPauseSales)

    # ======================================================================================================
    # Excel file upload
    # ======================================================================================================
    def MakeGbFileUpload(self):
        self.gbFileUpload = QGroupBox(self.m_centralWidget)
        #self.gbFileUpload = QGroupBox()

        self.gbFileUpload.setStyleSheet(
            '''
			QGroupBox { 
				border: 2px solid gray; 
				border-radius: 3px; 
			} 
			'''
        )
        self.gbFileUpload.setGeometry(QRect(520, 10, 700, 100))

        font = QFont()
        font.setPointSize(9)

        self.gbFileUpload.setFont(font)
        self.gbFileUpload.setObjectName("gbFileUpload")

        self.btnUpload = QPushButton('Select', self.gbFileUpload)
        self.btnUpload.clicked.connect(self.ShowDialog)
        self.btnUpload.move(570, 35)
        self.btnUpload.setGeometry(QRect(self.btnUpload.x(), self.btnUpload.y(), 100, 50))

        self.textLine = QLineEdit(self.gbFileUpload)
        self.textLine.setGeometry(QRect(10, 10, 530, 40))
        self.textLine.move(25, 40)

    # ======================================================================================================
    # Log
    # ======================================================================================================
    def MakeGbLog(self):
        self.centralwidget = QWidget(self.m_mainWindow)
        #self.centralwidget = QWidget()

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


    # ======================================================================================================
    # Buttons
    # ======================================================================================================
    def MakeGbUploadButton(self):
        #self.btnStart = QPushButton('업로드', self.m_centralWidget)
        self.btnStart = QPushButton('업로드')

        self.btnStart.move(640, 590)
        self.btnStart.setGeometry(QRect(self.btnStart.x(), self.btnStart.y(), 500, 50))
        self.btnStart.setStyleSheet(
            """
                QPushButton{
                    font: bold; 
                }
            """
        )


    def RetranslateUi(self):
        _translate = QCoreApplication.translate
        # --------------------------------------------------------------------------------------------------
        self.gbAccount.setTitle(_translate("MainWindow", "계정 선택"))
        self.rbMirae.setText(_translate("MainWindow", "미래메디쿠스"))
        self.rbHyMedi.setText(_translate("MainWindow", "HY 메디칼"))
        # --------------------------------------------------------------------------------------------------
        self.gbMarketType.setTitle(_translate("MainWindow", "오픈 마켓 선택"))
        self.rbESMPlus.setText(_translate("MainWindow", "ESM Plus"))
        self.rb11st.setText(_translate("MainWindow", "11번가"))
        self.rbSmartStore.setText(_translate("MainWindow", "스마트 스토어"))
        # --------------------------------------------------------------------------------------------------
        self.gbSalesStatus.setTitle(_translate("MainWindow", "판매 상태"))
        self.rbPauseSales.setText(_translate("MainWindow", "판매 중지"))
        self.rbBeginSales.setText(_translate("MainWindow", "판매 개시"))
        # --------------------------------------------------------------------------------------------------
        self.gbFileUpload.setTitle(_translate("MainWindow", "엑셀 파일"))
        # # --------------------------------------------------------------------------------------------------
        # self.menu.setTitle(_translate("MainWindow", "제품 등록하기"))
        # self.menu_2.setTitle(_translate("MainWindow", "엑셀 템플릿 만들기"))

    def ShowDialog(self):
        # Get file's directory in string
        fname = QFileDialog.getOpenFileName(self.m_centralWidget, 'Open file', './')

        # Check file's existence
        if(fname[0]):
            # Check file's extension
            extension = fname[0][len(fname[0]) - 5:]
            if (extension == ".xlsm" or extension == ".xlsx"):
                self.textLine.setText(fname[0])
                Log.Getinstance().AddMessage(fname[0] + " 파일이 선택되었습니다.")
            else:
                reply = QMessageBox.question(self.m_centralWidget, 'Message', '엑셀 파일이 아닙니다.',
                                             QMessageBox.Yes)
                Log.Getinstance().AddMessageWithColor("엑셀 파일이 아닙니다.", QColor(255, 0, 0))
