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
class Login(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.vars = {}
		self.driver.get(help.LINK_URL)
		self.driver.set_window_size(1323,1025)
		# self.driver.implicitly_wait(10)
	def tearDown(self):
		self.driver.quit()
	@parameterized.expand(help.readData("LoginTC1"))
	def testLoginTC1(self,usernameInput, passwordInput,description,expected):
		#For login successfully
		self.driver.find_element('xpath', '//*[@id="loginForm_phone"]').send_keys(usernameInput)
		self.driver.find_element('xpath', '//*[@id="loginForm_password"]').send_keys(passwordInput)
		self.driver.find_element('xpath', '//*[@id="loginForm"]/div[5]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("Phone: "+str(usernameInput))
			print("password: "+str(passwordInput))
			time.sleep(5)
			self.driver.find_element('xpath', '//*[@id="personalHealthForm_name"]').send_keys("hihi")
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
	###########################
	@parameterized.expand(help.readData("LoginTC2"))
	def testLoginTC2(self,usernameInput, passwordInput,description,expected):
		#For wrong password
		self.driver.find_element('xpath', '//*[@id="loginForm_phone"]').send_keys(usernameInput)
		self.driver.find_element('xpath', '//*[@id="loginForm_password"]').send_keys(passwordInput)
		self.driver.find_element('xpath', '//*[@id="loginForm"]/div[5]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("Phone: "+str(usernameInput))
			print("password: "+str(passwordInput))
			time.sleep(2)
			self.driver.find_element('xpath', '/html/body/div[2]/div/div/div/div/div[1]')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
	# 	###########################
	@parameterized.expand(help.readData("LoginTC3"))
	def testLoginTC3(self,usernameInput, passwordInput,description,expected):
		#For wrong phone type
		self.driver.find_element('xpath', '//*[@id="loginForm_phone"]').send_keys(usernameInput)
		self.driver.find_element('xpath', '//*[@id="loginForm_password"]').send_keys(passwordInput)
		self.driver.find_element('xpath', '//*[@id="loginForm"]/div[5]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("Phone: "+str(usernameInput))
			print("password: "+str(passwordInput))
			time.sleep(2)
			self.driver.find_element('xpath', '//*[@id="loginForm_phone_help"]/div')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
		##########################
	@parameterized.expand(help.readData("LoginTC4"))
	def testLoginTC4(self,usernameInput, passwordInput,description,expected):
		#For no phone input
		self.driver.find_element('xpath', '//*[@id="loginForm_phone"]').send_keys(usernameInput)
		self.driver.find_element('xpath', '//*[@id="loginForm_password"]').send_keys(passwordInput)
		self.driver.find_element('xpath', '//*[@id="loginForm"]/div[5]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("Phone: "+str(usernameInput))
			print("password: "+str(passwordInput))
			time.sleep(2)
			self.driver.find_element('xpath', '//*[@id="loginForm_phone_help"]/div')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
		############################
	@parameterized.expand(help.readData("LoginTC5"))
	def testLoginTC5(self,usernameInput, passwordInput,description,expected):
		#For no password input
		self.driver.find_element('xpath', '//*[@id="loginForm_phone"]').send_keys(usernameInput)
		# self.driver.find_element('xpath', '//*[@id="loginForm_password"]').send_keys(passwordInput)
		self.driver.find_element('xpath', '//*[@id="loginForm"]/div[5]/div/div/div/div/button').click()
		try:
			print("Testcase description: "+str(description))
			print("Expected: "+str(expected))
			print("Testcase:")
			print("Phone: "+str(usernameInput))
			print("password: "+str(passwordInput))
			time.sleep(2)
			self.driver.find_element('xpath', '//*[@id="loginForm_password_help"]/div')
			time.sleep(1)
		except NoSuchElementException:
			result = "Unsucessful"
		else:
			result = "Successful"
		print("Result: " + result )
		print("======")
if __name__ == "__main__":
	unittest.main()

