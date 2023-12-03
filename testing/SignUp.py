from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest	
import time
import help
from parameterized import parameterized
class SignUp(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.vars = {}
		self.driver.get(help.LINK_URL)
		self.driver.find_element('xpath', '//*[@id="loginForm"]/div[6]/span').click()
		self.driver.set_window_size(1323,1025)
		# self.driver.implicitly_wait(10)
	def tearDown(self):
		self.driver.quit()
	@parameterized.expand(help.readData("SignUp"))
	def testSignUp(self,phone, fullName, password, confirmPassword, dob, gender,description):
		# if(usernameInput == None):
		# 	usernameInput = ""
		# if(passwordInput == None):
		# 	passwordInput = ""
		self.driver.find_element('xpath', '//*[@id="registerForm_phone"]').send_keys(phone)
		self.driver.find_element('xpath', '//*[@id="registerForm_fullName"]').send_keys(fullName)
		self.driver.find_element('xpath', '//*[@id="registerForm_password"]').send_keys(password)
		self.driver.find_element('xpath', '//*[@id="registerForm_dob"]').send_keys(dob)
		self.driver.find_element('xpath', '//*[@id="registerForm_confirmPassword"]').send_keys(confirmPassword)
		if(gender == 'Male'):
			self.driver.find_element('xpath', '//*[@id="registerForm_gender"]/label[1]/span[1]/input').click()
		elif(gender == 'Female'):
			self.driver.find_element('xpath', '//*[@id="registerForm_gender"]/label[2]/span[1]/input').click()
		#submit
		self.driver.find_element('xpath', '//*[@id="registerForm"]/div[4]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Testcase value:")
			print("Phone: "+str(phone))
			print("fullName: "+str(fullName))
			print("password: "+str(password))
			print("confirmPassword: "+str(confirmPassword))
			print("dob: "+str(dob))
			print("gender: "+str(gender))
			time.sleep(2)
			self.driver.find_element('xpath', '//*[@id="loginForm_password"]').send_keys("1")
		except NoSuchElementException:
			print("SignUp failed")
		else:
			print("SignUp successful")
		print("======")

		
if __name__ == "__main__":
	unittest.main()

