from selenium import webdriver
from Selenium import ReuseChrome
import time
driver = webdriver.Chrome()
driver.maximize_window()
executor_url = driver.command_executor._url
session_id = driver.session_id
url='http://www.baidu.com/'
driver.get(url)
time.sleep(5)
print(session_id)
print(executor_url)
del driver

driver2 = ReuseChrome.ReuseChrome(command_executor=executor_url, session_id=session_id)
driver2.session_id = session_id
bolgurl = 'http://www.cnblogs.com/'
mybolg =bolgurl+'MYuhan'
driver2.get(mybolg)
driver2.find_element_by_css_selector('#blog_nav_newpost').click()
print(driver2.current_url)
print(session_id)
time.sleep(20)