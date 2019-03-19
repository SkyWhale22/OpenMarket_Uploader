from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Uploader.UploaderBase import UploaderBase
from Items.Base import ItemBase

from openpyxl import load_workbook

from Items.ESM import ItemESM
from Items.ESM import ESMItemInfo
from Items.ESM import Languages

"""
	ESMUploader class definition
"""
class B2BUploader:
	####################################################################################################
	#                                        Member Variables                                          #
	####################################################################################################

	# -------------------------------------------------------------------------------------------------
	# Public
	# -------------------------------------------------------------------------------------------------
	m_itemList = None
	m_driver = None

	####################################################################################################
	#                                        Member Functions                                          #
	####################################################################################################

	# -------------------------------------------------------------------------------------------------
	# Private
	# -------------------------------------------------------------------------------------------------
	def __init__(self):
		print("------- Init! ------")
		self.m_itemList = []
		self.m_path = "C:/Users/kimsu/OneDrive/Documents/Development/chromedriver_win32/chromedriver.exe"
		self.m_driver = webdriver.Chrome(self.m_path)
		self.m_driver.get('https://www.godo.co.kr/')

	# -------------------------------------------------------------------------------------------------
	# Public
	# -------------------------------------------------------------------------------------------------

	def UpLoad(self):
		# Step 1: Sign in to the ESM Plus.
		self.SignIn("hymedi682", "rlawnsgh12")

		# Step 2: Get data from .xlsx file and contain these date in the the list.
		#self.GetDataFromExel()

		# # Step 3: To make it sure, check read data.
		# self.PrintAllItems()
		#
		# # Step 4: While m_itemList contains items, loop the following steps.
		# while(len(self.m_itemList) > 0):
		# 	# Step 5: Get the last item from the list, and remove it from it.
		# 	#         You are able to get an item from head by changing code below 'item = self.m_itemList.pop(0)
		# 	item = self.m_itemList.pop()
		#
		# 	# Step 6: Make the chrome browser getting into item registeration page.
		self.GetInItemRegisterView()
		#
		# 	# Step 7: Fill out basic information of the item which will be uploaded.
		self.SelectCategory()
		#
		# 	# Step 8: Fill out exposure information of the item which will be uploaded.
		# 	self.FillOutExposureInfo(item)
		#
		# 	# Step 9: Fill out additional information of the item which will be uploaded.
		# 	self.FillOutAdditionalInfo(item)
		#
		# 	# Step 10: The last step. Click uploading buttton.
		# 	self.ClickSubmitBtn()

	# SignIn logic
	def SignIn(self, id, pw):

		self.m_driver.switch_to.frame(self.m_driver.find_element_by_xpath('//*[@id="godoLogin"]/iframe'))

		signInID    = self.m_driver.find_element_by_xpath('//*[@id="frmLogin"]/fieldset/div[1]/input[1]')
		signInPW    = self.m_driver.find_element_by_xpath('//*[@id="frmLogin"]/fieldset/div[1]/input[2]')
		signInBtn   = self.m_driver.find_element_by_xpath('//*[@id="frmLogin"]/fieldset/div[2]/button')

		signInID.clear()
		signInPW.clear()

		signInID.send_keys(id)
		signInPW.send_keys(pw)


		signInBtn.click()
		self.m_driver.switch_to.frame(self.m_driver.find_element_by_xpath('//*[@id="godoLogin"]/iframe'))
		btnMyGodo   = self.m_driver.find_element_by_class_name("middle-mygodo")
		btnMyGodo.click()

		self.m_driver.implicitly_wait(2)

		btnAccessMySite = self.m_driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[4]/a[2]')
		btnAccessMySite.click()

		'//*[@id="frmLogin"]'
		self.m_driver.implicitly_wait(2)

		self.m_driver.switch_to.window(self.m_driver.window_handles[1])
		signInID    = self.m_driver.find_element_by_name('managerId')
		signInPW    = self.m_driver.find_element_by_name('managerPw')
		signInBtn   = self.m_driver.find_element_by_xpath('//*[@id="frmLogin"]/table/tbody/tr/td/div/div[1]/div[2]/input')

		signInID.send_keys("helper682")
		signInPW.send_keys("rlawnsgh12***")

		signInBtn.click()



	# Print All item's data on the console.
	# Make sure to comment following code out so that it won't harm the performance.
	# Or make the visual console.
	def PrintAllItems(self):

		for i in range(0, len(self.m_itemList)):
			item = self.m_itemList[i]

	# Get in item registration view
	def GetInItemRegisterView(self):
		btnGoods    = self.m_driver.find_element_by_xpath('//*[@id="menu_goods"]')
		btnGoods.click()

		self.m_driver.implicitly_wait(0.5)

		btnRegister = self.m_driver.find_element_by_xpath('//*[@id="menu"]/div[4]/ul[1]/li[2]/a')
		btnRegister.click()

	def SelectCategory(self):
		self.m_driver.find_element_by_xpath('//*[@id="cateGoods1"]/option[2]').click()
		self.m_driver.find_element_by_xpath('//*[@id="cateGoods2"]/option[2]').click()
		self.m_driver.find_element_by_xpath('//*[@id="btn_category_select"]').click()
		self.m_driver.find_element_by_xpath('//*[@id="depth-toggle-layer-goodsDisplay"]/table/tbody/tr[1]/td[2]/label[2]').click()
		self.m_driver.find_element_by_xpath('//*[@id="depth-toggle-layer-goodsDisplay"]/table/tbody/tr[2]/td[2]/label[2]').click()

	def SetBasicInfo(self):

		pass

	# Fill out additional information of the ite m which will be uploaded.
	def FillOutAdditionalInfo(self, item):
		self.m_driver.find_element_by_xpath('//*[@id="depth-toggle-layer-goodsDisplay"]/table/tbody/tr[1]/td[2]/label[2]/input')

	# Finally, click the submit button.
	def ClickSubmitBtn(self):
		pass
	def GetDataFromExel(self):
		pass
	# Value checker. This check is the variable empty or not.
	def IsAttributeNone(self, attribute):
		if(attribute == None):
			return False

		return True

	def InsertSourceOfOriginData(self, item):
		if (self.IsAttributeNone(item.GetSourceOfOrigin())):
			self.m_driver.find_element_by_xpath(item.GetSourceOfOrigin()).click()
			#item.

# Make sure to comment this out or remove before releasing.
if __name__ == '__main__':
	test = B2BUploader()
	test.UpLoad()