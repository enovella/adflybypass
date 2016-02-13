'''
Read it at: http://robertoviola.org/blog/2014/9/14/adfly-python-bypass
Modifications: @enovella_

v0.1 20160213   First version
'''

import sys

try:
	from selenium import webdriver
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
except Exception:
	sys.exit('''Install dependencies first....
				Selenium and phantomjs
				=======================

				sudo pip2 install selenium 
				sudo apt-get update 
				sudo apt-get install -y phantomjs

			''')

def usage():
	sys.exit("Bypass adf.ly \n\tuse: %s http://adf.ly/badc0de\n\n")


if (len(sys.argv) != 2):
	usage()

url     = sys.argv[1]
driver  = webdriver.PhantomJS('phantomjs')
driver.get(url)
wait    = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID,"skip_button")))
element.click()

#element = driver.find_element_by_id("skip_button")
#print element
#element.click()

print driver.current_url

driver.quit()

