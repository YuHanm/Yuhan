from selenium import webdriver
import time
option = webdriver.ChromeOptions()
#伪装成手机
#option.add_argument('--user-agent=iphone')
#获取
option.add_argument('--user-data-dir=C:/Users/Avazu Holding/AppData/Local/Google/Chrome/User Config/Default')
driver = webdriver.Chrome(chrome_options=option)

driver.implicitly_wait(3)
driver.save_screenshot()
bolgurl ='http://www.cnblogs.com/'
mybolg =bolgurl+'MYuhan'
driver.get(mybolg)
driver.find_element_by_css_selector('#blog_nav_newpost').click()
driver.find_element_by_id('Editor_Edit_txbTitle').send_keys('自动化发帖标题')
driver.switch_to.frame("Editor_Edit_EditorBody_ifr")
driver.find_element_by_id("tinymce").send_keys('正文内容')

time.sleep(5)
#driver.quit()