from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.baidu.com/"
driver.get(url)
driver.implicitly_wait(10)
mouse = driver.find_element_by_link_text('设置')
time.sleep(5)
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text('搜索设置').click()
driver.find_element_by_xpath('//*[@id="nr"]').click()
s=driver.find_element_by_xpath('//select[@id="nr"]')

Select(s).select_by_value('50').click()
