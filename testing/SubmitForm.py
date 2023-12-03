from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest	
import time
import help
from parameterized import parameterized
class SubmitForm(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.vars = {}
		self.driver.get(help.LINK_URL)
		self.driver.set_window_size(1323,1025)
		self.driver.find_element('xpath', '//*[@id="loginForm_phone"]').send_keys(help.PHONE)
		self.driver.find_element('xpath', '//*[@id="loginForm_password"]').send_keys(help.PASSWORD)
		self.driver.find_element('xpath', '//*[@id="loginForm"]/div[5]/div/div/div/div/button').click()
		time.sleep(2)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[5]/div/div[2]/div/div/div/span').click()
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_name"]').send_keys(Keys.CONTROL, 'a')
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_name"]').send_keys(Keys.DELETE)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_phone"]').send_keys(Keys.CONTROL, 'a')
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_phone"]').send_keys(Keys.DELETE)
		# self.driver.implicitly_wait(10)
	def tearDown(self):
		self.driver.quit()
	@parameterized.expand(help.readData("SubmitFormTC1"))
	def testSubmitFormTC1(self,fullName, dob, gender ,diease, phone, email, medicalRecord,description,expected):
		#For submit successfully
		if(email == None):
			email = ""
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_name"]').send_keys(fullName)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_dob"]').send_keys(dob)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_phone"]').send_keys(phone)
		if(gender == 'Male'):
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[1]/span[1]/input').click()
		elif(gender == 'Female'):
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[2]/span[1]/input').click()
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div').click()
		dieaseList = diease.split(',')
		for ds in dieaseList:
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(ds)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(Keys.ENTER)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_email"]').send_keys(email)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_medicalRecord"]').send_keys(medicalRecord)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[6]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("fullName: "+str(fullName))
			print("dob: "+str(dob))
			print("gender: "+str(gender))
			print("diease: "+str(diease))
			print("phone: "+str(phone))
			print("email: "+str(email))
			print("medicalRecord: "+str(medicalRecord))
			time.sleep(5)
			self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
	###########################
	@parameterized.expand(help.readData("SubmitFormTC2"))
	def testSubmitFormTC2(self,fullName, dob, gender ,diease, phone, email, medicalRecord,description,expected):
		#Forget full name
		if(email == None):
			email == ""
		# self.driver.find_element('xpath', '//*[@id="personalHealthForm_name"]').send_keys(fullName)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_dob"]').send_keys(dob)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_phone"]').send_keys(phone)
		if(gender == 'Male'):
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[1]/span[1]/input').click()
		elif(gender == 'Female'):
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[2]/span[1]/input').click()
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div').click()
		dieaseList = diease.split(',')
		for ds in dieaseList:
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(ds)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(Keys.ENTER)
		# self.driver.find_element('xpath', '//*[@id="personalHealthForm_email"]').send_keys(email)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_medicalRecord"]').send_keys(medicalRecord)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[6]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("fullName: "+str(fullName))
			print("dob: "+str(dob))
			print("gender: "+str(gender))
			print("diease: "+str(diease))
			print("phone: "+str(phone))
			print("email: "+str(email))
			print("medicalRecord: "+str(medicalRecord))
			time.sleep(5)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_name_help"]/div')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
	###########################
	@parameterized.expand(help.readData("SubmitFormTC3"))
	def testSubmitFormTC3(self,fullName, dob, gender ,diease, phone, email, medicalRecord,description,expected):
		#Forget dob
		if(email == None):
			email == ""
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_name"]').send_keys(fullName)
		# self.driver.find_element('xpath', '//*[@id="personalHealthForm_dob"]').send_keys(dob)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_phone"]').send_keys(phone)
		if(gender == 'Male'):
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[1]/span[1]/input').click()
		elif(gender == 'Female'):
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[2]/span[1]/input').click()
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div').click()
		dieaseList = diease.split(',')
		for ds in dieaseList:
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(ds)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(Keys.ENTER)
		# self.driver.find_element('xpath', '//*[@id="personalHealthForm_email"]').send_keys(email)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_medicalRecord"]').send_keys(medicalRecord)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[6]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("fullName: "+str(fullName))
			print("dob: "+str(dob))
			print("gender: "+str(gender))
			print("diease: "+str(diease))
			print("phone: "+str(phone))
			print("email: "+str(email))
			print("medicalRecord: "+str(medicalRecord))
			time.sleep(5)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_dob_help"]/div')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
	###########################
	@parameterized.expand(help.readData("SubmitFormTC4"))
	def testSubmitFormTC4(self,fullName, dob, gender ,diease, phone, email, medicalRecord,description,expected):
		#Forget dob
		if(email == None):
			email == ""
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_name"]').send_keys(fullName)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_dob"]').send_keys(dob)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_phone"]').send_keys(phone)
		# if(gender == 'Male'):
		# 	self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[1]/span[1]/input').click()
		# elif(gender == 'Female'):
		# 	self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[2]/span[1]/input').click()
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div').click()
		dieaseList = diease.split(',')
		for ds in dieaseList:
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(ds)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(Keys.ENTER)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_email"]').send_keys(email)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_medicalRecord"]').send_keys(medicalRecord)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[6]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("fullName: "+str(fullName))
			print("dob: "+str(dob))
			print("gender: "+str(gender))
			print("diease: "+str(diease))
			print("phone: "+str(phone))
			print("email: "+str(email))
			print("medicalRecord: "+str(medicalRecord))
			time.sleep(5)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender_help"]/div')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
	###########################
	@parameterized.expand(help.readData("SubmitFormTC5"))
	def testSubmitFormTC5(self,fullName, dob, gender ,diease, phone, email, medicalRecord,description,expected):
		#Forget dob
		if(email == None):
			email == ""
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_name"]').send_keys(fullName)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_dob"]').send_keys(dob)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_phone"]').send_keys(phone)
		if(gender == 'Male'):
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[1]/span[1]/input').click()
		elif(gender == 'Female'):
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[2]/span[1]/input').click()
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div').click()
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_email"]').send_keys(email)
		# dieaseList = diease.split(',')
		# for ds in dieaseList:
		# 	self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(ds)
		# 	self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(Keys.ENTER)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_medicalRecord"]').send_keys(medicalRecord)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[6]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("fullName: "+str(fullName))
			print("dob: "+str(dob))
			print("gender: "+str(gender))
			print("diease: "+str(diease))
			print("phone: "+str(phone))
			print("email: "+str(email))
			print("medicalRecord: "+str(medicalRecord))
			time.sleep(5)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease_help"]/div')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
	###########################
	@parameterized.expand(help.readData("SubmitFormTC6"))
	def testSubmitFormTC6(self,fullName, dob, gender ,diease, phone, email, medicalRecord,description,expected):
		#Forget dob
		if(email == None):
			email == ""
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_name"]').send_keys(fullName)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_dob"]').send_keys(dob)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_email"]').send_keys(email)
		# self.driver.find_element('xpath', '//*[@id="personalHealthForm_phone"]').send_keys(phone)
		if(gender == 'Male'):
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[1]/span[1]/input').click()
		elif(gender == 'Female'):
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[2]/span[1]/input').click()
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div').click()
		dieaseList = diease.split(',')
		for ds in dieaseList:
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(ds)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(Keys.ENTER)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_medicalRecord"]').send_keys(medicalRecord)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[6]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("fullName: "+str(fullName))
			print("dob: "+str(dob))
			print("gender: "+str(gender))
			print("diease: "+str(diease))
			print("phone: "+str(phone))
			print("email: "+str(email))
			print("medicalRecord: "+str(medicalRecord))
			time.sleep(5)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_phone_help"]/div')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
	###########################
	@parameterized.expand(help.readData("SubmitFormTC7"))
	def testSubmitFormTC7(self,fullName, dob, gender ,diease, phone, email, medicalRecord,description,expected):
		#Forget dob
		if(email == None):
			email == ""
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_name"]').send_keys(fullName)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_dob"]').send_keys(dob)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_email"]').send_keys(email)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_phone"]').send_keys(phone)
		if(gender == 'Male'):
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[1]/span[1]/input').click()
		elif(gender == 'Female'):
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[2]/span[1]/input').click()
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div').click()
		dieaseList = diease.split(',')
		for ds in dieaseList:
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(ds)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(Keys.ENTER)
		# self.driver.find_element('xpath', '//*[@id="personalHealthForm_medicalRecord"]').send_keys(medicalRecord)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[6]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("fullName: "+str(fullName))
			print("dob: "+str(dob))
			print("gender: "+str(gender))
			print("diease: "+str(diease))
			print("phone: "+str(phone))
			print("email: "+str(email))
			print("medicalRecord: "+str(medicalRecord))
			time.sleep(5)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_medicalRecord_help"]/div')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:	
			result = "Successful"
		print("Result: " + result )
		print("======")
	###########################
if __name__ == "__main__":
	unittest.main()

