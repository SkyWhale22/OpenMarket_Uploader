from  enum import Enum

"""
    RegionType enum class definition.
"""
class RegionType(Enum):
	KDomestic       = 2
	KInternational  = 3

"""
    SourceOfOrigin class definition.
"""
class ISourceOfOrigin:
	####################################################################################################
	#                                        Member Variables                                          #
	####################################################################################################

	#-------------------------------------------------------------------------------------------------
	# Private
	#-------------------------------------------------------------------------------------------------
	__m_region = None
	__m_regionType = None

	__m_middleSOO    = [None]
	__m_lastSOO      = [None]


	####################################################################################################
	#                                        Member Functions                                          #
	####################################################################################################

	#-------------------------------------------------------------------------------------------------
	# Private
	#-------------------------------------------------------------------------------------------------
	def __init__(self, sub1, sub2, sub3):
		self.SetRegion(sub1)
		self.SetMiddleSOO(sub2)
		self.SetLastSOO(sub3)

	def SetRegion(self, selected):

		switcher = {
			"국내" : RegionType.KDomestic,
			"수입" : RegionType.KInternational
		}.get(selected, None)

		if(switcher == RegionType.KDomestic):
			#self.m_driver.find_element_by_xpath('//*[@id="sltOrigin"]/option[2]').click()
			self.__m_region = Domestic()
			self.__m_regionType = RegionType.KDomestic
		else:
			#self.m_driver.find_element_by_xpath('//*[@id="sltOrigin"]/option[3]').click()
			self.__m_region = International()
			self.__m_regionType = RegionType.KInternational

		# switcher = {
		# 	"국내": '//*[@id="sltOrigin"]/option[2]',
		# 	"수입": '//*[@id="sltOrigin"]/option[3]'
		# }.get(selected, None)

	def GetRegionType(self):
		return self.__m_regionType

	def SetMiddleSOO(self, input):
		if(self.__m_regionType == RegionType.KDomestic):
			self.__m_region.SetMiddleSOO(input, self.__m_middleSOO)
		#else:

	def SetLastSOO(self, input):
		self.__m_region.SetLastSOO(input, self.__m_middleSOO[0], self.__m_lastSOO)

	def CheckRegionType(self):
		self.__m_region.PrintRegion()

	def GetFirstXpath(self):
		xpath = '//*[@id="sltOrigin"]/option[' + str(self.__m_regionType.value) + ']'
		return xpath

	def GetSecondXpath(self):
		xpath = '//*[@id="sltOriginLName"]/option[' + str(self.__m_middleSOO[0].value) + ']'
		return xpath

	def GetThirdXpath(self):
		xpath = '//*[@id="sltOriginMName"]/option[' + str(self.__m_lastSOO[0].value) + ']'
		return xpath

"""
    RegionBase class virtual interface.
    Domastic class and International class inherited this class.
"""
class RegionBase:
	####################################################################################################
	#                                        Member Variables                                          #
	####################################################################################################

	#-------------------------------------------------------------------------------------------------
	# Protected
	#-------------------------------------------------------------------------------------------------
	_m_middleSOO    = None
	_m_lastSOO      = None

	#-------------------------------------------------------------------------------------------------
	# Public
	#-------------------------------------------------------------------------------------------------

	def SetMiddleSOO(self, input, output):
		pass

	def SetLastSOO(self, input, middleSOO, output):
		pass

	# Print
	def PrintRegion(self):
		print("Region Base Class")

