from selenium import webdriver
import time
option = webdriver.ChromeOptions()
#伪装成手机
#option.add_argument('--user-agent=iphone')
#获取
option.add_argument('--user-data-dir=C:/Users/Avazu Holding/AppData/Local/Google/Chrome/User Data/Default')
driver = webdriver.Chrome(chrome_options=option)

driver.implicitly_wait(3)

bolgurl ='http://www.cnblogs.com/'
mybolg =bolgurl+'MYuhan'
driver.get(mybolg)
driver.find_element_by_css_selector('#blog_nav_newpost').click()
time.sleep(5)
driver.quit()