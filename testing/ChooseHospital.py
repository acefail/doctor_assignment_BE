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
		self.driver.find_element('xpath', '//*[@id="loginForm_phone"]').send_keys("0123456790")
		self.driver.find_element('xpath', '//*[@id="loginForm_password"]').send_keys("nguyenxuantrinh")
		self.driver.find_element('xpath', '//*[@id="loginForm"]/div[5]/div/div/div/div/button').click()
		time.sleep(2)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[5]/div/div[2]/div/div/div/span').click()
		# self.driver.find_element('xpath', '//*[@id="personalHealthForm_name"]').send_keys("fullName")
		# self.driver.find_element('xpath', '//*[@id="personalHealthForm_dob"]').send_keys("2022-02-01")
		# self.driver.find_element('xpath', '//*[@id="personalHealthForm_phone"]').send_keys("0123456789")
		# self.driver.find_element('xpath', '//*[@id="personalHealthForm_gender"]/label[2]/span[1]/input').click()
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div').click()
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys("hear disease")
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_disease"]').send_keys(Keys.ENTER)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_email"]').send_keys("aaaa@gmail.com")
		self.driver.find_element('xpath', '//*[@id="personalHealthForm_medicalRecord"]').send_keys("medicalRecord")
		time.sleep(3)
		self.driver.find_element('xpath', '//*[@id="personalHealthForm"]/div[6]/div/div/div/div/button').click()
		time.sleep(2)
		# self.driver.implicitly_wait(10)
	def tearDown(self):
		self.driver.quit()
	@parameterized.expand(help.readData("ChooseHospitalTC1"))
	def testChooseHospitalTC1(self, hospital, appointment,description,expected):
		#Make appointment successfully
		self.driver.find_element('xpath', '//*[@id="appointmentForm_date"]').send_keys(appointment)
		self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]').send_keys(hospital)
		self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]').click()
		for i in range(0, int(hospital)):
			self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]').send_keys(Keys.DOWN)
		self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]').send_keys(Keys.ENTER)
		self.driver.find_element('xpath', '//*[@id="appointmentForm"]/div[2]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("hospital: "+str(hospital))
			print("appointment: "+str(appointment))
			time.sleep(1)
			self.driver.find_element('xpath', '/html/body/div[2]/div/div')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
	###########################
	@parameterized.expand(help.readData("ChooseHospitalTC2"))
	def testChooseHospitalTC2(self, hospital, appointment,description,expected):
		#Make appointment successfully
		self.driver.find_element('xpath', '//*[@id="appointmentForm_date"]').send_keys(appointment)
		self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]').send_keys("")
		self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]').click()
		if(hospital != None):
			for i in range(0, int(hospital)):
				self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]').send_keys(Keys.DOWN)
			self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]').send_keys(Keys.ENTER)
		self.driver.find_element('xpath', '//*[@id="appointmentForm"]/div[2]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("hospital: "+str(hospital))
			print("appointment: "+str(appointment))
			time.sleep(5)
			self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital_help"]/div')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
	###########################
	@parameterized.expand(help.readData("ChooseHospitalTC3"))
	def testChooseHospitalTC3(self, hospital, appointment,description,expected):
		#Make appointment successfully
		# self.driver.find_element('xpath', '//*[@id="appointmentForm_date"]').send_keys(appointment)
		self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]').send_keys(hospital)
		self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]').click()
		if(hospital != None):
			for i in range(0, int(hospital)):
				self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]').send_keys(Keys.DOWN)
			self.driver.find_element('xpath', '//*[@id="appointmentForm_hospital"]').send_keys(Keys.ENTER)
		self.driver.find_element('xpath', '//*[@id="appointmentForm"]/div[2]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("hospital: "+str(hospital))
			print("appointment: "+str(appointment))
			time.sleep(5)
			self.driver.find_element('xpath', '//*[@id="appointmentForm_date_help"]/div')
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

