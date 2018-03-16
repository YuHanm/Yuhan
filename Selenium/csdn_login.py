from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://passport.csdn.net/account/login')
time.sleep(5)
driver.find_element_by_css_selector('#username').send_keys('1138941694@qq.com')
driver.find_element_by_css_selector('.pass-word').send_keys('521125')
driver.find_element_by_class_name('logging').click()
time.sleep(5)
driver.find_element_by_css_selector('.toolbar_to_feed').click()