from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://www.google.com.hk/')
time.sleep(5)
driver.find_element_by_css_selector('.gsfi').send_keys('自动化测试')
driver.find_element_by_css_selector('#lst-ib').send_keys(Keys.ENTER)

#获取一组定位元素
s = driver.find_elements_by_css_selector('h3.r>a')
for i in s:

    print(i.get_attribute("href"))
t = random.randint(0,10)
a = s[t].get_attribute('href')
driver.get(a)