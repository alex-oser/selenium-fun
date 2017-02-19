from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys, time

driver = webdriver.Chrome('./chromedriver.mac')
driver.implicitly_wait(10)
			
try:
	clicks = 0
	while True:
		try:
			# Enter the address of the google form here, a sample link is provided
			driver.get('https://goo.gl/forms/z87TJnolVeHSoT4A3')
			
			# Google makes it difficult to find elements by id, so using XPATH is much 
			# Select multiple choice option 1
			elem = driver.find_element_by_xpath("//*[@id='mG61Hd']/div/div[2]/div[2]/div[1]/div[2]/div/content/div/label[1]/div/div[1]/div[3]/div")
			elem.click()

			# Select checkbox option 1
			elem = driver.find_element_by_xpath("//*[@id='mG61Hd']/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/label/div/div[1]/div[2]")
			elem.click()

			# Select dropdown option 1
			actions = ActionChains(driver)
			actions.send_keys(Keys.TAB+Keys.TAB+Keys.DOWN+Keys.ENTER)
			actions.perform()

			# Enter text in short answer box
			elem = driver.find_element_by_xpath("//*[@id='mG61Hd']/div/div[2]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/input")
			elem.send_keys('Hello world')

			elem = driver.find_element_by_xpath("//*[@id='mG61Hd']/div/div[2]/div[3]/div[1]/div/div")
			elem.click()

			actions = ActionChains(driver)
			actions.send_keys(Keys.TAB+Keys.RETURN)
			actions.perform()

			clicks += 1
		except (WebDriverException, NoSuchElementException, StaleElementReferenceException):
			print 'exception'
			pass
except KeyboardInterrupt:
	sys.exit(''.join(["Congratulations! You filled out the form ",str(clicks)," times!"]))