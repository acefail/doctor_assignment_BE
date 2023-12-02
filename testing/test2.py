from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException

import unittest
import page

from datetime import date, timedelta
import radar
import random

import time

class MoodleQuizCreateMCQTest(unittest.TestCase):
	def setUp(self):
		self.options = Options()
		self.options.add_experimental_option('detach', True)

		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

		# self.driver.maximize_window()

		print('Navigate to Moodle Orange School')
		self.driver.get("http://school.moodledemo.net/")

		# Redirect to Log in Page
		print('Navigate to Log in Page')
		paths = self.driver.find_elements("xpath", '//a[@href]')

		for path in paths:
			if "Log in" in path.get_attribute("innerHTML"):
				path.click()
				break

		# Fill in username = teacher, password = moodle
		self.driver.find_element(By.NAME, 'username').send_keys("teacher")
		self.driver.find_element(By.NAME, 'password').send_keys("moodle")
		self.driver.find_element('xpath', "//button[@type='submit' and @id='loginbtn']").click()
		self.driver.implicitly_wait(5)
		print('Logged in as Teacher')

		# Choose first lecture found
		courses = self.driver.find_elements('xpath', "//a[@href and @class='aalink coursename mr-2 mb-1']")
		print('Courses found:', len(courses))
		for path in courses:
			if "Mindful course creation" in path.get_attribute("innerHTML"):
				path.click()
				print('Choosing Mindful course creation')
				break

		# Enable Edit Mode
		self.driver.find_element('xpath', "//form[@class='d-flex align-items-center editmode-switch-form']").click()

		# Adding Quiz activity
		self.driver.find_element('xpath', "(//button[@class='btn btn-link text-decoration-none section-modchooser section-modchooser-link activity-add bulk-hidden d-flex align-items-center p-3 mb-3'])[1]").click()
		self.driver.find_element('xpath', "//a[@href and @title='Add a new Quiz']").click()
		print('Creating Quiz')
		self.sendkeys_CreateQuizSite(name = 'MCQ Create Test')

		print('Quiz Site added, now navigating to Result page')
		self.driver.find_element('xpath', "//input[@type='submit' and @value='Save and display']").click()
		try:
			self.driver.find_element('xpath', "//button[@type='submit' and text()='Continue']").click()
		except NoSuchElementException:
			pass

		self.driver.find_element('xpath', "//a[@href and text()='Add question']").click()
		print('Now we can attempt add MCQ to Quiz site')
		self.driver.find_element('xpath', "//span[@class='add-menu' and text()='Add']").click()
		self.driver.find_element('xpath', "//a[@href and @data-action='addquestion']").click()
		self.driver.find_element('xpath', "//label[@for='item_qtype_multichoice']").click()
		self.driver.find_element('xpath', "//input[@type='submit' and @value='Add']").click()
		while True:
			try:
				self.driver.find_element('xpath', "//iframe[@id='{}']".format('id_questiontext_ifr'))
				break
			except NoSuchElementException:
				print("TinyMCE Element Not Found, trying to reload")
				self.driver.refresh()
				time.sleep(1)
		# time.sleep(10)

	def isOnQuizCreationSite(self):
		try:
			ele = self.driver.find_element('xpath', "//h2[text()='Adding a new Quiz']")
			return True if ele else False

		except:
			return False

	def sendkeys_CreateQuizSite(self, name = None, opentime = None, closetime = None, timelimit = None):
		print('Sending keys:')
		if name:
			print('-> Inputting Quiz Name: ', name)
			self.driver.find_element('xpath', "//input[@type='text' and @name='name']").send_keys(name)
		else:
			print('~~ No Quiz Name')

		
		print('-> Dropdown Time Selection')
		self.driver.find_element('xpath', "//a[@href='#id_timingcontainer']").click()
		if opentime:
			print('-> Selecting Open Time:', opentime)
			self.driver.find_element('xpath', "//input[@name='timeopen[enabled]']").click()
			openday = Select(self.driver.find_element('xpath', "//select[@name='timeopen[day]']"))
			openmonth = Select(self.driver.find_element('xpath', "//select[@name='timeopen[month]']"))
			openyear = Select(self.driver.find_element('xpath', "//select[@name='timeopen[year]']"))

			openday.select_by_value(str(opentime.day))
			openmonth.select_by_value(str(opentime.month))
			openyear.select_by_value(str(opentime.year))
		else:
			print('~~ No OpenTime')

		if closetime:
			print('-> Selecting Close Time:', closetime)
			self.driver.find_element('xpath', "//input[@name='timeclose[enabled]']").click()
			closeday = Select(self.driver.find_element('xpath', "//select[@name='timeclose[day]']"))
			closemonth = Select(self.driver.find_element('xpath', "//select[@name='timeclose[month]']"))
			closeyear = Select(self.driver.find_element('xpath', "//select[@name='timeclose[year]']"))

			closeday.select_by_value(str(closetime.day))
			closemonth.select_by_value(str(closetime.month))
			closeyear.select_by_value(str(closetime.year))
		else:
			print('~~ No CloseTime')

		if timelimit:
			print('-> Inputing TimeLimit:', timelimit)
			self.driver.find_element('xpath', "//input[@name='timelimit[enabled]']").click()
			timelimitinput = self.driver.find_element('xpath', "//input[@name='timelimit[number]' and @type='text']")
			timelimitinput.clear()
			timelimitinput.send_keys(str(timelimit))
		else:
			print('~~ No Time Limit')

	# def quizhasOpenTime(self):
	# 	try:
	# 		self.driver.find_element('xpath', "//strong[text()='Opens:']")
	# 	except NoSuchElementException:
	# 		return False
		
	# 	return True


	# def quizhasCloseTime(self):
	# 	try:
	# 		self.driver.find_element('xpath', "//strong[text()='Closes:']")
	# 	except NoSuchElementException:
	# 		return False
		
	# 	return True

	# def quizhasTimeLimit(self):
	# 	try:
	# 		self.driver.find_element('xpath', "//p[@class='text-left' and contains(text(), 'Time limit:')]")
	# 	except NoSuchElementException:
	# 		return False
		
	# 	return True

	# def findfeedback(self, feedbackString):
	# 	try:
	# 		self.driver.find_element('xpath', "//div[@class='form-control-feedback invalid-feedback' and contains(text(), '{}')]".format(feedbackString))
	# 	except NoSuchElementException:
	# 		return False
		
	# 	return True


	def sendkeys_TinyMCE(self, id, text):
		textiframe = self.driver.find_element('xpath', "//iframe[@id='{}']".format(id))
		self.driver.switch_to.frame(frame_reference=textiframe)
		self.driver.find_element('xpath', "//body[@id='tinymce']").send_keys(text)
		self.driver.switch_to.default_content()


	def sendkeys_createMCQ(self, name = None, text = None, defMark = None, choice1 = None, grade1 = None, choice2 = None, grade2 = None):
		### Question Name
		if name:
			print('|-- Question name:', name)
			self.driver.find_element('xpath', '//input[@type="text" and @name="name"]').send_keys(name)
		else:
			print('~~~ No Question name!')

		### Question Description
		if text:
			print('|-- Question text:', text)
			self.sendkeys_TinyMCE('id_questiontext_ifr', text)
		else:
			print('~~~ No Question text!')

		### Input Default Mark of this question
		if defMark:
			print('|-- Default Mark:', defMark)
			self.driver.find_element('xpath', '//input[@type="text" and @name="defaultmark"]').send_keys(str(defMark))

		### Choice 1
		if choice1:
			print('|-- Choice 1:', choice1)
			self.sendkeys_TinyMCE('id_answer_0_ifr', choice1)
		else:
			print('~~~ Choice 1 Answer is not given')

		if grade1:
			print('|-- Grade for Choice 1:', grade1)
			grade1select = Select(self.driver.find_element('xpath', "//select[@name='fraction[0]']"))
			grade1select.select_by_value(str(grade1))
		else:
			print('~~~ Grade for Choice 1 is not given, default at 0%')

		### Choice 2
		if choice2:
			print('|-- Choice 2:', choice2)
			self.sendkeys_TinyMCE('id_answer_1_ifr', choice2)
		else:
			print('~~~ Choice 2 Answer is not given')

		if grade2:
			print('|-- Grade for Choice 2:', grade2)
			grade2select = Select(self.driver.find_element('xpath', "//select[@name='fraction[1]']"))
			grade2select.select_by_value(str(grade2))
		else:
			print('~~~ Grade for Choice 2 is not given, default at 0%')

	def questionNameFeedback(self, expect = True):
		try:
			warning = self.driver.find_element('xpath', "//div[@id='id_error_name']")
			if 'You must supply a value here' in warning.get_attribute('innerText'):
				print('|-- Warning of Empty Question Name Found')
			
				if not expect:
					print('|-> Why there is this warning while not expected -- Test Failed')
					self.driver.close()
					self.assertTrue(False, '')

			else:
				print('|-- Question Name is filled in')
				if expect:
					print('|-> This is expected to be empty')
					self.driver.close()
					self.assertTrue(False, '')

		except NoSuchElementException:
			print('|-- Question Name is filled in')
			if expect:
				print('|-> This is expected to be empty')
				self.driver.close()
				self.assertTrue(False, '')

	def questionTextFeedback(self, expect = True):
		try:
			warning = self.driver.find_element('xpath', "//div[@id='id_error_questiontext']")
			if 'You must supply a value here' in warning.get_attribute('innerText'):
				print('|-- Warning of Empty Question Text Found')
			
				if not expect:
					print('|-> Why there is this warning while not expected -- Test Failed')
					self.driver.close()
					self.assertTrue(False, '')

			else:
				print('|-- Question Text is filled in')
				if expect:
					print('|-> This is expected to be empty')
					self.driver.close()
					self.assertTrue(False, '')

		except NoSuchElementException:
			print('|-- Question Text is filled in')
			if expect:
				print('|-> This is expected to be empty')
				self.driver.close()
				self.assertTrue(False, '')

	def choiceFeedback(self, nth_answer):
		try:
			warning = self.driver.find_element('xpath', "//div[@id='id_error_answer_{}']".format(str(nth_answer)))
			if '2 choices' in warning.get_attribute('innerText'):
				print('|-- Warning about less than 2 answer is provided FOUND')
			else:
				print('~~~ No warning feed back at Choice', nth_answer + 1)
		except NoSuchElementException:
			print('~~~ No warning feed back at Choice', nth_answer + 1)

	def gradeFeedback(self, nth_answer):
		try:
			warning = self.driver.find_element('xpath', "//div[@id='id_error_fraction_{}']".format(str(nth_answer)))
			# print(warning.get_attribute('innerText'))
			if 'Grade set' in warning.get_attribute('innerText'):
				print('|-- Warning about Empty Choice {} but Grade {} is set'.format(nth_answer + 1, nth_answer + 1))
			elif 'should be 100%' in warning.get_attribute('innerText'):
				print('|-- Warning no answer with 100% point FOUND')
			else:
				print('~~~ No warning feed back at Grade', nth_answer + 1)
		except NoSuchElementException:
			print('~~~ No warning feed back at Grade', nth_answer + 1)

	def traverseFeedbacks(self, expectOfemptyName=True, expectOfemptyText=True):
		self.questionNameFeedback(expectOfemptyName)
		self.questionTextFeedback(expectOfemptyText)
		self.choiceFeedback(0)
		self.gradeFeedback(0)
		self.choiceFeedback(1)
		self.gradeFeedback(1)

	def isMCQcreated(self):
		try:
			self.driver.find_element('xpath', "//label[text()='Shuffle']")
			print('Shuffle button found')
			return True
		except NoSuchElementException:
			return False

	def test_MCQsuccessful(self):
		print('-------------------------------------------------------------')
		print('Running test_MCQsuccessful:')
		self.sendkeys_createMCQ('test_MCQsuccessful', 'Full information is provided in form', None, 'Choice 1', 1.0, 'Choice 2', 0.5)
		self.driver.find_element('xpath', "//input[@type='submit' and @value='Save changes']").click()
		if self.isMCQcreated():
			print('MCQ created OwO!')
			print('test_MCQsuccessful PASSED!')
			print('-------------------------------------------------------------')
			self.driver.close()
			self.assertTrue(True, '')
		else:
			self.traverseFeedbacks()
			self.driver.close()
			self.assertTrue(False, 'test fail without creating a MCQ while provided with appropriate input')

	def test_gradesetbutNoAnswer(self):
		print('-------------------------------------------------------------')
		print('Running test_gradesetbutNoAnswer:')
		choice1 = 'Choice 1' if bool(random.getrandbits(1)) else None
		choice2 = 'Choice 2' if bool(random.getrandbits(1)) or not choice1 else None

		self.sendkeys_createMCQ('test_gradesetbutNoAnswer', 'Choice is left empty randomly, with Grades set', None, choice1, 1.0, choice2, 0.5)
		self.driver.find_element('xpath', "//input[@type='submit' and @value='Save changes']").click()
		if self.isMCQcreated():
			print('MCQ created OwO!')
			self.driver.close()
			self.assertTrue(False, 'this test should give warning, instead of creating a MCQ')
		else:
			print('Feedbacks found:')
			self.traverseFeedbacks(expectOfemptyName=False, expectOfemptyText=False)
			print('test_gradesetbutNoAnswer PASSED!')
			print('-------------------------------------------------------------')
			self.driver.close()
			self.assertTrue(True, '')

	def test_oneChoice(self):
		print('-------------------------------------------------------------')
		print('Running test_oneChoice:')

		self.sendkeys_createMCQ('test_oneChoice', 'Full information is provided in form', None, "I'm the only choice", 1.0, None, None)
		self.driver.find_element('xpath', "//input[@type='submit' and @value='Save changes']").click()
		if self.isMCQcreated():
			print('MCQ created OwO!')
			self.driver.close()
			self.assertTrue(False, 'this test should give warning, instead of creating a MCQ')
		else:
			print('Feedbacks found:')
			self.traverseFeedbacks(expectOfemptyName=False, expectOfemptyText=False)
			print('test_oneChoice PASSED!')
			print('-------------------------------------------------------------')
			self.driver.close()
			self.assertTrue(True, '')

	def test_no100percentChoice(self):
		print('-------------------------------------------------------------')
		print('Running test_no100percentChoice:')

		self.sendkeys_createMCQ('test_no100percentChoice', 'Full information is provided in form, but grades of the two answer is <100%', None, "Half Choice 1", 0.5, "Half Choice 2", 0.5)
		self.driver.find_element('xpath', "//input[@type='submit' and @value='Save changes']").click()
		if self.isMCQcreated():
			print('MCQ created OwO!')
			self.driver.close()
			self.assertTrue(False, 'this test should give warning, instead of creating a MCQ')
		else:
			print('Feedbacks found:')
			self.traverseFeedbacks(expectOfemptyName=False, expectOfemptyText=False)
			print('test_oneChoice PASSED!')
			print('-------------------------------------------------------------')
			self.driver.close()
			self.assertTrue(True, '')

	
if __name__ == "__main__":
	unittest.main()