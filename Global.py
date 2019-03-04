from abc import*

def GetResWidth():
    return 1230

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
