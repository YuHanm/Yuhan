from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

bolgurl ='http://www.cnblogs.com/'
mybolg =bolgurl+'MYuhan'
driver.get(mybolg)
driver.find_element_by_css_selector('#blog_nav_newpost').click()
time.sleep(5)