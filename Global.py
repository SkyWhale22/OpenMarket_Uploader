from abc import*
from PyQt5.QtWidgets import QGroupBox, QBoxLayout, QPushButton, QTextEdit, QLabel

def GetResWidth():
    return 1280

def GetResHeight():
    return 720

class BaseClass:
	pass

class SingletonInstance:
	__instance = None

	@classmethod
	def Getinstance(cls):
		return cls.__instance

	@classmethod
	def Instance(cls, *args, **kargs):
		cls.__instance = cls(*args, **kargs)
		cls.instance = cls.Getinstance
		return cls.__instance

class UIBase(metaclass=ABCMeta):
	@abstractmethod
	def SetupUi(self, mainwindow):
		pass

	@abstractmethod
	def RetranslateUi(self, mainWindow):
		pass

class WidgetBase(QGroupBox):
    """
    위젯 베이스 클래스
    """
    def __init__(self):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(self.box)


class Widget_1(WidgetBase):
    """
    버튼 그룹
    """
    def __init__(self):
        super(Widget_1, self).__init__()
        self.setTitle("Widget_1")
        self.box.addWidget(QPushButton("Test_1"))
        self.box.addWidget(QPushButton("Test_2"))
        self.box.addWidget(QPushButton("Test_3"))


class Widget_2(WidgetBase):
    def __init__(self):
        super(Widget_2, self).__init__()
        self.setTitle("Widget_2")
        self.box.addWidget(QTextEdit())


class Widget_3(WidgetBase):
    def __init__(self):
        super(Widget_3, self).__init__()
        self.setTitle("Widget_3")
        self.box.addWidget(QLabel("Test Label"))
