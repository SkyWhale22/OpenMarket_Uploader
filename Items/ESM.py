from Items.Base import ItemBase
from enum import Enum
from Interfaces.SourceOfOrigin import ISourceOfOrigin
"""
	ItemESM class definition
	This class inherited ItemBase Class.
	This class contains the data, which will be updated on ESM Plus, which is used for uploading item on 'G-Market'
	and 'Auction'
"""

class Languages(Enum):
	KEnglish    = 0,
	KJapanese   = 1,
	KChinese    = 2,
	KCount      = 3

class ESMItemInfo:
	####################################################################################################
	#                                        Member Variables                                          #
	####################################################################################################

	# -------------------------------------------------------------------------------------------------
	# Public
	# -------------------------------------------------------------------------------------------------
	m_productName           = None
	m_caution               = None
	m_warrenty              = None
	m_asRepresentitive      = None
	m_estimatedDeliveryDays = None
	m_licenceNumber         = None
	m_kcCredit              = None
	m_ratedVoltage           = None
	m_releaseDate           = None
	m_manufacturer          = None
	m_originCountry         = None
	m_howToUse              = None

	####################################################################################################
	#                                        Member Functions                                          #
	####################################################################################################

	# -------------------------------------------------------------------------------------------------
	# Private
	# -------------------------------------------------------------------------------------------------
	def __init__(self, productName, caution, warrenty, asRepresentitive, estimatedDeliveryDays, licenceNum, kcCredit, ratedVoltage, releaseDate, manufacturer, manufacturingCountry, howToUse):
		self.m_productName              = productName
		self.m_caution                  = caution
		self.m_warrenty                 = warrenty
		self.m_asRepresentitive         = asRepresentitive
		self.m_estimatedDeliveryDays    = estimatedDeliveryDays
		self.m_licenceNumber            = licenceNum
		self.m_kcCredit                 = kcCredit
		self.m_ratedVoltage             = ratedVoltage
		self.m_releaseDate              = releaseDate
		self.m_manufacturer             = manufacturer
		self.m_originCountry            = manufacturingCountry
		self.m_howToUse                 = howToUse


class ItemESM(ItemBase):
	####################################################################################################
	#                                        Member Variables                                          #
	####################################################################################################

	#-------------------------------------------------------------------------------------------------
	# Private
	#-------------------------------------------------------------------------------------------------
	__m_productNameForPromotion = None
	__m_multiLingProductName    = {}
	__m_categoryName            = None
	__m_esmItemInfo             = None

	__m_sourceOfOrigin = None
	#-------------------------------------------------------------------------------------------------
	# Protected
	#-------------------------------------------------------------------------------------------------

	#-------------------------------------------------------------------------------------------------
	# Public
	#-------------------------------------------------------------------------------------------------

	####################################################################################################
	#                                        Member Functions                                          #
	####################################################################################################

	#-------------------------------------------------------------------------------------------------
	# Private
	#-------------------------------------------------------------------------------------------------
	def __init__(self, name, price, modelCode, stockNum, brandName, promotionName, sourceOfOrigin_sub1, sourceOfOrigin_sub2, sourceOfOrigin_sub3, engName, japName, chiName, esmItemInfo):
		super(ItemESM, self).__init__(name, price, modelCode, stockNum, brandName)

		self.__m_productNameForPromotion                    = promotionName
		self.__m_sourceOfOrigin = ISourceOfOrigin(sourceOfOrigin_sub1, sourceOfOrigin_sub2, sourceOfOrigin_sub3)

		self.__m_multiLingProductName[Languages.KEnglish] = engName
		self.__m_multiLingProductName[Languages.KJapanese]  = japName
		self.__m_multiLingProductName[Languages.KChinese]   = chiName
		self.__m_esmItemInfo                                = esmItemInfo

	#-------------------------------------------------------------------------------------------------
	# Public
	#-------------------------------------------------------------------------------------------------

	# Returns ESMItemInfo struct.
	def GetESMItemInfo(self):
		return self.__m_esmItemInfo

	# Returns promotion name of the instance.
	def GetPromotionName(self):
		return self.__m_productNameForPromotion

	# Returns
	def GetMultiLingProductName(self, language):
		return self.__m_multiLingProductName[language]

		# switch-case version of code above.
		# switcher = {
		# 	"English"   : self.__m_multiLingProductName[Languages.KEnglish],
		# 	"Japanese"  : self.__m_multiLingProductName[Languages.KJapanese],
		# 	"Chinese"   : self.__m_multiLingProductName[Languages.KChinese]
		# }
		# return switcher.get(language, "Wrong Input")

	# Returns category name of the instance.
	def GetCategoryName(self):
		return self.__m_categoryName

	# Returns source of origin of the instance.
	def GetSourceOfOrigin(self):
		return self.__m_sourceOfOrigin