"""
    Domestic class definition.
    This class holds every are in the South Korea.
"""
class Domestic(RegionBase):
	####################################################################################################
	#                                        Member Variables                                          #
	####################################################################################################

	#-------------------------------------------------------------------------------------------------
	# Public
	#-------------------------------------------------------------------------------------------------

	# Provinces
	class Provinces(Enum):
		KGangwon        = 2
		KGyeonggi       = 3
		KGyeongnam      = 4
		KGyeongbuk      = 5
		KDaegu          = 6
		KGwangju        = 7
		KDaejeon        = 8
		KBusan          = 9
		KSeoul          = 10
		KSejong         = 11
		KUlsan          = 12
		KIncheon        = 13
		KJeonnam        = 14
		KJeonbuk        = 15
		KJeju           = 16
		KChungnam       = 17
		KChungbuk       = 18

	# 강원도
	class GangWon(Enum):
		KGangNeung      = 0
		KGoSung         = 1
		KDongHae        = 2
		KSamChuck       = 3
		KSokCho         = 4
		KYangGu         = 5
		KYangYang       = 6
		KYeongWol       = 7
		KWonJu          = 8
		KInje           = 9
		KJeongSeon      = 10
		KCheorWon       = 11
		KChunCheon      = 12
		KTaeBaek        = 13
		KPyeongChang    = 14
		KHongChang      = 15
		KHwaCheon       = 16
		KHoengSung      = 17
		KCount          = 18

	# 경기도
	class GyeongGi(Enum):
		KGapyeong       = 0
		KGoyang         = 1
		KGwacheon       = 2
		kGwangmyeong    = 3
		KGwangju        = 4
		KGuri           = 5
		KGunpo          = 6
		KSuwon          = 7
		KSeongnam       = 8
		KYongin         = 9
		KBucheon        = 10
		KAnsan          = 11
		KAnyang         = 12
		KNamyangju      = 13
		KHwaseong       = 14
		KUijeongbu      = 15
		KSiheung        = 16
		KPyeongtaek     = 17
		KGwangmyeong    = 18
		KPaju           = 19
		KGimpo          = 20
		KIcheon         = 21
		KYangju         = 22
		KOsan           = 23
		KAnseong        = 24
		KUiwang         = 25
		KHanam          = 26
		KPocheon        = 27
		KDongducheon    = 28
		KYeoju          = 30
		KYangpyeong     = 31
		KYeoncheon      = 32
		KCount          = 33

	# 경상남도
	class GyeongNam(Enum):
		KChangwon           = 0
		KGimhae             = 1
		KJinju              = 2
		KYangsan            = 3
		KGeoje              = 4
		KTongyeong          = 5
		KSacheon            = 6
		KMiryang            = 7
		KHamanCounty        = 8
		KGeochangCounty     = 9
		KChangnyeongCounty  = 10
		KGoseongCounty      = 11
		KNamhaeCounty       = 12
		KHapcheonCounty     = 13
		KHadongCounty       = 14
		KHamyangCounty      = 15
		KSancheongCounty    = 16
		kUiryeongCounty     = 17
		KCount              = 18

	# 경상북도
	class GyeongBuk(Enum):
		KPohang             = 0
		KGumi               = 1
		KGyeongsan          = 2
		KGyeongju           = 3
		KAndong             = 4
		KGimcheon           = 5
		KYeongju            = 6
		KSangju             = 7
		KYeongcheon         = 8
		KMungyeong          = 9
		KChilgokCounty      = 10
		KUiseongCounty      = 11
		KUljinCounty        = 12
		KYecheonCounty      = 13
		KCheongdoCounty     = 14
		KSeongjuCounty      = 15
		KYeongdeokCounty    = 16
		KGoryeongCounty     = 17
		KBonghwaCounty      = 18
		KCheongsongCounty   = 19
		KGunwiCounty        = 20
		KYeongyangCounty    = 21
		KUlleungCounty      = 22
		KCount              = 23

	# 대구
	class DaeGu(Enum):
		KNamgu              = 0
		KDalseo             = 1
		KDalSeongCounty     = 2
		KDonggu             = 3
		KBukgu              = 4
		KSeogu              = 5
		KSuseong            = 6
		KJunggu             = 7
		KCount              = 8

	# 광주
	class GwangJu(Enum):
		KGwangsan       = 0
		KNamgu          = 1
		KDonggu         = 2
		KBukgu          = 3
		KSeogu          = 4
		KCount          = 5

	# 대전
	class DaeJeon(Enum):
		KDaedukgu       = 0
		KDonggu         = 1
		KSeogu          = 2
		KYusunggu       = 3
		KJunggu         = 4
		KCount          = 5
	# 부산
	class Busan(Enum):
		KGangseo        = 0
		KGeumjeong      = 1
		KGijangCounty   = 2
		KNamgu          = 3
		KDonggu         = 4
		KDongraegu      = 6
		KBusanjingu     = 7
		KBukgu          = 8
		KSasanggu       = 9
		KSahagu         = 10
		KSeogu          = 11
		KSuyounggu      = 12
		KYeongjegu      = 13
		KYoungdogu      = 14
		KJunggu         = 15
		KHaeundaegu     = 16
		KCount          = 17

	# 서울
	class Seoul(Enum):
		KGangnam        = 0
		KGangdong       = 1
		KGangbuk        = 2
		KGangseo        = 3
		KGwanak         = 4
		KGwangjin       = 5
		KGuro           = 6
		KGeumcheon      = 7
		KNowon          = 8
		KDobong         = 9
		KDongdaemoon    = 10
		KDongjak        = 11
		KMapo           = 12
		KSeodaemun      = 13
		KSeocho         = 14
		KSungdong       = 15
		KSungbuk        = 16
		KSongpa         = 17
		KYangchun       = 18
		KYeongdeungpo   = 19
		KYongsan        = 20
		KEunpyeong      = 21
		KJongro         = 22
		KJunggu         = 23
		KJungrang       = 24
		KCount          = 25

	# 세종
	class Sejong(Enum):
		KAll            = 0
		KCount          = 1

	# 울산
	class Ulsan(Enum):
		KNamgu          = 0
		KDonggu         = 1
		KBukgu          = 2
		KUljugu         = 3
		KJunggu         = 4
		KCount          = 5

	# 인천
	class InCheon(Enum):
		KGanghwa        = 0
		KGyeyang        = 1
		KNamgu          = 2
		KNamdonggu      = 3
		KDonggu         = 4
		KBupyeonggu     = 5
		KSeogu          = 6
		KYeonsugu       = 7
		KOngjingu       = 8
		KJunggu         = 9
		KCount          = 10

	# 전라남도
	class JeonNam(Enum):
		KYeosu          = 0
		KMokpo          = 1
		KSuncheon       = 2
		KGwangyang      = 3
		KNaju           = 4
		KMuan           = 5
		KHaenam         = 6
		KGoheung        = 7
		KHwasun         = 8
		KYeongam        = 9
		KYeonggwang     = 10
		KWando          = 11
		KDamyang        = 12
		KBoseong        = 13
		KJangseong      = 14
		KJangheung      = 15
		KGangjin        = 16
		KSinan          = 17
		KHampyeong      = 18
		KJindo          = 19
		KGokseong       = 20
		KGurye          = 21
		KCount          = 22

	# 전라북도
	class JeonBuk(Enum):
		KJeonju         = 0
		KIksan          = 1
		KGunsan         = 2
		KJeongeup       = 3
		KGimje          = 4
		KNamwon         = 5
		KWanju          = 6
		KKGochang       = 7
		KBuan           = 8
		KSunchang       = 9
		KImsil          = 10
		KMuju           = 11
		KJinan          = 12
		KJangsu         = 13
		KCount          = 14

	# 제주도
	class Jeju(Enum):
		KSeogwuipo      = 0
		KJejus          = 1
		KCount          = 2

	# 충청남도
	class ChungNam(Enum):
		KCheonan        = 0
		KAsan           = 1
		KSeosan         = 2
		KDangjin        = 3
		KGongju         = 4
		KKNonsan        = 5
		KBoryeong       = 6
		KGyeryong       = 7
		KHongseong      = 8
		KYesan          = 9
		KBuyeo          = 10
		KSeocheon       = 11
		KTaean          = 12
		KGeumsan        = 13
		KCheongyang     = 14
		KCount          = 15

	# 충청북도
	class ChungBuk(Enum):
		KCheongju       = 0
		KChungju        = 1
		KJecheon        = 2
		KKEumseong      = 3
		KJincheon       = 4
		KOkcheon        = 5
		KYeongdong      = 6
		KGoesan         = 7
		KJeungpyeong    = 8
		KBoeun          = 9
		KDanyang        = 10
		KCount          = 11

	####################################################################################################
	#                                        Member Functions                                          #
	####################################################################################################

	#-------------------------------------------------------------------------------------------------
	# Public
	#-------------------------------------------------------------------------------------------------

	def SetRegion(self):
		self.m_driver.find_element_by_xpath('//*[@id="sltOrigin"]/option[2]').click()

	def PrintRegion(self):

		print("Domestic")

	def SetMiddleSOO(self, input, output):
		switcher = {
		    "강원도"    : self.Provinces.KGangwon,
		    "경기도"    : self.Provinces.KGyeonggi,
			"경상남도"  : self.Provinces.KGyeongnam,
			"경상북도"  : self.Provinces.KGyeongbuk,
			"대구"      : self.Provinces.KDaegu,
			"광주"      : self.Provinces.KGwangju,
			"대전"      : self.Provinces.KDaejeon,
			"부산"      : self.Provinces.KBusan,
			"서울"      : self.Provinces.KSeoul,
			"세종"      : self.Provinces.KSejong,
			"울산"      : self.Provinces.KUlsan,
			"인천"      : self.Provinces.KIncheon,
			"전라남도"  : self.Provinces.KJeonnam,
			"전라북도"  : self.Provinces.KJeonbuk,
			"제주도"    : self.Provinces.KJeju,
			"충청남도"  : self.Provinces.KChungnam,
			"충청북도"  : self.Provinces.KChungbuk
		}.get(input)

		output[0] = switcher

	def SetLastSOO(self, input, middleSOO, output):
		switcher = None
		if(middleSOO == self.Provinces.KGangwon):
			switcher = {
				"강릉" : self.GangWon.KGangNeung,
				"고성" : self.GangWon.KGoSung,
				"동해" : self.GangWon.KDongHae,
				"삼척" : self.GangWon.KSamChuck,
				"속초" : self.GangWon.KSokCho,
				"양구" : self.GangWon.KYangGu,
				"양양" : self.GangWon.KYangYang,
				"영월" : self.GangWon.KYeongWol,
				"원주" : self.GangWon.KWonJu,
				"인제" : self.GangWon.KInje,
				"정선" : self.GangWon.KJeongSeon,
				"철원" : self.GangWon.KCheorWon,
				"춘천" : self.GangWon.KChunCheon,
				"태백" : self.GangWon.KTaeBaek,
				"평챵" : self.GangWon.KPyeongChang,
				"홍창" : self.GangWon.KHongChang,
				"화천" : self.GangWon.KHwaCheon,
				"횡성" : self.GangWon.KHoengSung,
			}.get(input, None)

		elif(middleSOO == self.Provinces.KGyeonggi):
			switcher = {
				"가평"    : self.GyeongGi.KGapyeong,
				"고양"    : self.GyeongGi.KGoyang,
				"과천"    : self.GyeongGi.KGwacheon,
				"광명"    : self.GyeongGi.kGwangmyeong,
				"광주"    : self.GyeongGi.KGwangju,
				"구리"    : self.GyeongGi.KGuri,
				"군포"    : self.GyeongGi.KGunpo,
				"수원"    : self.GyeongGi.KSuwon,
				"성남"    : self.GyeongGi.KSeongnam,
				"용인"    : self.GyeongGi.KYongin,
				"부천"    : self.GyeongGi.KBucheon,
				"안산"    : self.GyeongGi.KAnsan,
				"안양"    : self.GyeongGi.KAnyang,
				"남양주"  : self.GyeongGi.KNamyangju,
				"화성"    : self.GyeongGi.KHwaseong,
				"의정부"  : self.GyeongGi.KUijeongbu,
				"시흥"    : self.GyeongGi.KSiheung,
				"평택"    : self.GyeongGi.KPyeongtaek,
				"파주"    : self.GyeongGi.KPaju,
				"김포"    : self.GyeongGi.KGimpo,
				"인천"    : self.GyeongGi.KIcheon,
				"양주"    : self.GyeongGi.KYangju,
				"오산"    : self.GyeongGi.KOsan,
				"안성"    : self.GyeongGi.KAnseong,
				"의왕"    : self.GyeongGi.KUiwang,
				"하남"    : self.GyeongGi.KHanam,
				"포천"    : self.GyeongGi.KPocheon,
				"동두천"  : self.GyeongGi.KDongducheon,
				"여주"    : self.GyeongGi.KYeoju,
				"양평"    : self.GyeongGi.KYangpyeong,
				"연천"    : self.GyeongGi.KYeoncheon
			}.get(input, None)

		elif(middleSOO == self.Provinces.KGyeongnam):
			switcher = {
				"창원" : self.GyeongNam.KChangwon,
				"김해" : self.GyeongNam.KGimhae,
				"진주" : self.GyeongNam.KJinju,
				"양산" : self.GyeongNam.KYangsan,
				"거제" : self.GyeongNam.KGeoje,
				"통영" : self.GyeongNam.KTongyeong,
				"사천" : self.GyeongNam. KSacheon,
				"밀양" : self.GyeongNam.KMiryang,
				"함안" : self.GyeongNam.KHamanCounty,
				"고챵" : self.GyeongNam.KGeochangCounty,
				"창녕" : self.GyeongNam.KChangnyeongCounty,
				"고성" : self.GyeongNam.KGoseongCounty,
				"남해" : self.GyeongNam.KNamhaeCounty,
				"합천" : self.GyeongNam.KHapcheonCounty,
				"하동" : self.GyeongNam.KHadongCounty,
				"함양" : self.GyeongNam.KHamyangCounty,
				"산청" : self.GyeongNam.KSancheongCounty,
				"의령" : self.GyeongNam.kUiryeongCounty
			}.get(input, None)

		elif(middleSOO == self.Provinces.KGyeongbuk):
			switcher = {
				"포항" : self.GyeongBuk.KPohang,
				"구미" : self.GyeongBuk.KGumi,
				"경산" : self.GyeongBuk.KGyeongsan,
				"경주" : self.GyeongBuk.KGyeongju,
				"안동" : self.GyeongBuk.KAndong ,
				"김천" : self.GyeongBuk.KGimcheon,
				"영주" : self.GyeongBuk.KYeongju,
				"상주" : self.GyeongBuk.KSangju,
				"영천" : self.GyeongBuk.KYeongcheon,
				"문경" : self.GyeongBuk.KMungyeong,
				"칠곡" : self.GyeongBuk.KChilgokCounty,
				"의성" : self.GyeongBuk.KUiseongCounty,
				"을진" : self.GyeongBuk.KUljinCounty,
				"예천" : self.GyeongBuk.KYecheonCounty,
				"청도" : self.GyeongBuk.KCheongdoCounty,
				"성주" : self.GyeongBuk.KSeongjuCounty,
				"영덕" : self.GyeongBuk.KYeongdeokCounty,
				"고령" : self.GyeongBuk.KGoryeongCounty,
				"봉화" : self.GyeongBuk.KBonghwaCounty,
				"청송" : self.GyeongBuk.KCheongsongCounty,
				"군위" : self.GyeongBuk.KGunwiCounty,
				"영상" : self.GyeongBuk.KYeongyangCounty,
				"을영" : self.GyeongBuk.KUlleungCounty
			}.get(input, None)

		# elif(self.__m_province == self.Provinces.KDaegu):
		# elif(self.__m_province == self.Provinces.KGwangju):
		# elif(self.__m_province == self.Provinces.KDaejeon):
		# elif(self.__m_province == self.Provinces.KBusan):
		# elif(self.__m_province == self.Provinces.KSeoul):
		# elif(self.__m_province == self.Provinces.KSejong):
		# elif(self.__m_province == self.Provinces.KUlsan):
		# elif(self.__m_province == self.Provinces.KIncheon):
		# elif(self.__m_province == self.Provinces.KJeonnam):
		# elif(self.__m_province == self.Provinces.KJeonbuk):
		# elif(self.__m_province == self.Provinces.KJeju):
		# elif(self.__m_province == self.Provinces.KChungnam):
		# elif(self.__m_province == self.Provinces.KChungbuk):

		output[0] = switcher

	# def SetProvince(self, input):
	# 	switcher = {
	# 	    "강원도"    : '//*[@id="sltOriginLName"]/option[2]',
	# 	    "경기도"    : '//*[@id="sltOriginLName"]/option[3]',
	# 		"경상남도"  : '//*[@id="sltOriginLName"]/option[4]',
	# 		"경상북도"  : '//*[@id="sltOriginLName"]/option[5]',
	# 		"대구"      : '//*[@id="sltOriginLName"]/option[6]',
	# 		"광주"      : '//*[@id="sltOriginLName"]/option[7]',
	# 		"대전"      : '//*[@id="sltOriginLName"]/option[8]',
	# 		"부산"      : '//*[@id="sltOriginLName"]/option[9]',
	# 		"서울"      : '//*[@id="sltOriginLName"]/option[10]',
	# 		"세종"      : '//*[@id="sltOriginLName"]/option[11]',
	# 		"울산"      : '//*[@id="sltOriginLName"]/option[12]',
	# 		"인천"      : '//*[@id="sltOriginLName"]/option[13]',
	# 		"전라남도"  : '//*[@id="sltOriginLName"]/option[14]',
	# 		"전라북도"  : '//*[@id="sltOriginLName"]/option[15]',
	# 		"제주도"    : '//*[@id="sltOriginLName"]/option[16]',
	# 		"충청남도"  : '//*[@id="sltOriginLName"]/option[17]',
	# 		"충청북도"  : '//*[@id="sltOriginLName"]/option[18]'
	# 	}.get(input)
	#
	# 	self.__m_province = switcher
	#
	# 	def SetArea(self, areaText):
	# 		switcher = None
	# 		if (self.__m_province == self.Provinces.KGangwon):
	# 			switcher = {
	# 				"강릉": '//*[@id="sltOriginMName"]/option[2]',
	# 				"고성": '//*[@id="sltOriginMName"]/option[3]',
	# 				"동해": '//*[@id="sltOriginMName"]/option[4]',
	# 				"삼척": '//*[@id="sltOriginMName"]/option[5]',
	# 				"속초": '//*[@id="sltOriginMName"]/option[6]',
	# 				"양구": '//*[@id="sltOriginMName"]/option[7]',
	# 				"양양": '//*[@id="sltOriginMName"]/option[8]',
	# 				"영월": '//*[@id="sltOriginMName"]/option[9]',
	# 				"원주": '//*[@id="sltOriginMName"]/option[10]',
	# 				"인제": '//*[@id="sltOriginMName"]/option[11]',
	# 				"정선": '//*[@id="sltOriginMName"]/option[12]',
	# 				"철원": '//*[@id="sltOriginMName"]/option[13]',
	# 				"춘천": '//*[@id="sltOriginMName"]/option[14]',
	# 				"태백": '//*[@id="sltOriginMName"]/option[15]',
	# 				"평챵": '//*[@id="sltOriginMName"]/option[16]',
	# 				"홍창": '//*[@id="sltOriginMName"]/option[17]',
	# 				"화천": '//*[@id="sltOriginMName"]/option[18]',
	# 				"횡성": '//*[@id="sltOriginMName"]/option[19]',
	# 			}.get(areaText, "Wrong Input!")
	#
	# 		elif (self.__m_province == self.Provinces.KGyeonggi):
	# 			switcher = {
	# 				"가평": self.GyeongGi.KGapyeong,
	# 				"고양": self.GyeongGi.KGoyang,
	# 				"과천": self.GyeongGi.KGwacheon,
	# 				"광명": self.GyeongGi.kGwangmyeong,
	# 				"광주": self.GyeongGi.KGwangju,
	# 				"구리": self.GyeongGi.KGuri,
	# 				"군포": self.GyeongGi.KGunpo,
	# 				"수원": self.GyeongGi.KSuwon,
	# 				"성남": self.GyeongGi.KSeongnam,
	# 				"용인": self.GyeongGi.KYongin,
	# 				"부천": self.GyeongGi.KBucheon,
	# 				"안산": self.GyeongGi.KAnsan,
	# 				"안양": self.GyeongGi.KAnyang,
	# 				"남양주": self.GyeongGi.KNamyangju,
	# 				"화성": self.GyeongGi.KHwaseong,
	# 				"의정부": self.GyeongGi.KUijeongbu,
	# 				"시흥": self.GyeongGi.KSiheung,
	# 				"평택": self.GyeongGi.KPyeongtaek,
	# 				"파주": self.GyeongGi.KPaju,
	# 				"김포": self.GyeongGi.KGimpo,
	# 				"인천": self.GyeongGi.KIcheon,
	# 				"양주": self.GyeongGi.KYangju,
	# 				"오산": self.GyeongGi.KOsan,
	# 				"안성": self.GyeongGi.KAnseong,
	# 				"의왕": self.GyeongGi.KUiwang,
	# 				"하남": self.GyeongGi.KHanam,
	# 				"포천": self.GyeongGi.KPocheon,
	# 				"동두천": self.GyeongGi.KDongducheon,
	# 				"여주": self.GyeongGi.KYeoju,
	# 				"양평": self.GyeongGi.KYangpyeong,
	# 				"연천": self.GyeongGi.KYeoncheon
	# 			}.get(areaText, "Wrong Input!")
	#
	# 		elif (self.__m_province == self.Provinces.KGyeongnam):
	# 			switcher = {
	# 				"창원": self.GyeongNam.KChangwon,
	# 				"김해": self.GyeongNam.KGimhae,
	# 				"진주": self.GyeongNam.KJinju,
	# 				"양산": self.GyeongNam.KYangsan,
	# 				"거제": self.GyeongNam.KGeoje,
	# 				"통영": self.GyeongNam.KTongyeong,
	# 				"사천": self.GyeongNam.KSacheon,
	# 				"밀양": self.GyeongNam.KMiryang,
	# 				"함안": self.GyeongNam.KHamanCounty,
	# 				"고챵": self.GyeongNam.KGeochangCounty,
	# 				"창녕": self.GyeongNam.KChangnyeongCounty,
	# 				"고성": self.GyeongNam.KGoseongCounty,
	# 				"남해": self.GyeongNam.KNamhaeCounty,
	# 				"합천": self.GyeongNam.KHapcheonCounty,
	# 				"하동": self.GyeongNam.KHadongCounty,
	# 				"함양": self.GyeongNam.KHamyangCounty,
	# 				"산청": self.GyeongNam.KSancheongCounty,
	# 				"의령": self.GyeongNam.kUiryeongCounty
	# 			}.get(areaText, "Wrong Input!")
	#
	# 		elif (self.__m_province == self.Provinces.KGyeongbuk):
	# 			switcher = {
	# 				"포항": self.GyeongBuk.KPohang,
	# 				"구미": self.GyeongBuk.KGumi,
	# 				"경산": self.GyeongBuk.KGyeongsan,
	# 				"경주": self.GyeongBuk.KGyeongju,
	# 				"안동": self.GyeongBuk.KAndong,
	# 				"김천": self.GyeongBuk.KGimcheon,
	# 				"영주": self.GyeongBuk.KYeongju,
	# 				"상주": self.GyeongBuk.KSangju,
	# 				"영천": self.GyeongBuk.KYeongcheon,
	# 				"문경": self.GyeongBuk.KMungyeong,
	# 				"칠곡": self.GyeongBuk.KChilgokCounty,
	# 				"의성": self.GyeongBuk.KUiseongCounty,
	# 				"을진": self.GyeongBuk.KUljinCounty,
	# 				"예천": self.GyeongBuk.KYecheonCounty,
	# 				"청도": self.GyeongBuk.KCheongdoCounty,
	# 				"성주": self.GyeongBuk.KSeongjuCounty,
	# 				"영덕": self.GyeongBuk.KYeongdeokCounty,
	# 				"고령": self.GyeongBuk.KGoryeongCounty,
	# 				"봉화": self.GyeongBuk.KBonghwaCounty,
	# 				"청송": self.GyeongBuk.KCheongsongCounty,
	# 				"군위": self.GyeongBuk.KGunwiCounty,
	# 				"영상": self.GyeongBuk.KYeongyangCounty,
	# 				"을영": self.GyeongBuk.KUlleungCounty
	# 			}.get(areaText, "Wrong Input!")

		#   "강원도"    : "self.Gangwon",
		#   "경기도"    : "self.GyeongGi",
		# 	"경상남도"  : "self.GyeongNam",
		# 	"경상북도"  : "self.GyeongBuk",
		# 	"대구"      : "self.DaeGu",
		# 	"광주"      : "self.GwangJu",
		# 	"대전"      : "self.DaeJeon",
		# 	"부산"      : "self.Busan",
		# 	"서울"      : "self.Seoul",
		# 	"세종"      : "self.Sejong",
		# 	"울산"      : "self.Ulsan",
		# 	"인천"      : "self.InCheon",
		# 	"전라남도"  : "self.JeonNam",
		# 	"전라북도"  : "self.JeonBuk",
		# 	"제주도"    : "self.Jeju",
		# 	"충청남도"  : "self.ChungNam",
		# 	"충청북도"  : "self.ChungBuk"
		# }
		# selClass = getattr(self, areaText, lambda:"default")
		#
		# self.__m_area = selClass()


class International(RegionBase):
	def PrintRegion(self):
		print("International")

	def SetArea(self, areaText):
		pass

test = ISourceOfOrigin("국내", "강원도", "고성")

print(test.GetFirstXpath())
fix1 = test.GetSecondXpath()
fix1 = fix1[1:len(test.GetSecondXpath())]
print(test.GetFirstXpath()+fix1)
print(test.GetSecondXpath())
print(test.GetThirdXpath())
