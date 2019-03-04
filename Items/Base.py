"""
    ItemBase class definition.
    Every items which will contain scrapped date from the web should inherit this class.
"""

class ItemBase:
	"""Super Class"""

	####################################################################################################
	#                                        Member Variables                                          #
	####################################################################################################

	#-------------------------------------------------------------------------------------------------
	# Protected
	#-------------------------------------------------------------------------------------------------
	_m_name = None          # Name of the product
	_m_price = None         # Price of the product
	_m_modelCode = None     # Model Code of the product
	_m_stockNum = None      # Left amount of stocks
	_m_brandName = None     # Brand name of the product

	#-------------------------------------------------------------------------------------------------
	# Protected
	#-------------------------------------------------------------------------------------------------
	m_next = None
	m_prev = None

	####################################################################################################
	#                                        Member Functions                                          #
	####################################################################################################

	#-------------------------------------------------------------------------------------------------
	# Private
	#-------------------------------------------------------------------------------------------------
	def __init__(self, name, price, modelCode, stockNum, brandName):
		self._m_name = name
		self._m_price = price
		self._m_modelCode = modelCode
		self._m_stockNum = stockNum
		self._m_brandName = brandName

	#-------------------------------------------------------------------------------------------------
	# Public
	#-------------------------------------------------------------------------------------------------

	# Returns the name of the product
	def GetProductName(self):
		return self._m_name

	# Returns the price of the product
	def GetProductPrice(self):
		return self._m_price

	# Returns the model code of the product
	def GetProductCode(self):
		return self._m_modelCode

	# Returns the left amount of the product
	def GetNumberOfStocks(self):
		return self._m_stockNum

	# Returns the brand name of the product
	def GetProductBrandName(self):
		return self._m_brandName

	# Prints all contained data
	def PrintInfo(self):
		print(self.GetProductName())
		print(self.GetProductPrice())
		print(self.GetProductCode())
		print(self.GetNumberOfStocks())

	def SetNextNode(self, item):
		ItemBase(item).m_previous = self
		self.m_next = item


# itemTest = ItemBase("test", 123, "testCode", 100, "testBrand")
# itemTest.PrintInfo()
