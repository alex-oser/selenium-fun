from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys

driver = webdriver.Chrome('./chromedriver.mac')
driver.implicitly_wait(10)
			
try:
	fucks = 0
	while True:
		try:
			driver.get('https://docs.google.com/forms/d/e/1FAIpQLScUbXGVlsGDp6svuSE3iBNcytOigFpZfOW11H7On1YZMhw9yQ/viewform?c=0&w=1')
			
			for i in range(1,22):
				driver.find_element_by_xpath("//*[@id='mG61Hd']/div/div[2]/div[2]/div["+str(i)+"]/div[2]/div/content/div/label[1]/div[2]/div/div[3]/div").click()
			driver.find_element_by_xpath("//*[@id='mG61Hd']/div/div[2]/div[2]/div[22]/div[2]/div/content/div/label[10]/div[2]/div/div[3]/div").click()
			actions = ActionChains(driver)
			actions.send_keys(Keys.TAB+Keys.TAB+Keys.RETURN)
			actions.perform()
			fucks += 1
		except (WebDriverException, NoSuchElementException, StaleElementReferenceException):
			pass
except KeyboardInterrupt:
	sys.exit(''.join(["Congratulations! You fucked with Sous ",str(fucks)," times!"]))