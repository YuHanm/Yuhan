from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://www.google.com.hk/')
time.sleep(5)
driver.find_element_by_css_selector('.gsfi').send_keys('自动化测试')
driver.find_element_by_css_selector('#lst-ib').send_keys(Keys.ENTER)
