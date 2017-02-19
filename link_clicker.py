from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome('./chromedriver.mac')
driver.get('https://en.wikipedia.org/wiki/Main_page')
driver.implicitly_wait(10)

pages_visited = 0
pages_to_visit = 100
average = 0
errors = 0
while pages_visited < pages_to_visit:
	try:
		driver.find_element_by_id('n-randompage').click()
		title = random_page = driver.find_element_by_id('firstHeading').get_attribute('innerHTML')
		clicks = 0
		error = False
		while not title == 'Philosophy':
			body = driver.find_element_by_id('mw-content-text')
			p = body.find_elements_by_xpath('./p')
			link = ''
			i = 0
			driver.implicitly_wait(0)
			while link == '':
				try:
					hrefs = p[i].find_elements_by_xpath('./a[@href]')
					for href in hrefs:
						if not '#' in href.get_attribute('outerHTML') and not 'Help' in href.get_attribute('outerHTML') \
						and not 'Greek' in href.get_attribute('innerHTML'):
							link = href
							break
					i += 1
				except NoSuchElementException, IndexError:
					print 'exception'
					i += 1
			driver.implicitly_wait(10)
			print 'about to click:', link.get_attribute('innerHTML')
			link.click()
			title = driver.find_element_by_id('firstHeading').get_attribute('innerHTML')
			clicks += 1
			if clicks > 50:
				print 'More than 50 clicks at', title
				error = True
				errors += 1
				break
		pages_visited += 1
		if not error:	
			print 'Took', clicks, 'clicks to reach Philosophy from', random_page
			average += clicks
	except (WebDriverException, StaleElementReferenceException, IndexError):
		errors += 1
		pages_visited += 1
		print 'Exception at', title

driver.quit()
print 'On average, it took', average/(pages_to_visit-errors), 'clicks to find Philosophy with', errors, 'total error(s).'