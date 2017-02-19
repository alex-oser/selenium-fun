from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome('./chromedriver.mac')
driver.get('http://orteil.dashnet.org/cookieclicker/')
driver.implicitly_wait(10)
i = 0
while True:
	i += 1
	if i%10000 == 1:
		while True:
			try:
				driver.find_element_by_id('prefsButton').click()
				options = driver.find_elements_by_xpath("//a[@class='option']")
				for option in options:
					if 'Export save' in option.get_attribute('innerHTML'):
						option.click()
						break
				save = driver.find_element_by_id('textareaPrompt').get_attribute('innerHTML')
				print 'Most recent save:', save
				print '*'*80
				driver.find_element_by_xpath("//div[@class='close']").click()
			except StaleElementReferenceException:
				continue
			except WebDriverException:
				print 'Export error'
				continue
			break
	try:
		sell = driver.find_element_by_id('storeBulkSell').get_attribute('class')
		is_selling = 'selected' in sell
		if is_selling:
			driver.find_element_by_id('bigCookie').click()
	except WebDriverException:
		print 'exception'

