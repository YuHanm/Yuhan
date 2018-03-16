from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://passport.csdn.net')

time.sleep(10)